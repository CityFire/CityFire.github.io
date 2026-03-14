# 博客文章详细说明

本目录包含个人技术博客的所有文章，涵盖移动开发、架构设计、编程语言、AI技术、系统运维等多个技术领域。

## 📚 文章分类索引

### 一、iOS 开发

#### 1.1 SwiftUI 相关
- **[SwiftUI 的深度思考：从设计哲学到工程实践](SwiftUI.md)**
  - 声明式与响应式编程范式
  - SwiftUI 与 UIKit 的思维转变
  - 响应式系统实现原理
  - 状态管理最佳实践

- **[SwiftUIToUIKit](SwiftUIToUIKit.md)**
  - SwiftUI 与 UIKit 的互操作
  - UIViewControllerRepresentable 使用
  - UIViewRepresentable 实践

- **[Swift_Concurrency](Swift_Concurrency.md)**
  - async/await 异步编程
  - Actor 并发模型
  - Task 和 TaskGroup
  - 并发安全最佳实践

#### 1.2 UIKit 相关
- **[UIKit_MainThread](UIKit_MainThread.md)**
  - UIKit 主线程机制
  - UI 更新线程安全
  - 主线程检查原理

#### 1.3 iOS 性能优化
- **[ios_performance_optimized](ios_performance_optimized.md)**
  - iOS 性能优化策略
  - 启动时间优化
  - 内存优化技巧
  - UI 流畅度优化

- **[memoryPerfomance_iOS](memoryPerfomance_iOS.md)**
  - 内存性能分析
  - 内存泄漏检测
  - 内存管理最佳实践

#### 1.4 iOS 多线程
- **[multiThread_programing](multiThread_programing.md)**
  - iOS 多线程编程
  - GCD 使用详解
  - OperationQueue 实践

- **[nsoperation](nsoperation.md)**
  - NSOperation 深入理解
  - 自定义 Operation
  - 依赖管理和优先级

#### 1.5 iOS 其他技术
- **[CoreBluetooth](CoreBluetooth.md)**
  - 蓝牙开发指南
  - CoreBluetooth 框架使用
  - 蓝牙设备通信

- **[liveActivity](liveActivity.md)**
  - iOS 16 Live Activity
  - 实时活动开发
  - 锁屏小组件

- **[nscfConstantString](nscfConstantString.md)**
  - NSString 内部实现
  - CFString 桥接机制
  - 字符串优化

- **[multiPathReuse](multiPathReuse.md)**
  - UITableViewCell 复用机制
  - 多路径复用优化
  - 列表性能提升

---

### 二、架构设计

#### 2.1 系统架构
- **[Architecture](Architecture.md)**
  - 架构风格分类
  - 单体架构 vs 分布式架构
  - 架构演进历程

- **[SystemArchitecture](SystemArchitecture.md)**
  - 系统架构设计原则
  - 分层架构设计
  - 微服务架构模式

- **[PresentLayerArchitectureDesign](PresentLayerArchitectureDesign.md)**
  - 表现层架构设计
  - MVC/MVP/MVVM 模式
  - 架构模式选择

- **[architectureForMobileDevelop](architectureForMobileDevelop.md)**
  - 移动应用架构设计
  - 客户端架构演进
  - 组件化架构

#### 2.2 微服务架构
- **[microService](microService.md)**
  - 微服务架构设计
  - 服务拆分原则
  - 微服务通信机制

- **[AtomicService](AtomicService.md)**
  - 原子服务设计
  - 服务粒度划分
  - 服务治理

#### 2.3 设计模式
- **[DesignPattern](DesignPattern.md)**
  - 常用设计模式
  - 设计模式应用场景
  - 设计原则

- **[strategyFactoryModern](strategyFactoryModern.md)**
  - 策略工厂模式
  - 现代设计模式实践
  - 设计模式组合应用

- **[structuralizationDesign](structuralizationDesign.md)**
  - 结构化设计
  - 模块化设计原则
  - 代码组织结构

---

### 三、编程语言

#### 3.1 Swift 语言
- **[Swift_new](Swift_new.md)**
  - Swift 新特性
  - Swift 版本演进
  - 语言改进点

#### 3.2 C++ 语言
- **[cplusplus_newfeature](cplusplus_newfeature.md)**
  - C++ 新特性
  - C++11/14/17/20 特性
  - 现代C++编程

- **[const_cpp](const_cpp.md)**
  - C++ const 关键字
  - const 正确性
  - const 最佳实践

- **[cpp_performance](cpp_performance.md)**
  - C++ 性能优化
  - 零开销抽象
  - 性能分析技巧

- **[smartPointer](smartPointer.md)**
  - 智能指针详解
  - shared_ptr/unique_ptr/weak_ptr
  - 内存管理最佳实践

- **[placement](placement.md)**
  - Placement New
  - 内存分配策略
  - 自定义内存管理

#### 3.3 仓颉语言
- **[cangjie](cangjie.md)**
  - 仓颉语言介绍
  - 语言特性
  - 编程范式

- **[cangjieInstallForMac](cangjieInstallForMac.md)**
  - Mac 环境配置
  - 开发环境搭建
  - 工具链安装

