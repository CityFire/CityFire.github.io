---
title: NSCFConstantString & __NSCFString & NSTaggedPointerString
---

## __NSCFConstantString

字符串常量，是一种编译时常量，它的 retainCount 值很大，是 4294967295，在控制台打印出的数值则是 18446744073709551615==2^64-1，测试证明，即便对其进行 release 操作，retainCount 也不会产生任何变化。是创建之后便是放不掉的对象。相同内容的 __NSCFConstantString 对象的地址相同，也就是说常量字符串对象是一种单例。

这种对象一般通过字面值 @"..."、CFSTR("...") 或者 stringWithString: 方法（需要说明的是，这个方法在 iOS6 SDK 中已经被称为redundant，使用这个方法会产生一条编译器警告。这个方法等同于字面值创建的方法）产生。

这种对象存储在字符串常量区。

## __NSCFString

和 __NSCFConstantString 不同， __NSCFString 对象是在运行时创建的一种 NSString 子类，他并不是一种字符串常量。所以和其他的对象一样在被创建时获得了 1 的引用计数。
通过 NSString 的 stringWithFormat 等方法创建的 NSString 对象一般都是这种类型。
这种对象被存储在堆上。


## NSTaggedPointerString

理解这个类型，需要明白什么是标签指针，这是苹果在 64 位环境下对 NSString,NSNumber 等对象做的一些优化。简单来讲可以理解为把指针指向的内容直接放在了指针变量的内存地址中，因为在 64 位环境下指针变量的大小达到了 8 位足以容纳一些长度较小的内容。于是使用了标签指针这种方式来优化数据的存储方式。从他的引用计数可以看出，这货也是一个释放不掉的单例常量对象。在运行时根据实际情况创建。

对于 NSString 对象来讲，当非字面值常量的数字，英文字母字符串的长度小于等于 9 的时候会自动成为 NSTaggedPointerString 类型，如果有中文或其他特殊符号（可能是非 ASCII 字符）存在的话则会直接成为 ）__NSCFString 类型。

这种对象被直接存储在指针的内容中，可以当作一种伪对象。

0x01 引用计数为什么会是18446744073709551615？

这个值意味着无限的retainCount，这个对象是不能被释放的。所有的 NSCFConstantString对象的retainCount都是这个值，这就意味着 NSCFConstantString不会被释放，使用第一种方法创建的NSString，如果值一样，无论写多少遍，都是同一个对象。而且这种对象可以直接用 == 来比较。

```
* copy： 对NSArray是浅拷贝，NSMutableArray是深拷贝

* mutableCopy： 始终是深拷贝


* 无论深浅拷贝，集合对象内元素都是浅拷贝
```

我们发现系统系统了方法`- (instancetype)initWithArray:(NSArray<ObjectType> *)array copyItems:(BOOL)flag`
其中`copyItems:(BOOL)flag`表示是否拷贝元素，我们先代码测试一下

```
NSString *str1 = @"hello world";
    NSMutableString *str2 = [NSMutableString stringWithString:@"hello world"];
    NSArray *array1 = [NSArray arrayWithObjects: str1, str2, nil];
    NSMutableArray *array2 = [[NSMutableArray alloc] initWithArray:array1 copyItems:true];
    NSLog(@"\n array1 = %p class = %@ \n", array1, [array1 class]);
    NSLog(@"\n array2 = %p class = %@ \n", array2, [array2 class]);
    NSLog(@"\n\n======== 元素是String ======== ");
    NSLog(@"\n obj0 = %p class = %@ \n", array1[0], [array1[0] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array2[0], [array2[0] class]);
    NSLog(@"\n\n======== 元素是mutableString ========");
    NSLog(@"\n obj0 = %p class = %@ \n", array1[1], [array1[1] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array2[1], [array2[1] class]);
```
查看输出(为了下文对比，我对输出做了line标记)
```
2021-05-09 10:59:16.343163+0800 AlgorithmDemo[9904:51756] 
 array1 = 0x100607650 class = __NSArrayI  (line1)
 array2 = 0x1006074a0 class = __NSArrayM (line2)
======== 元素是String ======== 
 obj0 = 0x100008220 class = __NSCFConstantString (line3)  
 obj0 = 0x100008220 class = __NSCFConstantString (line4)
======== 元素是mutableString ========
 obj0 = 0x100606330 class = __NSCFString (line5)
 obj0 = 0x100605430 class = __NSCFString (line6)
```

根据输出我们对得出系统`initWithArray : copyItems :`方法如下结论

```
* 该方法对NSArray对象是深拷贝 (严格意义来说此处不能称为拷贝，是生成新对象) （line1 line2）

* 当数组内元素为不可变对象时，该方法对元素执行浅拷贝(line3 line4)
应该是NSCFConstantString的问题导致地址相同
* 当数组内元素为可变对象时，该方法对元素执行深拷贝(line4 line5)

？？？ 由此我们知道，当我们想深拷贝NSArray及其内部的元素时，用系统方法- (instancetype)initWithArray:(NSArray<ObjectType> *)array copyItems:(BOOL)flag是不行的
```




