---
date: 2025-08-22 15:25:24
title: 在SwiftUI中运用策略模式与工厂模式实现灵活登录架构
tags:
  - 设计模式
  - SwiftUI
category: SwiftUI
---

在现代移动应用中，支持多种登录方式已成为标准需求。本文探讨如何通过策略模式和工厂模式在SwiftUI中构建一个灵活、可扩展的登录系统，以及这种设计带来的诸多好处。最近项目要求新增绿泡泡登录方式，需要在登录页面新增一个登录按钮，所以这篇文章就‌blingbling地从此刻诞生啦。

## 架构设计概述

我们的登录系统包含三个核心组件：

1. 目的地页面枚举：定义所有可能的登录后跳转页面
2. 视图工厂协议：负责创建具体的目标视图
3. 视图策略体系：管理不同登录方式的视图呈现逻辑

```swift
// 标准化目的地页面枚举
enum LoginViewDestination {
    case forgotPassword
    case registerMember(phone: String)
    case bindMemberCard(phone: String)
    case none
    // ... 其他目的地
}

// 视图工厂协议
protocol LoginViewFactoryProtocol {
    func makeDestinationView(for destination: LoginViewDestination) -> AnyView
}

// 视图策略协议
protocol LoginViewStrategy {
    var viewModel: LoginViewModel { get }
    func makeView() -> AnyView
}
```

## 策略模式的精妙运用

### 多登录方式的策略实现

我们为每种登录方式实现了具体的策略类：

```swift
// 一键登录策略
struct OneClickLoginViewStrategy: LoginViewStrategy {
    let viewModel: LoginViewModel
    func makeView() -> AnyView {
        AnyView(OneClickLoginView(vm: viewModel))
    }
    // ... 其他实现
}

// 账号登录策略
struct AccountLoginViewStrategy: LoginViewStrategy {
    let viewModel: LoginViewModel
    
    func makeView() -> AnyView {
        AnyView(AccountLoginView(vm: viewModel))
    }
}

// 微信登录策略
struct WechatLoginViewStrategy: LoginViewStrategy {
    let viewModel: LoginViewModel
    // 具体实现
    func makeView() -> AnyView {
        AnyView(WechatLoginView(vm: viewModel))
    }
}
```

### 策略选择机制

通过枚举类型优雅地管理策略创建：

```swift
enum LoginViewStrategyType {
    case oneClick(viewModel: LoginViewModel)
    case account(viewModel: LoginViewModel)
    case wechat(viewModel: LoginViewModel)
    
    var loginViewStrategy: LoginViewStrategy {
        switch self {
        case .oneClick(let viewModel):
            return OneClickLoginViewStrategy(viewModel: viewModel)
        case .account(let viewModel):
            return AccountLoginViewStrategy(viewModel: viewModel)
        case .wechat(let viewModel):
            return WechatLoginViewStrategy(viewModel: viewModel)
        }
    }
}
```

## 工厂模式的协同作用

### 统一视图创建接口

工厂模式提供了统一的视图创建接口，隐藏具体实现细节：

```swift
struct LoginViewFactory: LoginViewFactoryProtocol {
    func makeDestinationView(for destination: LoginViewDestination) -> AnyView {
        switch destination {
        case .forgotPassword:
            return AnyView(ForgotPasswordView())
        case .registerMember(let phone):
            return AnyView(RegisterMemberView(phone: phone))
        case .bindMemberCard(let phone):
            return AnyView(BindMemberCardView(phone: phone, isFromLogin: true))
        case .none:
            return AnyView(EmptyView())
        }
    }
}
```

## 设计优势与收益

### 1. 彻底解耦与单一职责

视图与业务逻辑分离：每个策略只关注特定登录方式的UI呈现，ViewModel处理业务逻辑，符合单一职责原则。

导航逻辑抽象化：工厂模式将目的地视图创建与导航逻辑分离，使主内容视图保持简洁：

