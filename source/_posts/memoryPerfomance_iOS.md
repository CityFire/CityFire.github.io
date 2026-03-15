---
date: 2023-08-02 09:03:49
title: 关于iOS内存的深入排查和优化
---

一些内存相关的名词
## 虚拟内存VM
虚拟内存机制在这里就不多说了，主要包括内存管理单元MMU、内存映射、分段、分页。在iOS中，一页通常有16KB的内存空间。
分配内存的时候，先分配虚拟内存，然后使用的时候再映射到实际的物理内存。
一个`VM Region`指的是一段连续的虚拟内存页，这些页的属性都相同。
```
/* localized structure - cannot be safely passed between tasks of differing sizes */
/* Don't use this, use MACH_TASK_BASIC_INFO instead */
struct task_basic_info {
    integer_t       suspend_count;  /* suspend count for task */
    vm_size_t       virtual_size;   /* virtual memory size (bytes) */
    vm_size_t       resident_size;  /* resident memory size (bytes) */
    time_value_t    user_time;      /* total user run time for
                                     *  terminated threads */
    time_value_t    system_time;    /* total system run time for
                                     *  terminated threads */
    policy_t        policy;         /* default policy for new threads */
};

struct mach_task_basic_info {
    mach_vm_size_t  virtual_size;       /* virtual memory size (bytes) */
    mach_vm_size_t  resident_size;      /* resident memory size (bytes) */
    mach_vm_size_t  resident_size_max;  /* maximum resident memory size (bytes) */
    time_value_t    user_time;          /* total user run time for
                                         *  terminated threads */
    time_value_t    system_time;        /* total system run time for
                                         *  terminated threads */
    policy_t        policy;             /* default policy for new threads */
    integer_t       suspend_count;      /* suspend count for task */
};
```
复制代码

VM分为`Clean Memory`和`Dirty Memory`。即:
虚拟内存 `Virtual Memory = Dirty Memory + Clean Memory + Compressed Memory`。
复制代码
使用`malloc`函数，申请一段堆内存，则该内存为`Clean`的。一旦写入数据，通常这块内存会变成`Dirty`。
获取App申请到的所有虚拟内存：
```
- (int64_t)memoryVirtualSize {
    struct task_basic_info info;
    mach_msg_type_number_t size = (sizeof(task_basic_info_data_t) / sizeof(natural_t));
    kern_return_t ret = task_info(mach_task_self(), TASK_BASIC_INFO, (task_info_t)&info, &size);
    if (ret != KERN_SUCCESS) {
        return 0;
    }
    return info.virtual_size;
}
```
复制代码

`mach_task_self()`表示获取当前的`Mach task`。
## Clean Memory
可以简单理解为能够被写入数据的干净内存。对开发者而言是read-only，而iOS系统可以写入或移除。
```
1. System Framework、Binary Executable占用的内存
2. 可以被释放（Page Out，iOS上是压缩内存的方式）的文件，包括内存映射文件Memory mapped file（如image、data、model等）。内存映射文件通常是只读的。
3. 系统中可回收、可复用的内存，实际不会立即申请到物理内存，而是真正需要的时候再给。
4. 每个framework都有_DATA_CONST段，当App运行时使用到了某个framework，该framework对应的_DATA_CONST的内存就由clean变为dirty了。
```
注意：如果通过文件内存映射机制memory mapped file载入内存的，可以先清除这部分内存占用，需要的时候再从文件载入到内存。所以是Clean Memory。

## Dirty Memory

主要强调不可被重复使用的内存。对开发者而言，已经写入数据。
```
1. 被写入数据的内存，包括所有heap中的对象、图像解码缓冲(ImageIO, CGRasterData，IOSurface)。
2. 已使用的实际物理内存，系统无法自动回收。
3. heap allocation、caches、decompressed images。
4. 每个framework的_DATA段和_DATA_DIRTY段。
```
iOS中的内存警告，只会释放clean memory。因为iOS认为dirty memory有数据，不能清理。所以，应尽量避免dirty memory过大。

要清楚地知道Allocations和Dirty Size分别是因为什么？

值得注意的是，在使用 framework 的过程中会产生 Dirty Memory，使用单例或者全局初始化方法是减少 Dirty Memory 不错的方法，因为单例一旦创建就不会销毁，全局初始化方法会在 class 加载时执行。

下方有测量实验，如+50dirty的操作，在release环境不生效，因iOS系统自动做了优化。
## Compressed Memory

