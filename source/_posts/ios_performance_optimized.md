---
title: iOS性能优化
categories: 性能优化
tags: 性能优化
---

iOS性能优化是提升用户体验的关键环节。性能优化的核心思路是"监控 -> 定位 -> 修复 -> 预防"。本文将从原理到实践，全面介绍iOS性能优化的知识。

# 性能优化原理

iOS系统的图形渲染是由CPU和GPU协作完成的，理解它们的工作原理是性能优化的基础。

## CPU与GPU的协作

- **CPU**：负责计算视图frame、图片解码，需要绘制纹理图片通过数据总线交给GPU
- **GPU**：负责纹理混合、顶点变换与计算、像素点的填充计算，渲染到帧缓冲区
- **时钟信号**：垂直同步信号V-Sync和水平同步信号H-Sync
- **双缓冲机制**：显示系统通常会引入两个帧缓冲区

## CPU工作流程

图片加载的工作流程如下：

1. 使用`+imageWithContentsOfFile:`方法从磁盘加载图片（此时图片未解压缩）
2. 将生成的`UIImage`赋值给`UIImageView`
3. 隐式的`CATransaction`捕获到`UIImageView`图层树的变化
4. 在主线程下一个`runloop`到来时，`Core Animation`提交隐式transaction
5. 这个过程可能对图片进行`copy`操作，涉及以下步骤：
   - 分配内存缓冲区用于文件IO和解压缩
   - 将文件数据从磁盘读到内存
   - 解压压缩的图片数据为位图形式（耗时操作）
6. `CALayer`使用未压缩的位图数据渲染UIImageView

CPU计算好图片的Frame，解压后交给GPU做渲染。

## GPU图形渲染流程

GPU图形渲染采用OpenGL ES pipeline，流程如下：

1. **获取图片坐标**：GPU获取纹理坐标
2. **顶点着色器**：进行顶点计算和变换
3. **光栅化**：获取图片对应屏幕上的像素点
4. **片元着色器**：计算每个像素点的最终颜色值
5. **帧缓冲区**：渲染到屏幕上

## iOS渲染架构

iOS渲染分为五个阶段：

### 第一阶段：Event（处理用户事件）

处理用户点击、滑动等交互事件。

### 第二阶段：Commit（提交阶段）

这是性能优化的重点阶段，包含四个子阶段：

- **Layout（布局阶段）**：计算视图的frame和布局
- **Display（显示阶段）**：绘制视图内容
- **Prepare（准备阶段）**：准备渲染数据
- **Commit（提交阶段）**：提交渲染任务

### 第三、四阶段：Render（渲染阶段）

- **Render Prepare**：准备渲染命令
- **Render Execute**：执行渲染命令

### 第五阶段：Display（显示阶段）

最终将内容显示到屏幕上。

## 内存管理

### 物理内存与虚拟内存

- **物理内存**：实际的硬件内存
- **虚拟内存**：操作系统提供的逻辑内存地址空间

### Mach-O文件

Mach-O是iOS可执行文件的格式，包含以下几种类型：

- **MH_OBJECT**：中间对象文件
- **MH_EXECUTE**：可执行二进制
- **MH_DYLIB**：动态共享库
- **MH_DSYM**：符号文件和调试信息

### iOS内存布局

![内核空间](<images/kernSpace.png>)

### 内存问题

- **OOM（内存溢出）**：使用matrix OOMDetector检测
- **内存泄漏**：使用MLeaksFinder、PLeakSniffer检测
- **循环引用**：使用FBRetainCycleDetector检测
- **僵尸对象**：因野指针导致的崩溃
- **野指针**：指针指向已删除对象

### ANR应用无响应

主线程超过系统规定时间无响应会被Watchdog杀掉，异常编码为0x8badf00d。

# 编译优化

## 编译优化策略

### 模块化组件化

将庞大的单体工程拆分成多个独立模块：

