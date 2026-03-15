---
date: 2025-08-19 15:02:11
title: iOS 中使用 ActivityKit 实现 实时活动 通知功能
categories: SwiftUI
tags: SwiftUI
---

LiveActivity 是 iOS 16.1 引入的一项重要功能，它允许应用在锁屏界面或灵动岛（Dynamic Island）区域实时展示动态信息，例如商品订单进度、体育比赛比分或12306火车票状态等。相比传统推送，Live Activity提供了更优的用户体验和信息触达能力。
实时活动可以出现在用户锁屏界面，并可实时展示用户关心的一些核心信息。由于使用远程推送通道更新实时活动不需要主 app 保持开启，并且相比小组件需要用户手动添加到桌面这个门槛，实时活动功能是默认开启的，所以这一机制保证了信息的触达概率会远高于小组件。

实时活动是一种更高级的推送形态，对比传统的推送，实时活动显得灵活许多。传统推动在用户接收并读取到内容的瞬间信息就失效了，如果想要为用户提供持续更新的信息需要依赖一条接一条的推送才可以实现，这无论从成本还是用户体验上，都是难以接受的。而实时活动则会在持续期间，无干扰的保持着信息的更新，并且又会在合适的时机自行消失，因此用户体验极佳。

## 核心优势

### 更高的信息触达率

- 默认开启功能，无需用户手动添加
- 信息持续展示，不会像传统推送那样瞬间失效
- 支持实时更新，无需频繁发送多条推送

### 灵活的展示位置

- 锁屏界面底部（所有支持 iOS 16.1 的 iPhone）
- 灵动岛区域（仅 iPhone 14 Pro 及以上机型）

### 高效的数据更新机制

- 通过 ActivityKit 本地更新或远程推送更新
- 每次数据更新限制 ≤4KB
- 不支持视图内直接发起网络请求

### ‌合理的生命周期限管理
- 8 小时内可刷新数据
- 超过 12 小时系统自动终止

## 实现详解

Live Activity 的生命周期由 ActivityKit 管理，其中，数据部分的模型类为 ActivityAttributes，自定义数据模型需要继承自 ActivityAttributes，静态数据变量直接生命在结构体内，动态数据变量需要声明在 ActivityAttributes 的 ContentState 中，这部分变量在接收到推送更新数据时，会自动根据 json 数据的 key 值进行解析并更新，而静态数据变量则不会变化.

### 数据模型设计

Live Activity 的数据模型需要继承自 ActivityAttributes，包含静态数据和动态数据两部分：

```swift
struct LockScreenLiveActivityAttrbutes: ActivityAttributes {
    public typealias ContentState = State
    
    // 静态数据（不会变化）
    var orderId: String
    var totalAmount: String
    
    // 动态数据（通过推送更新）
    public struct State: Codable, Hashable {
        var title: String
        var subTitle: String
        var progress: Double
    }
}
```

#### 静态数据

```swift
struct LockScreenLiveActivityAttrbutes: ActivityAttributes {
    // 静态数据
    var orderId: String
    var totalAmount: String
}
```

#### 动态数据

```swift
struct LockScreenLiveActivityAttrbutes: ActivityAttributes {
    public typealias ContentState = State
    // 动态数据,接收到推送时会更新的数据
    public struct State: Codable, Hashable {
        var title: String = "您的订单已经拣货完成"
        var subTitle: String = "商家正在备货，骑手正在前往"
        var progress: Double // 动态更新的数据
    }
}
```

## 启动 Live Activity

```swift
public func startActivity() {
    let data = LiveActivityData(title: "订单进度")
    let activity = try? Activity<LiveActivityData>.request(attributes: data, content: .init(progress: 0, status: "待付款"))

    let activity = try Activity.request(
                attributes: attributes,
                content: .init(state: initialContentState, staleDate: nil),
                pushType: .token) // 使用 Activity.request 方法时注意传入 pushType 参数为.token，指定实时活动更新方式为 “基于 token” 的推送更新，这个 token 就标识了是哪部手机的哪个实时活动来接受推送通知。拿到 token 后，前端要把它发送给后端服务器，由后端处理发给苹果进行推送

    Task {
        // 获取实时活动的唯一推送Token  Activity.request 方法后，token 不会立刻生成，而是会异步生成，过一段时间才能取到，所以要建一个 Task 使用 for await 方式来获取
        for await pushToken in activity.pushTokenUpdates {
            let pushTokenString = pushToken.map { String(format: "%02x", $0) }.joined()
            // 需要将 PushToken 同步给服务器，这样后续如果有新的信息需要下发，服务器通过该 PushToken 来进行推送操作即可。
//          Logger().log("New push token: \(pushTokenString)")
            print("New push token: \(pushTokenString)")
                
            try await self.sendPushToken(pushTokenString: pushTokenString)
        }
    }
}

```

## 更新 Live Activity