iOS设备没有swapped memory，而是采用Compressed Memory机制，一般情况下能将目标内存压缩至原有的一半以下。对于缓存数据或可重建数据，尽量使用NSCache或NSPurableData，收到内存警告时，系统自动处理内存释放操作。并且是线程安全的。

这里要注意，压缩内存机制，使得内存警告与释放内存变得稍微复杂一些。即，对于已经被压缩过的内存，如果尝试释放其中一部分，则会先将它解压。而解压过程带来的内存增大，可能得到我们并不期待的结果。如果选用NSDictionary之类的，内存比较紧张时，尝试将NSDictionary的部分内存释放掉。但若NSDictionary之前是压缩状态，释放需要先解压，解压过程可能导致内存增大而适得其反。

所以，我们平常开发所关心的内存占用其实是 Dirty Size和Compressed Size两部分，也应尽量优化这两部分。而Clean Memory一般不用太多关注。

## Resident Memory

已经被映射到虚拟内存中的物理内存。而phys_footprint才是真正消耗的物理内存。

`Resident Memory = Dirty Memory + Clean Memory that loaded in pysical memory`。

复制代码

获取App消耗的Resident Memory：
```
- (int64_t)memoryResidentSize {
    struct task_basic_info info;
    mach_msg_type_number_t size = sizeof(task_basic_info_data_t) / sizeof(natural_t);
    kern_return_t ret = task_info(mach_task_self(), TASK_BASIC_INFO, (task_info_t)&info, &size);
    if (ret != KERN_SUCCESS) {
        return 0;
    }
    return info.resident_size;
}
```
复制代码
```
Memory Footprint
/*
* phys_footprint
*   Physical footprint: This is the sum of:
*     + (internal - alternate_accounting)
*     + (internal_compressed - alternate_accounting_compressed)
*     + iokit_mapped
*     + purgeable_nonvolatile
*     + purgeable_nonvolatile_compressed
*     + page_table
*
* internal
*   The task's anonymous memory, which on iOS is always resident.
*
* internal_compressed
*   Amount of this task's internal memory which is held by the compressor.
*   Such memory is no longer actually resident for the task [i.e., resident in its pmap],
*   and could be either decompressed back into memory, or paged out to storage, depending
*   on our implementation.
*
* iokit_mapped
*   IOKit mappings: The total size of all IOKit mappings in this task, regardless of
    clean/dirty or internal/external state].
*
* alternate_accounting
*   The number of internal dirty pages which are part of IOKit mappings. By definition, these pages
*   are counted in both internal *and* iokit_mapped, so we must subtract them from the total to avoid
*   double counting.
*/
```
复制代码

App消耗的实际物理内存，包括：
```
1. Dirty Memory
2. Clean memory but loaded in pysical memory
3. Page Table
4. Compressed Memory
5. IOKit used
6. NSCache， Purgeable等
```
获取App的Footprint：
```
- (int64_t)memoryPhysFootprint {
    task_vm_info_data_t vmInfo;
    mach_msg_type_number_t count = TASK_VM_INFO_COUNT;
    kern_return_t ret = task_info(mach_task_self(), TASK_VM_INFO, (task_info_t)&vmInfo, &count);
    if (ret != KERN_SUCCESS) {
        return 0;
    }
    return vmInfo.phys_footprint;
}
```
复制代码

XNU中Jetsam判断内存过大，使用的也是phys_footprint，而非resident size。
获取设备的所有物理内存大小，可以使用
```
[NSProcessInfo processInfo].physicalMemory
```
复制代码

内存测量结果

测量环境
iPhone 7, iOS 13.3。
Clean Memory
初始状态
```
类型	内存值(MB)	分析	
resident	59	App消耗的内存	
footprint	13	实际物理内存	
VM	4770	App分配的虚拟内存	
Xcode Navigator	14.3	footprint + 调试需要	
```
加50MB的clean memory

代码为：
```
__unused char *buf = malloc(50 * 1024 * 1024);
```
复制代码
```
类型	内存值(MB)	增量	分析
resident	60	+1	App消耗的内存
footprint	14	+1	实际物理内存
VM	4817	+47	App分配的虚拟内存
Xcode Navigator	14.3	+0	footprint + 调试需要
```
实际，仅增加50MB的VM，而这里额外会有1～2MB的footprint增加，猜测是用于内存映射所需的。

到达虚拟内存上限会报错： error: can't allocate region，但不会导致崩溃***。
同时，申请的过程不会耗时。