- **增量编译极快**：修改模块内部代码只需重新编译该模块
- **二进制化**：稳定模块提前编译成.framework或.a
- **并行编译**：多个独立模块同时编译

### 头文件清理

**问题根源**：C++/ObjC的#include/#import是文本替换，造成巨大头文件依赖树。

**优化思路**：

1. **前向声明**：在头文件中使用`@class`或`@protocol`替代`#import`
2. **移除冗余引用**：使用Xcode的"Show Includes"分析头文件使用情况
3. **头文件迁移**：只在实现文件.m中使用的头文件，从.h移到.m
4. **预编译头文件(PCH)**：谨慎使用全局必须且几乎不修改的系统头文件

### 启用Clang Module

- **是什么**：将传统文本式头文件包含替换为模块化导入`@import`
- **效果**：
  - 编译更快：同一框架只解析一次
  - 避免宏污染：模块是独立的
  - 语义更精确：更好的代码补全和跳转

### 编译分析工具

- **Xcode Build With Timing Summary**：分析每个阶段耗时
- **XCLogParser**：解析.xcactivitylog日志，生成直观报告

### ccache

使用ccache-clang加速增量编译。

# 启动优化

App启动分为冷启动和热启动：

- **冷启动**：App启动前，内核没有为它分配进程
- **热启动**：App从后台进入

## 冷启动流程

冷启动分为三个阶段：

### 1. main()函数之前

- 内核加载App到内存
- dyld动态链接器分析Mach-O文件
- ASLR机制进行Rebasing和Binding
- 加载runtime组件
- 向需要初始化的object发送消息

### 2. main()函数之后

- 执行AppDelegate生命周期方法
- 初始化自定义服务
- 渲染首屏

### 3. 首屏渲染结束

至第一个界面的`viewDidAppear:`执行完成

## Mach-O文件识别

通过文件第一个字节（魔数）判断是否为Mach-O文件：

- `0xfeedface` → MH_MAGIC
- `0xfeedfact` → MH_MAGIC_64
- `NXSwapInt(MH_MAGIC)` → MH_GIGAM
- `NXSwapInt(MH_MAGIC_64)` → MH_GIGAM_64

## 启动优化建议

- 尽量减少嵌入的dylibs数量
- 推荐使用系统提供的库
- 尽量减少类和方法的数量
- 尽量减少初始化函数
- 尽量使用Swift（无初始化器，代码更精简）

## 二进制插桩重排机制

WWDC 2017提出的启动优化方案，优化内存布局减少页面 faults。

# 包体积优化

- 资源文件优化
- 代码优化
- 编译选项优化

# 网络优化

## 序列化格式

- **Protocol Buffers (PB)**：体积小，解析快
- **JSON**：通用性强，但体积较大

## 网络监控

使用Fishhook Hook网络底层库CFNetwork进行监控。

## 关键指标

- DNS时间
- SSL时间
- 首包时间
- 响应时间

## 协议选择

- HTTP/HTTPS
- TCP/UDP
- QUIC（基于UDP的新协议）

# 电量优化

- 定位服务优化
- 后台任务优化
- 网络请求优化

# I/O操作优化

使用Frida动态二进制插桩技术，在程序运行时插入自定义代码获取I/O耗时和数据大小。

# 性能优化实践

## FPS优化

### 监控工具

- **Instruments - Time Profiler**：检查占用CPU较高的方法
- **Instruments - Core Animation**：检查离屏渲染、像素对齐、图片格式
- **Instruments - System Trace**：分析线程状态、系统调用、锁竞争

### Core Animation检测选项

- **Color Offscreen-Rendered Yellow**：检测离屏渲染
- **Color Misaligned Images**：检测图片缩放和像素对齐
- **Color Copied Images**：检测GPU不支持的图片格式

### 卡顿定位

#### Time Profiler使用方法