### 2. 归档

如果我们对Array执行归档再解档，结果会是什么样的呢，我们代码测试一下

```
NSString *str1 = @"hello world";
    NSMutableString *str2 = [NSMutableString stringWithString:@"hello world"];
    NSArray *array1 = [NSArray arrayWithObjects: str1, str2, nil];
    NSMutableArray *array2 = [[NSMutableArray alloc] initWithArray:array1 copyItems:true];
    
    NSData *data = [NSKeyedArchiver archivedDataWithRootObject:array1];
    NSMutableArray *array3 = [NSKeyedUnarchiver unarchiveObjectWithData:data];
    
    NSLog(@"\n array1 = %p class = %@ \n", array1, [array1 class]);
    NSLog(@"\n array2 = %p class = %@ \n", array2, [array2 class]);
    NSLog(@"\n array3 = %p class = %@ \n", array3, [array3 class]);
    
    NSLog(@"\n\n======== 元素是String ======== ");
    NSLog(@"\n obj0 = %p class = %@ \n", array1[0], [array1[0] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array2[0], [array2[0] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array3[0], [array3[0] class]);
    
    NSLog(@"\n\n======== 元素是mutableString ========");
    NSLog(@"\n obj0 = %p class = %@ \n", array1[1], [array1[1] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array2[1], [array2[1] class]);
    NSLog(@"\n obj0 = %p class = %@ \n", array3[1], [array3[1] class]);
```
查看输出

```
2021-05-09 11:14:50.710409+0800 AlgorithmDemo[12261:67019] 
 array1 = 0x1006b9e40 class = __NSArrayI  (line1)
 array2 = 0x1006ba180 class = __NSArrayM  (line1)
 array3 = 0x1006b7410 class = __NSArrayI  (line1)
======== 元素是String ======== 
 obj0 = 0x100008220 class = __NSCFConstantString  (line1)
 obj0 = 0x100008220 class = __NSCFConstantString  (line1)
 obj0 = 0x1006b6d20 class = __NSCFString  (line1)
======== 元素是mutableString ========
 obj0 = 0x1006b9cb0 class = __NSCFString  (line1)
 obj0 = 0x1006ba0e0 class = __NSCFString  (line1)
 obj0 = 0x1006b70e0 class = __NSCFString  (line1)

```
根据输出，我们很明显得出如下结论

```
* 对Array归档并解档后，会生成新的Array对象

* Array对象内的不可变元素进行了深拷贝

* Array对象内的可变元素进行了深拷贝
```
由此，我们得出对如下总结
```
* 只深拷贝NSArray对象，我们用mutableCopy就可以

* 只深拷贝NSMutableArray对象，我们用Copy或mutableCopy都可以

* 深拷贝Array对象及内部元素，我们可以通过归档的方法解决

3. 重写copyWithZone mutableCopyWithZone的方式深拷贝自定义对象
```
我们写一个person类测试一下

```
//
//  Person.h
//  AlgorithmDemo
//
//
#import <Foundation/Foundation.h>
@interface Person : NSObject
@property (nonatomic, copy) NSString *nickname;
@end
```
测试代码如下

```
Person *person = [[Person alloc] init];
    person.nickname = @"码代码的小马";
    
    NSMutableArray *array1 = [NSMutableArray arrayWithObjects:person, nil];
    
    NSArray *array2 = [array1 copy];
    NSMutableArray *array3 = [array1 mutableCopy];
    
    NSLog(@"\n array1 = %p class = %@", array1, [array1 class]);
    NSLog(@"\n array2 = %p class = %@", array2, [array2 class]);
    NSLog(@"\n array3 = %p class = %@", array3, [array3 class]);
    
    NSLog(@"\n\n======== 数组内元素 ======== ");
    NSLog(@"\n array1[0] = %p class = %@", array1[0], [array1[0] class]);
    NSLog(@"\n array2[0] = %p class = %@", array2[0], [array2[0] class]);
    NSLog(@"\n array3[0] = %p class = %@", array3[0], [array3[0] class]);
```

```
浅拷贝：

1, 直接调用copy/mutableCopy方法

2, [[NSMutableArray alloc] initWithArray:studentsArray copyItems:NO]

3, [[NSMutableArray alloc] initWithArray:studentsArray]

深拷贝：
1, [[NSMutableArray alloc] initWithArray:studentsArray copyItems:YES],前提要自己实现每一层级的NSCopying协议

2,  [NSKeyedUnarchiver unarchiveObjectWithData:[NSKeyedArchiver archivedDataWithRootObject:oldArray]]
```

