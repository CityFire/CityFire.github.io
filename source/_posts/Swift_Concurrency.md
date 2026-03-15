---
date: 2025-07-31 14:59:34
title: Swift Concurrency编程
categories: [Swift, 并发编程]
tags: [Swift]
---

Swift Concurrency 是苹果从 Swift 5.5 开始引入的现代化异步编程框架，通过结构化并发模型显著简化了异步代码的编写，同时保证了线程安全和性能。本文将深入解析其核心特性与实现原理。

# 什么是Swift Concurrency？

Swift Concurrency 是 Swift 语言对并发编程的系统性支持，它包括一系列语言特性和标准库类型，使得编写异步和并发代码变得更加安全、简洁和高效。

## 为什么要使用Swift Concurrency？

传统的异步编程方式，如使用回调函数或第三方库，存在以下问题：

- **回调地狱**：多层嵌套的回调导致代码难以阅读和维护
- **状态管理复杂**：异步操作的状态难以追踪和调试
- **线程安全难以保证**：共享状态的并发访问容易引发数据竞争
- **资源管理困难**：任务的生命周期管理不规范

Swift Concurrency 通过结构化并发模型从根本上解决了这些问题。

# 核心特性

## 1. async/await

async/await 让异步代码拥有同步代码的简洁性和可读性，彻底告别回调地狱。

### 基本用法

```swift
// 定义异步函数
func fetchUserData() async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: userURL)
    return try JSONDecoder().decode(User.self, from: data)
}

// 调用异步函数
func loadUser() async {
    do {
        let user = try await fetchUserData()
        updateUI(with: user)
    } catch {
        handleError(error)
    }
}
```

### 并发调用

使用 `async let` 可以并发执行多个异步操作：

```swift
func loadMultipleResources() async {
    // 并发启动多个异步操作
    async let userData = fetchUserData()
    async let settings = fetchUserSettings()
    async let notifications = fetchNotifications()
    
    do {
        // 等待所有结果
        let (user, settings, notifications) = try await (userData, settings, notifications)
        await updateUI(user: user, settings: settings, notifications: notifications)
    } catch {
        handleError(error)
    }
}
```

### await的工作原理

`await` 关键字表示暂停当前协程的执行，等待异步操作完成。在等待期间，Swift 运行时可以释放当前线程去执行其他任务，从而提高线程利用率。

## 2. Task 结构化并发

Task 是 Swift Concurrency 中用于执行异步操作的基本单位。

### Task的基本使用

```swift
// 创建并启动一个Task
let task = Task {
    let result = await someAsyncFunction()
    return result
}

// 等待结果
let value = await task.value

// 取消Task
task.cancel()
```

### TaskGroup

TaskGroup 用于管理一组并发任务的执行：

```swift
func processItems() async throws -> [Result] {
    try await withThrowingTaskGroup(of: Result.self) { group in
        for item in items {
            group.addTask {
                try await processItem(item)
            }
        }
        
        var results: [Result] = []
        for try await result in group {
            results.append(result)
        }
        return results
    }
}
```

### Task的生命周期

```swift
// Detached Task - 独立于调用者
let detachedTask = Task.detached {
    await doBackgroundWork()
}

// Task优先级
let highPriorityTask = Task(priority: .high) {
    // 高优先级任务
}

// 任务取消检查
let cancellableTask = Task {
    for item in items {
        try Task.checkCancellation()  // 检查是否被取消
        await process(item)
    }
}
```

### MainActor

使用 `@MainActor` 确保代码在主线程上执行：

```swift
// 在Actor或类上标记
@MainActor
class ViewModel: ObservableObject {
    @Published var user: User?
    
    // 这个方法会在主线程上执行
    func loadUser() async {
        let user = await fetchUser()
        self.user = user  // 安全更新UI相关状态
    }
}

// 在函数上标记
@MainActor
func updateUI() {
    // 确保在主线程执行
}
```

## 3. Actor 线程安全模型

Actor 是 Swift Concurrency 中用于确保线程安全的类型。

### Actor的基本用法

```swift
actor UserDataCache {
    private var cache: [String: User] = [:]
    
    func getUser(by id: String) -> User? {
        return cache[id]
    }
    
    func cacheUser(_ user: User) {
        cache[user.id] = user
    }
    
    func clearCache() {
        cache.removeAll()
    }
}

// 使用Actor
let cache = UserDataCache()
let user = await cache.getUser(by: "123")
```

### Actor的隔离特性

Actor 确保内部状态只能通过异步方法访问，从而避免数据竞争：

```swift
actor Counter {
    private var count = 0
    
    func increment() -> Int {
        count += 1
        return count
    }
    
    func getCount() -> Int {
        return count
    }
}

// 每个Actor实例都有自己的隔离域
let counter1 = Counter()
let counter2 = Counter()
```

### @MainActor vs Actor