- **[macroForCangjie](macroForCangjie.md)**
  - 仓颉宏编程
  - 元编程技术
  - 宏的应用场景

---

### 四、AI 与机器学习

#### 4.1 AI 实践
- **[AI_Practice](AI_Practice.md)**
  - AI 分析股价趋势
  - 数据思维模型
  - 预测模型构建

- **[AICodingTool](AICodingTool.md)**
  - AI 编程工具
  - AI 辅助开发
  - 工具使用技巧

- **[ai_programming](ai_programming.md)**
  - AI 编程实践
  - 机器学习应用
  - AI 开发流程

#### 4.2 AI 大模型
- **[《AI大模型：从入门到精通》](《AI大模型：从入门到精通》.md)**
  - 大模型基础知识
  - 模型训练与部署
  - 应用场景分析

- **[《图解大模型：从零掌握深度学习的奥秘》](《图解大模型：从零掌握深度学习的奥秘》.md)**
  - 深度学习原理
  - 模型架构图解
  - 学习路径指导

- **[《揭开人工智能的面纱》](《揭开人工智能的面纱》.md)**
  - AI 基础概念
  - 技术发展历程
  - 未来趋势展望

#### 4.3 AI Agent
- **[deepseekAIAgent](deepseekAIAgent.md)**
  - DeepSeek AI Agent
  - Agent 架构设计
  - 智能体应用

- **[manusAIAgent](manusAIAgent.md)**
  - Manus AI Agent
  - 多智能体系统
  - Agent 协作机制

#### 4.4 深度学习框架
- **[tensorflow](tensorflow.md)**
  - TensorFlow 入门
  - 模型构建
  - 训练与部署

---

### 五、跨平台开发

#### 5.1 Flutter
- **[flutter](flutter.md)**
  - Flutter 开发指南
  - Widget 体系
  - 状态管理

- **[Flutter_interview](Flutter_interview.md)**
  - Flutter 面试题
  - 核心概念解析
  - 最佳实践

#### 5.2 HarmonyOS
- **[harmonyos](harmonyos.md)**
  - 鸿蒙系统开发
  - ArkUI 框架
  - 应用开发指南

- **[HarmonyOSNEXT_Architecture](HarmonyOSNEXT_Architecture.md)**
  - 鸿蒙 NEXT 架构
  - 系统架构设计
  - 应用模型

- **[HarmonyOS_StateManage](HarmonyOS_StateManage.md)**
  - 鸿蒙状态管理
  - 状态装饰器
  - 数据绑定

#### 5.3 Qt
- **[Qt](Qt.md)**
  - Qt 开发入门
  - 信号槽机制
  - 跨平台开发

---

### 六、后端技术

#### 6.1 Java 框架
- **[spring_springMVC](spring_springMVC.md)**
  - Spring 框架
  - Spring MVC
  - 依赖注入

#### 6.2 分布式系统
- **[CAP](CAP.md)**
  - CAP 定理
  - 分布式系统权衡
  - 一致性保证

- **[distributedLock](distributedLock.md)**
  - 分布式锁实现
  - Redis 分布式锁
  - ZooKeeper 锁

---

### 七、网络与协议

- **[ComputerInternet](ComputerInternet.md)**
  - 计算机网络基础
  - 网络协议栈
  - 网络通信原理

- **[tcp_packet](tcp_packet.md)**
  - TCP 数据包分析
  - TCP 协议详解
  - 网络抓包实践

- **[https_usage](https_usage.md)**
  - HTTPS 原理
  - SSL/TLS 加密
  - 证书配置

- **[h264video](h264video.md)**
  - H.264 视频编码
  - 视频压缩原理
  - 编码参数优化

---

### 八、数据库与存储

- **[zerocopy](zerocopy.md)**
  - 零拷贝技术
  - 数据传输优化
  - 性能提升

---

### 九、系统运维

#### 9.1 容器化与编排
- **[k8s](k8s.md)**
  - Kubernetes 入门
  - 集群管理
  - 容器编排

#### 9.2 CI/CD
- **[jenkins_cicd](jenkins_cicd.md)**
  - Jenkins 流水线
  - 持续集成部署
  - 自动化构建

---

### 十、并发编程

- **[SpinLock](SpinLock.md)**
  - 自旋锁原理
  - 自旋锁实现
  - 性能分析

- **[anyLock](anyLock.md)**
  - 各种锁机制
  - 锁的选择策略
  - 并发控制

- **[lock_introduce](lock_introduce.md)**
  - 锁的基础知识
  - 互斥锁与读写锁
  - 死锁预防

- **[volatile](volatile.md)**
  - Volatile 关键字
  - 内存可见性
  - 指令重排序

---

### 十一、编译原理

- **[Compilers](Compilers.md)**
  - 编译器原理
  - 词法分析
  - 语法分析

- **[cmake](cmake.md)**
  - CMake 构建系统
  - 跨平台构建
  - 项目配置

---

### 十二、数据结构与算法

- **[DataStructures_Algorithms](DataStructures_Algorithms.md)**
  - 数据结构基础
  - 算法复杂度
  - 常用算法