## iOS内存机制
内存空间
同其他系统一样，iOS 也使用了虚拟内存机制，前面介绍过，内存是采用分段和分页管理的，在 iOS 系统下，内存从高地址到低地址 分为：
```
* 栈区（stack）：用于存储程序临时创建的局部变量和函数参数等，在作用域执行完毕后会被系统回收，其中分配的地址由高到低分布。
* 堆区（heap）：用于存储程序运行中动态分配的内存段（通过调用 alloc 等函数），例如创建的新对象，默认由 ARC 进行管理，MRC 模式下需要手动进行内存释放，其中分配的地址由低到高分布。
* 全局静态区：由编译器分配，主要是存放全局变量 和 静态变量，程序结束后由系统释放；主要分为：
    * BBS区：存放未初始化的全局变量 和 静态变量。
    * 数据区：存放已初始化的全局变量 和 静态变量。
* 常量区：存放的是常量，如常量字符串，程序结束后由系统释放。
* 代码区：由于存放程序代码。
```
![Alt text](images/highAddress.png)

https://juejin.cn/post/6864492188404088846


### 内存分区：可以分为5个区
说到内存分区，内存即指的是RAM
```
* 栈区（stack）： 这个一般由编译器操作，或者说是系统管理，会存一些局部变量，函数跳转跳转时现场保护(寄存器值保存于恢复)，这些系统都会帮我们自动实现，无需我们干预。 所以大量的局部变量，深递归，函数循环调用都可能耗尽栈内存而造成程序崩溃
* 堆区（heap）： 一般由程序员管理，比如alloc申请内存，free释放内存。我们创建的对象也都放在这里
* 全局区（静态区 static）：全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域， 未初始化的全局变量和未初始化的静态变量在相邻的另一块区域。 - 程序结束后有系统释放。注意：在嵌入式系统中全局区又可分为未初始化全局区：.bss段和初始化全局区：data段。举例：int a;未初始化的。int a = 10;已初始化的。
* 常量区：常量字符串就是放在这里的，还有const常量
* 代码区：存放代码，app程序会拷贝到这里，程序不是在ROM里面存储吗？
```
￼
## 内存管理方案
### TaggedPointer
通常我们创建对象，对象存储在堆中，对象的指针存储在栈中，如果我们要找到这个对象，就需要先在栈中，找到指针地址，然后根据指针地址找到在堆中的对象。 这个过程比较繁琐，当存储的对象只是一个很小的东西，比如一个字符串，一个数字。去走这么一个繁琐的过程，无非是耗费性能的，所以苹果就搞出了TaggedPointer这么一个东西。
```
1. TaggedPointer是苹果为了解决32位CPU到64位CPU的转变带来的内存占用和效率问题，针对NSNumber、NSDate以及部分NSString的内存优化方案。
2. Tagged Pointer指针的值不再是地址了，而是真正的值。所以，实际上它不再是一个对象了，它只是一个披着对象皮的普通变量而已。所以，它的内存并不存储在堆中，也不需要malloc和free。
3. Tagged Pointer指针中包含了当前对象的地址、类型、具体数值。因此Tagged Pointer指针在内存读取上有着3倍的效率，创建时比普通需要malloc跟free的类型快106倍。
```


### __NSCFConstantString

字符串常量，是一种编译时常量，它的 retainCount 值很大，是 4294967295，在控制台打印出的数值则是 18446744073709551615==2^64-1，测试证明，即便对其进行 release 操作，retainCount 也不会产生任何变化。是创建之后便是放不掉的对象。相同内容的 __NSCFConstantString 对象的地址相同，也就是说常量字符串对象是一种单例。

这种对象一般通过字面值 @"..."、CFSTR("...") 或者 stringWithString: 方法（需要说明的是，这个方法在 iOS6 SDK 中已经被称为redundant，使用这个方法会产生一条编译器警告。这个方法等同于字面值创建的方法）产生。
这种对象存储在字符串常量区。

### __NSCFString

和 __NSCFConstantString 不同， __NSCFString 对象是在运行时创建的一种 NSString 子类，他并不是一种字符串常量。所以和其他的对象一样在被创建时获得了 1 的引用计数。
通过 NSString 的 stringWithFormat 等方法创建的 NSString 对象一般都是这种类型。
这种对象被存储在堆上。


### NSTaggedPointerString

理解这个类型，需要明白什么是标签指针，这是苹果在 64 位环境下对 NSString,NSNumber 等对象做的一些优化。简单来讲可以理解为把指针指向的内容直接放在了指针变量的内存地址中，因为在 64 位环境下指针变量的大小达到了 8 位足以容纳一些长度较小的内容。于是使用了标签指针这种方式来优化数据的存储方式。从他的引用计数可以看出，这货也是一个释放不掉的单例常量对象。在运行时根据实际情况创建。

对于 NSString 对象来讲，当非字面值常量的数字，英文字母字符串的长度小于等于 9 的时候会自动成为 NSTaggedPointerString 类型，如果有中文或其他特殊符号（可能是非 ASCII 字符）存在的话则会直接成为 ）__NSCFString 类型。
这种对象被直接存储在指针的内容中，可以当作一种伪对象。

0x01 引用计数为什么会是18446744073709551615？

这个值意味着无限的retainCount，这个对象是不能被释放的。所有的 NSCFConstantString对象的retainCount都是这个值，这就意味着 NSCFConstantString不会被释放，使用第一种方法创建的NSString，如果值一样，无论写多少遍，都是同一个对象。而且这种对象可以直接用 == 来比较。