- `@MainActor`：确保代码在主线程执行，主要用于UI相关代码
- `Actor`：确保代码在独立的隔离域中执行，用于通用线程安全

## 4. Sendable 协议与数据安全

Sendable 协议在编译期确保跨并发域传递数据的安全性。

### 什么是Sendable？

符合 Sendable 协议的类型可以在并发环境安全地传递，不会引起数据竞争。

```swift
// 值类型自动符合Sendable
struct User: Sendable {
    let id: String
    let name: String
    let email: String
}

// 枚举也可以是Sendable
enum NetworkError: Error, Sendable {
    case invalidURL
    case noData
    case decodingError
}
```

### Sendable的类型

- **值类型**（struct、enum）：如果所有成员都是Sendable，则自动符合
- **不可变类**：final class + 所有属性不可变
- **Actor**：自动符合Sendable

### @unchecked Sendable

对于无法自动满足Sendable要求的类，可以使用 @unchecked Sendable：

```swift
final class DataProcessor: @unchecked Sendable {
    private let lock = NSLock()
    private var cache: [String: Data] = [:]
    
    func process(_ data: Data) -> Data {
        lock.lock()
        defer { lock.unlock() }
        // 手动保证线程安全
        return data
    }
}
```

### @Sendable闭包

```swift
// Task自动要求闭包是@Sendable
Task {
    // 这个闭包必须是Sendable
    await someAsyncFunction()
}

// 显式标记
let sendableClosure: @Sendable () async -> Void = {
    await doSomething()
}
```

# 底层实现机制

## 编译器静态类型检查

- **类型安全验证**：编译器检查跨并发域传递的类型是否满足 Sendable 要求
- **值类型**：仅包含 Sendable 属性的 struct/enum 自动隐式符合
- **引用类型**：需要显式标记或使用 @unchecked Sendable

## 运行时隔离机制

- **Actor 隔离域**：Actor 方法的参数和返回值必须是 Sendable 类型
- **协程调度**：Swift 运行时负责协程的调度和管理

## SIL层优化

- **编译时检查**：Swift 编译器在生成 SIL 时插入并发安全检查
- **零成本抽象**：Sendable 在运行时无额外开销

# 常见使用场景

## 网络请求

```swift
func fetchUser(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// 并发请求多个用户
func fetchUsers(ids: [String]) async throws -> [User] {
    try await withThrowingTaskGroup(of: User.self) { group in
        for id in ids {
            group.addTask {
                try await fetchUser(id: id)
            }
        }
        
        var users: [User] = []
        for try await user in group {
            users.append(user)
        }
        return users
    }
}
```

## 数据库操作

```swift
actor DatabaseManager {
    private var connection: Connection?
    
    func connect() async throws {
        connection = try await Connection.connect()
    }
    
    func query(_ sql: String) async throws -> [Row] {
        guard let conn = connection else {
            throw DatabaseError.notConnected
        }
        return try await conn.query(sql)
    }
}
```

## 并行处理

```swift
func processImages(_ images: [UIImage]) async -> [UIImage] {
    await withTaskGroup(of: UIImage.self) { group in
        for image in images {
            group.addTask {
                await self.processImage(image)
            }
        }
        
        var processed: [UIImage] = []
        for await result in group {
            processed.append(result)
        }
        return processed
    }
}
```

# 最佳实践

1. **优先使用值类型**：利用自动的 Sendable 一致性，减少线程安全问题
2. **合理使用 Actor**：对需要共享状态的操作使用 Actor 保护
3. **避免过度并发**：根据实际需求创建任务，避免不必要的上下文切换
4. **利用结构化并发**：确保所有任务都有明确的生命周期管理
5. **使用 @MainActor**：UI 相关代码使用 @MainActor 确保线程安全

```swift
// 推荐的实践模式
@MainActor
class MyViewModel: ObservableObject {
    @Published var state: ViewState = .idle
    
    func loadData() async {
        state = .loading
        
        do {
            let data = try await fetchData()
            state = .loaded(data)
        } catch {
            state = .error(error)
        }
    }
}
```

# Swift 6并发改进

Swift 6 引入了更严格的并发检查，帮助开发者在编译期发现潜在的线程安全问题：

- **Complete Concurrency Checking**：启用完整的并发检查
- **Sendable 推断改进**：更智能的 Sendable 类型推断
- **Actor 性能优化**：更高效的 Actor 间通信

# 总结

Swift Concurrency 通过编译期安全和运行时优化的结合，为开发者提供了既安全又高效的并发编程体验：

| 特性 | 作用 |
|------|------|
| async/await | 简化异步代码，让异步像同步一样简洁 |
| Task | 结构化并发，管理异步任务生命周期 |
| Actor | 线程安全，保护共享状态 |
| Sendable | 编译期安全检查，防止数据竞争 |

掌握 `Swift Concurrency` 是现代 iOS/macOS 开发的必备技能，它能让你的代码更加安全、简洁和高效。