aps 内的数据就是推送通知内容，timestamp 是时间戳；event 是通知类型，分为 update 和 end 两种；content-state 就是上文中定义的 ActivityAttributes 动态数据属性部分，这里的 key 要与属性名对应，接到通知后就可以自动解析并更新数据
 
 所有的属性，在 content-state 里都要有对应的 key-value，就算是空的也要写上，不然会解析失败
 
 ```
 "aps": {
     "timestamp":'$(date +%s)',
     "event":"update",
     "content-state":{
         "logo": "https://img.duoziwang.com/2016/12/17/16485364877.jpg",
         "title": "订单已经开始配送",
         "subTitle": "快递员正在加急配送",
         "progress": 0.6
     }
 }

 ```

```swift
public func updateActivity() {
    let newData = LiveActivityData(title: "订单进度")
    let newContent = LiveActivityData.ContentState(progress: 50, status: "已付款")
    try? activity?.update(using: newContent)
}
```

## 终止 Live Activity

主 APP 调用 end(dismissalPolicy:) 方法关闭指定的实时活动实例，这里可以通过关闭策略参数来控制是立即移除还是指定时间后移除，如果选择默认选项，系统会在 4 小时后进行实时活动的移除。

```swift
public func endActivity() {
    try? activity?.end(dismissalPolicy: .immediate)
}
```

通过 Push 下发 end 事件，并可以在消息体中通过 dismissal-date 参数来指定实时活动的移除时间点。PUSH 消息体中的内容实例：

```
 {
    "aps": {
        "timestamp":'$(date +%s)000',
        "event": "end",
        "content-state": {"content":"$JSON_STRING"},
        "dismissal-date": '$endDate'
    }
 }
```

## 实时活动推送配置

 如果实时活动确定要接入推送能力，以下是需要我们做的：

 1. 认证方式：确保 APP 的推送证书是基于 token 的认证方式 (Token-Based) ，如果现有的认证方式是基于证书的，则需要推送业务来改造成 Token-Based 的。

 2. Token获取：客户端获取实时活动的 PushToken。需要注意的是，推送时使用的 Token 并非 App 启动时通过 UIApplication 注册时所获得的 Device Token，而是实时活动启动之后，通过监听实时活动的实例回调（pushTokenUpdates）来获取到的。客户端获取到 PushToken 之后，需要将 PushToken 同步给服务器，这样后续如果有新的信息需要下发，服务器通过该 PushToken 来进行推送操作即可。

 3. 服务器集成：服务器端需要根据实时活动的 PushToken 来进行推送操作。

## 如何进行实时活动代码的断点调试

 开发中，如果遇到需要断点调试实时活动来进行问题定位的情况，可以按照如下流程进行：

 1. 模拟器或者真机启动主 APP，在 XCode 中的 Debug 菜单中找到相应实时活动的 Extention Target 的进程进行 Attach
 2. 回到主 APP，触发启动或者更新实时活动操作即可触发断点。

## 监测实时活动的状态

```swift
class LockScreenLiveActivityMonitor {
    private var taskHandle: Task<Void, Never>?
    private var monitoredActivities = Set<String>()
    
    func startMonitoring() {
        taskHandle = Task {
            if #available(iOS 17.2, *) {
                // 监听所有活动更新
                for await activity in Activity<LockScreenLiveActivityAttrbutes>.activityUpdates {
                    print("检测到活动：\(activity.id)")
                    
                    // 避免重复监听同一个activity
                    guard !monitoredActivities.contains(activity.id) else { continue }
                    monitoredActivities.insert(activity.id)
                    
                    // 监听推送令牌变化
                    Task {
                        var oldPushToken = ""
                        for await tokenData in activity.pushTokenUpdates {
                            let token = tokenData.map { String(format: "%02x", $0) }.joined()
                            if oldPushToken != token {
                                oldPushToken = token
                                // 上报推送令牌到友盟推送或服务器端
                                // 通过嵌套异步任务监听活动实例的 pushTokenUpdates 和 activityStateUpdates，将活动的令牌和ID上报给阿里云服务器。
                                print("token：\(token) - 活动ID：\(activity.id)")
                                // 发送pushToken至友盟服务器
                            }
                        }
                    }
                    
                    // 监听活动状态变化
                    Task {
                        for await state in activity.activityStateUpdates {
                            // 同步状态到服务器端
                            print("state: \(state) - 活动ID：\(activity.id)")
                            
                            // 如果活动结束，从监听列表中移除
                            if state == .ended {
                                monitoredActivities.remove(activity.id)
                            }
                        }
                    }
                }
            }
        }
    }
    
    func stopMonitoring() {
        taskHandle?.cancel()
        monitoredActivities.removeAll()
    }
}
```

## 总结

Live Activity 为 iOS 应用提供了全新的信息展示方式，特别适合需要实时更新状态的场景。通过合理的生命周期管理和推送集成，可以显著提升用户体验和信息触达效果。在实际开发中，需要注意数据模型设计、推送配置和状态监控等关键环节。