再加50MB的clean memory
```
类型	内存值(MB)	增量	分析
resident	60	+0	App消耗的内存
footprint	14	+0	实际物理内存
VM	4868	+51	App分配的虚拟内存
Xcode Navigator	14.3	+0	footprint + 调试需要
```
## Dirty Memory
Resident、footprint、VM都增加。是实实在在的内存消耗，各个工具都会统计。
初始状态
```
类型	内存值(MB)	分析	
resident	59	App消耗的内存	
footprint	13	实际物理内存	
VM	4769	App分配的虚拟内存	
Xcode Navigator	14.3	footprint + 调试需要	
```
加50MB的dirty memory
代码为：
// 仅此一句，依然是仅申请虚拟内存，物理内存不会变
```
char *buf = malloc(50 * 1024 * 1024 * sizeof(char));
```

// 内存使用了，所以是实际的物理内存被使用了。即内存有数据了，变成dirty memory。
```
for (int i = 0; i < 50 * 1024 * 1024; i++) {
    buf[i] = (char)rand();
}
```
复制代码
```
类型	内存值(MB)	增量	分析
resident	110	+51	App消耗的内存
footprint	64	+51	实际物理内存
VM	4817	+48	App分配的虚拟内存
Xcode Navigator	64.4	+50.1	footprint + 调试需要
```
实际增加了50MB的物理内存，Resident Memory也会变化，同时额外多了1～2MB。
申请过程比较耗时，超出上限会导致崩溃。
但该操作仅在debug下生效，release环境不生效，应该是iOS系统自行的优化。
再加50MB的dirty memory
```
类型	内存值(MB)	增量	分析
resident	160	+50	App消耗的内存
footprint	114	+50	实际物理内存
VM	4868	+51	App分配的虚拟内存
Xcode Navigator	114.4	+50	footprint + 调试需要
```
`Clean Memory + Dirty Memory`

初始状态
```
类型	内存值(MB)	分析	
resident	59	App消耗的内存	
footprint	13	实际物理内存	
VM	4770	App分配的虚拟内存	
Xcode Navigator	14.3	footprint + 调试需要	
```
加50MB的clean memory，使用其中10MB

代码为：
// 申请50MB的虚拟内存
```
char *buf = malloc(50 * 1024 * 1024 * sizeof(char));
```