---

### 十三、机器人技术

- **[ros](ros.md)**
  - ROS 机器人系统
  - 节点通信
  - 机器人开发

- **[rosRobot](rosRobot.md)**
  - ROS 机器人实践
  - 传感器集成
  - 运动控制

---

### 十四、游戏开发

- **[QWGameSdk](QWGameSdk.md)**
  - 游戏SDK集成
  - 游戏开发框架
  - SDK 接入指南

---

### 十五、工具与工程化

- **[inject](inject.md)**
  - 依赖注入工具
  - 代码注入技术
  - 热重载

- **[technology_select](technology_select.md)**
  - 技术选型
  - 技术决策
  - 架构评估

- **[scrachData](scrachData.md)**
  - 数据抓取
  - 爬虫技术
  - 数据处理

---

### 十六、软件工程

- **[SoftwareEngineer](SoftwareEngineer.md)**
  - 软件工程实践
  - 开发流程
  - 项目管理

- **[FirstNight](FirstNight.md)**
  - 开发经验分享
  - 技术成长
  - 职业发展

---

### 十七、Hexo 博客

- **[Hexo_migrate_newMacSystem](Hexo_migrate_newMacSystem.md)**
  - Hexo 博客迁移
  - 环境配置
  - 博客部署

---

### 十八、开源项目

- **[OpenClaw_Guide](OpenClaw_Guide.md)**
  - OpenClaw 项目指南
  - 开源项目贡献
  - 项目架构

---

### 十九、系列文章

#### Effective 系列（item1-42）
这是一系列关于编程最佳实践的文章，涵盖：
- **[item1.md ~ item42.md](item1.md)**
  - 编程技巧
  - 代码质量
  - 最佳实践

---

## 📊 文章统计

| 分类 | 文章数量 | 主要内容 |
|------|---------|---------|
| iOS 开发 | 13篇 | SwiftUI、UIKit、性能优化、多线程 |
| 架构设计 | 9篇 | 系统架构、微服务、设计模式 |
| 编程语言 | 10篇 | Swift、C++、仓颉 |
| AI 与机器学习 | 9篇 | AI实践、大模型、Agent |
| 跨平台开发 | 6篇 | Flutter、HarmonyOS、Qt |
| 后端技术 | 3篇 | Spring、分布式系统 |
| 网络与协议 | 4篇 | TCP、HTTPS、视频编码 |
| 并发编程 | 4篇 | 锁机制、并发控制 |
| 其他 | 15篇 | 编译原理、机器人、工具等 |
| **总计** | **73篇** | - |

## 🎯 阅读建议

### 初学者路径
1. **编程基础** → [DataStructures_Algorithms](DataStructures_Algorithms.md)
2. **iOS 入门** → [Swift_new](Swift_new.md) → [SwiftUI](SwiftUI.md)
3. **架构理解** → [Architecture](Architecture.md)
4. **实践提升** → [DesignPattern](DesignPattern.md)

### 架构师路径
1. **架构基础** → [Architecture](Architecture.md) → [SystemArchitecture](SystemArchitecture.md)
2. **微服务** → [microService](microService.md) → [AtomicService](AtomicService.md)
3. **分布式** → [CAP](CAP.md) → [distributedLock](distributedLock.md)
4. **性能优化** → [ios_performance_optimized](ios_performance_optimized.md)

### AI 开发者路径
1. **AI 基础** → [《揭开人工智能的面纱》](《揭开人工智能的面纱》.md)
2. **深度学习** → [tensorflow](tensorflow.md) → [《图解大模型》](《图解大模型：从零掌握深度学习的奥秘》.md)
3. **实践应用** → [AI_Practice](AI_Practice.md) → [AICodingTool](AICodingTool.md)
4. **Agent 开发** → [deepseekAIAgent](deepseekAIAgent.md)

### 跨平台开发者路径
1. **Flutter** → [flutter](flutter.md) → [Flutter_interview](Flutter_interview.md)
2. **HarmonyOS** → [harmonyos](harmonyos.md) → [HarmonyOS_StateManage](HarmonyOS_StateManage.md)
3. **Qt** → [Qt](Qt.md)

## 📝 写作规范

所有博客文章遵循以下规范：

1. **文件命名**：使用小写字母和下划线，如 `swift_new.md`
2. **Front Matter**：包含 `title`、`tags`、`categories`
3. **内容结构**：
   - 清晰的标题层级（H1-H4）
   - 代码示例使用语法高亮
   - 图片使用相对路径
   - 适当使用表格和列表

## 🔗 相关链接

- **博客地址**：[CityFire.github.io](https://cityfire.github.io)
- **GitHub**：[CityFire/CityFire.github.io](https://github.com/CityFire/CityFire.github.io)
- **Hexo 官网**：[hexo.io](https://hexo.io)

## 📮 联系方式

如有问题或建议，欢迎：
- 在 GitHub 上提交 Issue
- 发送邮件反馈
- 在博客文章下留言

---

**最后更新时间**：2026年3月

**维护者**：CityFire