```swift
// 主视图中简洁的导航链接
NavigationLink(
    destination: viewFactory.makeDestinationView(for: vm.transformedDestination),
    isActive: $vm.isLinkToActive
) {
    EmptyView()
}

// 扩展ViewModel提供标准化目的地页面转换
extension LoginViewModel {
    var transformedDestination: LoginViewDestination {
        switch linkToDestination {
        case .forgotPasswordView:
            return .forgotPassword
        case .registerMemberView:
            return .registerMember(phone: account)
        case .bindMemberCardView:
            return .bindMemberCard(phone: account)
        case .none:
            return .none
        }
    }
}
```

### 2. 高度可扩展性

#### 新增登录方式：只需实现新的策略类，无需修改现有代码，符合开闭原则。

添加新登录方式只需：

- 创建新的策略实现
- 在策略枚举中添加对应case
- 无需修改现有代码

```swift
// 未来添加指纹登录只需简单扩展
case fingerprint(viewModel: LoginViewModel)
// FaceID登录
case faceID(viewModel: LoginViewModel)
// 苹果登录
case apple(viewModel: LoginViewModel)
```

#### 动态切换：通过枚举类型轻松切换登录方式，支持运行时配置。

### 3. 可维护性提升

代码组织清晰：相关功能集中在一个策略中，便于理解和维护。

简化测试：每个策略可以独立测试，mock更容易实现。

**策略模式**：每个登录方式有独立的策略类，职责清晰，方便维护和测试。

**工厂模式**：统一的视图创建接口，使测试更简单，无需创建复杂的依赖关系。

### 4. 符合开闭原则

系统对扩展**开放**（可添加新策略），对修改**关闭**（现有代码不需要改动）。

### 5. SwiftUI中的天然优势

声明式UI配合策略模式：SwiftUI的声明式特性与策略模式天然契合，策略只需返回对应视图。

环境注入简便：SwiftUI的环境特性使得依赖注入更加简单自然：
```swift
struct LoginViewStrategyEnvironmentKey: EnvironmentKey {
    static let defaultValue: LoginViewStrategyType = .oneClick(viewModel: .init())
}

extension EnvironmentValues {
    var loginViewStrategy: LoginViewStrategyType {
        get { self[LoginViewStrategyEnvironmentKey.self] }
        set { self[LoginViewStrategyEnvironmentKey.self] = newValue }
    }
}

@Environment(\.dismiss) var dismiss
```

## 实际应用中的便利性

### 动态策略切换

根据条件动态选择登录策略：
```swift
private var currentLoginViewStrategy: LoginViewStrategy {
    if !vm.isUnsupportedOneClickLogin && !vm.isAccountLogin {
        return LoginViewStrategyType.oneClick(viewModel: vm).loginViewStrategy
    } else if !vm.isWechatLogin {
        return LoginViewStrategyType.account(viewModel: vm).loginViewStrategy
    } else {
        return LoginViewStrategyType.wechat(viewModel: vm).loginViewStrategy
    }
}
```

### 统一处理通用逻辑

基础策略扩展提供默认实现，减少重复代码：
```swift
extension LoginViewStrategy {
    func handleSpaceTap() {
        // 关闭键盘的通用处理
        UIApplication.shared.sendAction(
            #selector(UIResponder.resignFirstResponder), 
            to: nil, 
            from: nil, 
            for: nil
        )
    }
}
```

## 总结

**通过策略模式与工厂模式的结合，我们构建了一个高度灵活、可扩展的登录架构：**

1. 策略模式负责管理不同登录方式的视图呈现逻辑，使每种登录方式独立且可替换
2. 工厂模式负责统一创建目的地视图，简化导航逻辑
3. 组合使用实现了关注点分离，提高了代码的可维护性和可测试性

这种设计在SwiftUI中表现得尤为出色，充分利用了SwiftUI的声明式特性和响应式编程模型，实现了优雅而高效的架构解决方案。它不仅符合现代软件开发的设计原则，还为未来的功能扩展奠定了坚实基础。

这种模式组合可以广泛应用于需要多种呈现方式或行为的场景，如下单流程、支付方式选择、主题切换等，是SwiftUI应用架构中值得掌握的强大工具。