// 实际只用了10MB，所以10MB的dirty memory
```
for (int i = 0; i < 10 * 1024 * 1024; i++) {
    buf[i] = (char)rand();
}
```
复制代码
```
类型	内存值(MB)	增量	分析
resident	70	+11	App消耗的内存
footprint	24	+11	实际物理内存
VM	4817	+47	App分配的虚拟内存
Xcode Navigator	24.3	+10	footprint + 调试需要
```
申请了50MB，但实际仅使用了10MB，因此只有这10MB为Dirty Memory。
再加50MB的clean memory，使用其中10MB
```
类型	内存值(MB)	增量	分析
resident	80	+10	App消耗的内存
footprint	34	+10	实际物理内存
VM	4868	+51	App分配的虚拟内存
Xcode Navigator	34.3	+10	footprint + 调试需要
```
#### VM
初始状态
```
类型	内存值(MB)	分析	
resident	59	App消耗的内存	
footprint	13	实际物理内存	
VM	4770	App分配的虚拟内存	
Xcode Navigator	14.3	footprint + 调试需要
```	
加100MB的VM
代码为：
```
vm_address_t address;
vm_size_t size = 100*1024*1024;
// VM Tracker中显示Memory Tag 200
vm_allocate((vm_map_t)mach_task_self(), &address, size, VM_MAKE_TAG(200) | VM_FLAGS_ANYWHERE);
// VM Tracker中显示VM_MEMORY_MALLOC_HUGE
// vm_allocate((vm_map_t)mach_task_self(), &address, size, VM_MAKE_TAG(VM_MEMORY_MALLOC_HUGE) | VM_FLAGS_ANYWHERE);
```
复制代码
```
类型	内存值(MB)	增量	分析
resident	60	+1	App消耗的内存
footprint	14	+1	实际物理内存
VM	4867	+97	App分配的虚拟内存
Xcode Navigator	14.3	+0	footprint + 调试需要
```
这里，mach_task_self()表示在自己的进程空间内申请，size的单位是byte。使用参数VM_MAKE_TAG(200)给申请的内存提供一个Tag标记，该数字在VM Tracker中会有标记。
再加100MB的VM
```
类型	内存值(MB)	增量	分析
resident	60	+0	App消耗的内存
footprint	14	+0	实际物理内存
VM	4967	+100	App分配的虚拟内存
Xcode Navigator	14.3	+0	footprint + 调试需要
```
#### UIImage
图片大小：map.jpg: 9054*5945
初始状态
```
类型	内存值(MB)	分析	
resident	60	App消耗的内存	
footprint	14	实际物理内存	
VM	4768	App分配的虚拟内存	
Xcode Navigator	14.3	footprint + 调试需要	
```
```
self.image = [UIImage imageNamed:@"map.jpg"]
```
```
类型	内存值(MB)	增量	分析
resident	61	+2	App消耗的内存
footprint	14	+0	实际物理内存
VM	4768	+0	App分配的虚拟内存
Xcode Navigator	14.4	+0.1	footprint + 调试需要
```
构建UIImage对象所需要的图片数据消耗其实不大。这里的数据指的是压缩的格式化数据。
```
self.imageView.image = self.image;
```
```
类型	内存值(MB)	增量	分析
resident	61	+0	App消耗的内存
footprint	92	+78	实际物理内存
VM	4845	+77	App分配的虚拟内存
Xcode Navigator	92	+77.6	footprint + 调试需要
```
这个阶段，需要将图片数据解码成像素数据bitmap，并渲染到屏幕上。解码过程非常消耗内存和CPU资源，且默认在主线程中执行会阻塞主线程。
关于这里的一些详细信息及优化（如异步解码图片数据，主线程渲染），请看后文。
结论
通过以上的比较，可以对各个内存类型有一个初步直观的认识。
```
1. footprint是App实际消耗的物理内存
2. resident是实际映射到虚拟内存的物理内存
3. 通常看到的Xcode Navigator显示的最接近footprint，另外还有一些调试需要的内存。
```
几种内存查看方式的区别
### Xcode Navigator
初略展示了真实的物理内存消耗。颜色表明了内存占用是否合理。Xcode Navigator = footprint + 调试需要。不跟踪VM。往往初略观察App的内存占用情况，不能作为精确的参考。
Instuments Allocations
这里显示的内存，其实只是整个App占用内存的一部分，即开发者自行分配的内存，如各种类实例等。简单而言，就是开发者自行malloc申请的。
```
1. 主要是MALLOC_XXX, VM Region, 以及部分App进程创建的VM Region。
2. 非动态的内存，及部分其他动态库创建的VM Region并不在Allocations的统计范围内。
3. 主程序或动态库的_DATA数据段、Stack函数栈，并非通过malloc分配，因此不在Allocations统计内。
```
### All Heap Allocations
```
1. malloc
2. CFData
3. 其他手动申请的内存，如 *char buf = malloc(50 * 1024 * 1024 * sizeof(char));
```
### Malloc
开发者手动分配的内存块，比如一些人脸检测模型等，还有一些C/C++代码中的。
### All Anonymous VM
无法由开发者直接控制，一般由系统接口调用申请的。例如图片之类的大内存，属于All Anonymous VM -> VM: ImageIO_IOSurface_Data，其他的还有IOAccelerator与IOSurface等跟GPU关系比较密切的.
### VM: IOAccelerator
```
CVPixelBuffer: An image buffer that holds pixels in main memory.
A Core Video pixel buffer is an image buffer that holds pixels in main memory. Applications generating frames, compressing or decompressing video, or using Core Image can all make use of Core Video pixel buffers.
主要是CVPixelBuffer，通常使用Pool来管理，交给系统自动释放。而释放的时机完全由系统决定，开发者无法控制。
如果不太需要复用的话，可以考虑改为直接使用create函数，不再复用。这样能保证及时释放掉。
```
### VM: IOSurface
IOSurface是用于存储FBO、RBO等渲染数据的底层数据结构，是跨进程的，通常在CoreGraphics、OpenGLES、Metal之间传递纹理数据。该结构和硬件相关。提供CPU访问VRAM的方式，如创建IOSurface对象后，在CPU往对象里塞纹理数据，GPU就可以直接使用该纹理了。可以简单理解为IOSurface，为CPU和GPU直接搭建了一个传递纹理数据的桥梁。
```
Share hardware-accelerated buffer data (framebuffers and textures) across multiple processes. Manage image memory more efficiently.
The IOSurface framework provides a framebuffer object suitable for sharing across process boundaries. It is commonly used to allow applications to move complex image decompression and draw logic into a separate process to enhance security.
```
以下内容参考自：iOS 内存管理研究，总结得非常到位了。
（CGImage是一个可以惰性初始化(持有原始压缩格式DataBuffer)，并且通过类似引用计数管理真正的Image Bitmap Buffer的设计，
只有渲染时通过RetainBytePtr拿到Bitmap Buffer塞给VRAM(IOSurface)，不渲染时ReleaseBytePtr释放Bitmap Buffer，DataBuffer占用本身就小）。
通常我们使用UIImageView，系统会自动处理解码过程，在主线程上解码和渲染，会占用CPU，容易引起卡顿。
推荐使用ImageIO在后台线程执行图片的解码操作（可参考SDWebImageCoder）。但是ImageIO不支持webp。
```
ASDK的原理：拿空间换时间，换取流畅，牺牲内存，但内存开销比UIKit高。
	正常用一个全屏的UIImageView，直接用image = UIImage(named:xxx)来设置图片，要在主线程解码，但消耗内存反而较小，只有4MB（正常需要10MB）。
	应该是IOSurface对图片数据做了一些优化。但如果是非常大的图片就会阻塞，不建议直接渲染。
	CGImage是一个可以惰性初始化（持有原始压缩格式DataBuffer），并且通过类似ARC管理真正的Image Bitmap Buffer的设计。
	只有渲染时候通过RatainBytePtr拿到Bitmap Buffer塞给VRAM（IOSurface），不渲染时ReleaseBytePtr释放Bitmap Buffer，DataBuffer本身占用很小。
```
复制代码
## VM: Stack
调用堆栈，一般不需要做啥。每个线程都需要500KB左右的栈空间，主线程1MB。
## VM: CG raster data
SDWebImage的图片解码数据的缓存，为了避免渲染时在主线程解码导致阻塞。如果对于这一点比较介意，可以做相应设置即可：
```
/// Decompressing images that are downloaded and cached can improve peformance but can consume lot of memory.
/// Defaults to YES. Set this to NO if you are experiencing a crash due to excessive memory consumption.
[[SDImageCache sharedImageCache] setShouldDecompressImages:NO];
[[SDWebImageDownloader sharedDownloader] setShouldDecompressImages:NO];
[[SDImageCache sharedImageCache] setShouldCacheImagesInMemory:NO];
```
复制代码
常见堆栈：
```
mmap
CGDataProvicerCreateWithCopyOfData
CGBitmapContextCreateImage
[SDWebImageWebPCoder decodedImageWithData:]
[SDWebImageCodersManager decodedImageWithData:]
[SDImageCache diskImageForKey:data:options:]
[SDImageCache queryCacheOperationForKey:options:done:]_block_invoke
```
复制代码
## Instuments VM Tracker
interesting VM regions such as graphics- and Core Data-related. Hides mapped files, dylibs, and some large reserved VM regions.
比较大块的内存占用，如WebKit、ImageIO、CoreAnimation等VM Region，一般由系统生成和管理。
```
1. 数据段_DATA，如占用VM为10.6MB，Resident为6261KB，Dirty为1930KB。
2. 数据段_DATA_CONST，每个framework都有，当App在运行时用到了该framework，则此段内存由clean变为dirty。如占用VM为33.9MB，Resident为31.5MB，Dirty为4466KB。
3. 数据段_DATA_DIRTY，每个framework都有_DATA段和_DATA_DIRTY段，内存是dirty的。如占用VM为862KB，Resident为798KB，Dirty为451KB。
4. 有_LINKEDIT，包含了方法和变量的元数据（位置、偏移量），及代码签名等信息。如占用VM为98MB，Resident为22.4MB，Dirty为0KB. 注意：Dirty为0.
5. 代码段_TEXT，如占用VM为252.9MB，Resident为133.7MB，Dirty为80KB。 注意：Dirty几乎为0.
6. mapped file，如占用VM为104.4MB，Resident为7472KB，Dirty为32KB。clean memory。
7. shared memory，如占用VM为64KB，Resident为64KB，Dirty为64KB。
8. unused but dirty shlib __DATA，如占用VM为721KB，Resident为721KB，Dirty为721KB。
```
其他比如MALLOC_LARGE，MALLOC_NANO等都是申请VM的时候设置的tag。
```
1. MALLOC_LARGE, 如占用VM为384KB，Resident为384KB，Dirty为384KB。
2. MALLOC_NANO, 如占用VM为512MB，Resident为1584KB，Dirty为1568KB。
3. MALLOC_SMALL, 如占用VM为24MB，Resident为896KB，Dirty为800KB。
4. MALLOC_TINY, 如占用VM为4096KB，Resident为432KB，Dirty为432KB。
5. Stack, 如占用VM为2096KB，Resident为144KB，Dirty为128KB。
6. Performance tool data, 调试所需，如占用VM为336KB，Resident为336KB，Dirty为336KB。
```