1. 选择Time Profiler工具
2. 启动真机调试，在页面反复滑动
3. 查看CPU Weight较高的方法
4. 勾选Call Tree中的Invert Call Tree和Hide System Libraries

#### Animated Hitches

- **Commit Hitches**：提交阶段卡顿
- **Render Hitches**：渲染阶段卡顿

### 线上监控方案

通过向主线程RunLoop添加CFRunLoopObserver，监听kCFRunLoopBeforeSources和kCFRunLoopAfterWaiting状态，计算耗时，超过阈值则捕获堆栈。

## 卡顿优化

### CPU相关优化

- **主线程减负**：将耗时操作异步派发到全局队列
```swift
// 错误示范
let data = try? Data(contentsOf: bigFileURL) // 阻塞主线程！

// 正确示范
DispatchQueue.global(qos: .userInitiated).async {
    let data = try? Data(contentsOf: bigFileURL)
    DispatchQueue.main.async {
        self.updateUI(with: data)
    }
}
```

- **算法优化**：优化for循环、递归等计算密集型代码
- **视图布局优化**：避免在layoutSubviews或drawRect:中做复杂计算

### GPU相关优化

- **减轻视图复杂度**：
  - 减少图层数量，避免不必要的视图嵌套
  - 避免离屏渲染（cornerRadius + masksToBounds、shadow等）
  - 减少图层混合，确保opaque属性正确设置

- **图片优化**：
  - 尺寸匹配：图片尺寸不超过UIImageView显示尺寸
  - 格式选择：照片用JPEG，图形用PNG
  - 避免缩放

### 优化方案总结

| 优化点 | 方案 |
|--------|------|
| 离屏渲染 | CAShapeLayer绘制圆角、预渲染图片、shadowPath |
| 圆角 | GraphicsContext生成带圆角图片 |
| 像素对齐 | 控件位置和大小为整数 |
| 图片格式 | 使用32bit/通道的图片 |
| 后台操作 | 图片下载、解码、圆角处理放入后台 |
| 缓存 | 缓存图片和计算结果 |

## UITableView优化

1. **size缓存**：缓存cell高度和控件宽高
2. **图片优化**：遵循前述7条图片优化规则
3. **异步处理**：数据读取放入异步线程
4. **按需加载**：滑动时按需加载
5. **异步绘制**：复杂界面可考虑异步绘制

## 数据库优化

1. 频繁读写改为缓存
2. 数据库操作放入子线程
3. 减少不必要的数据库操作

# 编译时间优化

## 编译时间计算

### 方案一

```bash
defaults write com.apple.dt.Xcode ShowBuildOperationDuration -bool YES
```

编译成功后，时间显示在导航栏。

### 方案二

```bash
gem install xcpretty
npm install -g gnomon

xcodebuild build -workspace xxx.xcworkspace -scheme xxx ONLY_ACTIVE_ARCH=YES -configuration Debug | xcpretty | gnomon | sort -nr -k1 > ~/Desktop/xxx.txt
```

## 具体优化点

### 1. 头文件优化

一个头文件包含多个细分头文件会导致编译时间剧增。

**优化方案**：使用更细粒度的文件引入，按需引用具体的头文件。

**效果**：某项目优化后编译时间从15.65分钟缩短到4.65分钟，加快70%。

### 2. PCH文件优化

PCH中的文件会被所有文件依赖，修改后会导致全量编译。

### 3. Debug模式优化

关闭dSYM选项可节省约30秒编译时间。

### 4. 二进制化

将稳定模块提前编译成二进制，直接参与链接，跳过编译步骤。

# 总结

iOS性能优化是一个系统性的工程，需要从多个维度进行：

1. **理解原理**：深入理解CPU、GPU、内存等工作原理
2. **监控定位**：使用工具发现性能瓶颈
3. **针对性优化**：根据问题类型采取相应策略
4. **建立长效机制**：防止性能劣化

核心原则：**把一切可以在异步线程执行的操作从主线程移除**。
