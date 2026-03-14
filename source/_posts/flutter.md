---
title: 使用 Flutter 构建界面
categories: Flutter
tags: Flutter
---

# Flutter Docs

```
Flutter widgets are built using a modern framework that takes inspiration from React. The 
central idea is that you build your UI out of widgets. Widgets describe what their view 
should look like given their current configuration and state. When a widget's state changes, 
the widget rebuilds its description, which the framework diffs against the previous description
in order to determine the minimal changes needed in the underlying render tree to transition from 
one state to the next.
```

## Flutter的渊源

提起flutter，我第一次知道的时候是在趣丸科技任职期间，公司突然从各个业务线调取一两个同事临时组建海外TT语音的flutter版本。那段时间，公司的研发中心组织了好多次flutter的学习，后面我真正接触开发却是在荔枝集团的时候，刚好也是趣丸科技和荔枝内部的技术交流掀起的新技术栈尝试。不过也是小面积业务尝试，不像TT语音那样是一个纯粹的Flutter项目，前期有几个刚毕业没多久的同事熬不过长期的加班踩坑填坑而离职😅

说实话学一门语言很快，几天就可以上手写项目，但如果项目不从事相关技术栈的话很快就把这些知识给忘光了，不过捡起来也很快，加上现在有各种AI编程工具加持。Flutter官网文档还有针对拥有其他平台开发经验的友好指南，不得不说很贴心，这也就是吸引其他端开发者能够拥抱它的一个很重要的点吧。

## Flutter的技术选型

我们选择 Flutter 作为主要跨端开发框架，是经过深入的技术调研和权衡后做出的战略决策。主要考量点可以归纳为以下四个方面：

### 1. 极致的开发效率与热重载 (Hot Reload)

这是 Flutter 最吸引人的特性，也是提升开发效率的“杀手锏”。

- 快速迭代： 热重载功能允许我们在修改代码后，几乎立即（通常在毫秒到秒级内）看到更改效果，而无需重新启动应用。这彻底改变了开发流程。

- 提升体验： 对于UI调试、样式调整和修复小bug来说，这几乎是革命性的。设计师在旁边调整一个间距或颜色，开发者可以实时修改并看到效果，极大地促进了设计与开发的协作。

- 状态保持： 热重载会尽力保持应用当前的状态，这意味着你可以在一个表单填写到一半、或者页面滚动到某个位置时进行代码修改，修改后应用会在这个状态基础上更新，无需从头开始操作来复现问题。

**选型考量**： 相比于其他框架（如 React Native）的“热更新”（Hot Module Replacement, HMR），Flutter 的热重载更加稳定和快速，这能显著缩短开发周期，降低时间成本。

### 2. 出色的跨端一致性 (Consistency)

这是我们追求“一次编写，多处运行”理想状态的核心原因。

- 自绘引擎 (Skia)： Flutter 不像其他框架那样依赖原生（Native）组件。它使用自己的高性能渲染引擎（Skia）来绘制每一像素。这意味着：

  - UI 表现完全一致： 在 iOS 和 Android 上，应用的视觉效果、字体、动效等100%相同，彻底避免了因原生组件差异带来的样式和体验上的碎片化问题。

  - 摆脱平台限制： 我们不再需要为不同平台编写额外的适配代码，或者处理原生组件不同行为带来的兼容性问题。一套UI设计稿，一套代码，即可实现完美复现。

- 定制化UI： 由于不依赖原生控件，实现高度定制化的、品牌特有的UI设计（例如某种复杂的动画或非标准的控件）变得异常简单，不再受限于平台原生控件的能力。

**选型考量**： 对于追求品牌统一性和极致用户体验的产品来说，Flutter 提供的一致性保障是无可替代的。它确保了所有用户，无论使用何种设备，都能获得完全相同的体验。

### 3. 高性能 (Performance)

性能是技术选型的基石，Flutter 在这方面表现优异。

- 编译为原生代码 (AOT & JIT)：

  - 发布模式 (AOT)： 应用会被提前编译（Ahead-Of-Time）成机器码（ARM/x86库）。这保证了发布版应用拥有媲美原生平台的高性能启动速度和运行体验。
  - 开发模式 (JIT)： 采用即时编译（Just-In-Time），这正是支持热重载的基础，在开发时牺牲一点性能换取极致的开发效率。

- 摆脱桥接 (No JavaScript Bridge)： 这是与 React Native 等基于 JavaScript 的框架的关键区别。许多这类框架在调用原生模块时需要经过一个“JavaScript桥接器”，这可能会引起性能瓶颈（如频繁通信导致的丢帧）。而 Flutter 的 Dart 代码直接编译为原生代码，UI和业务逻辑的执行效率极高，动画可以流畅达到 60fps 甚至 120fps。

**选型考量**： 我们需要一个既能满足复杂交互动画需求，又能保证在低端设备上流畅运行的技术方案。Flutter 的架构设计使其在性能上更接近原生开发，避免了“桥接”带来的潜在性能问题。

### 4. 编程语言与生态系统 (Dart & Ecosystem)

- Dart 语言： 选择 Flutter 也意味着选择了 Dart 语言。它的优点非常契合 Flutter 的需求：

  - 强类型语言： 支持静态类型检查，这能在开发早期发现大量错误，提高了代码的健壮性和可维护性。
  - 易于学习： 对于有 Java/JavaScript/Kotlin/Swift 背景的开发者来说，Dart 语法非常容易上手，学习曲线平缓。
  - 丰富的标准库： 提供了强大的现代化标准库，非常适合UI开发。

- 蓬勃发展的生态系统：

  - 丰富的包库： Pub.dev 上有大量高质量的开源包，覆盖了从网络、数据库到各种原生功能（如相机、地图、蓝牙）的插件，极大加速了开发进程。
  - 强大的社区和谷歌支持： 作为由 Google 主导的项目，Flutter 拥有庞大且活跃的社区，能确保技术的长期维护和更新。其“跨端”愿景也已扩展到 Web 和桌面端（Windows, macOS, Linux），为未来技术规划提供了更多可能性。

总而言之，我们的选型决策是基于一个综合考虑：

| 考量维度 |	Flutter 的优势	| 带来的价值 |
| :---   |        :---      |:---|
|开发效率  |	热重载 | 快速迭代，缩短开发周期，提升开发者幸福感 |
|产品体验 |	跨端一致性| 保证所有用户获得统一、高质量的UI/UX体验|
技术性能 |	高性能原生编译、无桥接 | 应用流畅、稳定，媲美原生性能|
|长期发展 | Dart语言、强大生态、多平台潜力 | 代码健壮、易于维护，技术有未来|

## 状态管理

Flutter 状态管理的发展是一个从简单到复杂、从耦合到解耦的演进过程，其核心思想是将 UI 与业务逻辑分离。下图展示了这一演进路径：

![状态管理](<images/stateManager.png>)

### setState：最基础的内置方法

- 核心思想：在 StatefulWidget 内部管理状态。当状态改变时，调用 setState(() {}) 来通知框架“数据变了，需要重绘UI”。
- 适用场景：

  - 简单的、局部化的状态（例如：一个页面的计数器、一个复选框的选中状态）。
  - widget 本身的临时状态。
- 代码示例：
```dart
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() { // 调用setState触发重建
      _counter++; // 更新状态
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Text('You have pushed the button $_counter times.'),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter, // 触发状态更改
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
```

- 优点：

  - 无需引入第三方包，Flutter 内置。
  - 非常简单直观，适合初学者和小功能。
- 缺点：

  - 业务逻辑与UI高度耦合：状态和逻辑都写在 UI 代码里，难以测试和复用。
  - 性能影响：调用 setState 会重建整个 StatefulWidget，如果子树很大，会有不必要的性能开销。
  - 无法跨组件共享状态：状态被封装在单个 widget 内，难以传递给其他不直接关联的 widget。

### Provider：官方推荐的 InheritedWidget 语法糖
- 核心思想：基于 Flutter 原有的 InheritedWidget，将其变得极其易用。它提供了一种在 widget 树中从上向下传递数据的方式。子组件可以监听这些数据的变化，并在数据变化时自动重建。
- 适用场景：

  - 中小型应用的状态管理。
  - 需要跨组件共享状态（如用户信息、主题设置）。
- 代码示例：

 - 1. 定义状态模型（使用 ChangeNotifier）:
  ```dart
  import 'package:flutter/material.dart';

  class CounterModel with ChangeNotifier {
    int _count = 0;
    int get count => _count;

    void increment() {
      _count++;
      notifyListeners(); // 关键：通知所有监听者重建
    }
  }
```

- 2. 在顶层提供（Provide）状态:
  ```dart
  void main() {
    runApp(
      ChangeNotifierProvider(
        create: (context) => CounterModel(), // 创建状态对象
        child: MyApp(),
      ),
    );
  }
```

- 3.在子组件中读取和使用状态:
  ```dart
  // 读取状态
  final counter = Provider.of<CounterModel>(context);
  Text('Count: ${counter.count}'),

  // 或使用 Consumer，更高效地只在需要时重建
  Consumer<CounterModel>(
    builder: (context, counter, child) => Text('Count: ${counter.count}'),
  ),

  FloatingActionButton(
    onPressed: () => counter.increment(), // 修改状态
  )
```

- 优点：

  - 官方推荐，概念清晰，学习曲线平缓。
  - 解耦了UI和业务逻辑（逻辑在 ChangeNotifier 里）。
  - 性能优异，Consumer/Selector 可以精细控制重建范围。
- 缺点：  

  - 需要结合 ChangeNotifier 等类一起使用，模板代码稍多。
  - 对异步操作的支持需要手动处理（例如在调用 API 时处理加载和错误状态）。


### Bloc：高度结构化的响应式状态管理

- 核心思想：严格遵循 BLoC 模式（Business Logic Component） 和 Redux 模式的思想。核心概念是 Event（事件）-> Bloc（处理）-> State（状态）。UI 发送 Event，Bloc 处理逻辑并输出新的 State，UI 监听并响应 State 的变化。
- 适用场景：

  - 中大型复杂应用，业务逻辑繁重。
  - 需要极高可测试性和可预测性的项目。
  - 需要强大调试工具（Bloc DevTools）的场景。
- 代码示例：

- 1. 定义 Event 和 State:
```dart
// events
abstract class CounterEvent {}
class IncrementEvent extends CounterEvent {}

// states
abstract class CounterState {}
class CounterInitial extends CounterState { final int count; CounterInitial(this.count); }
```

  - 2. 创建 Bloc 处理逻辑:
```dart
class CounterBloc extends Bloc<CounterEvent, CounterState> {
  CounterBloc() : super(CounterInitial(0)) {
    on<IncrementEvent>((event, emit) {
      // 处理逻辑，产生新状态
      emit(CounterInitial(state.count + 1));
    });
  }
}
```

  - 3. 在UI层中使用:
```dart
// 提供Bloc
BlocProvider(
  create: (context) => CounterBloc(),
  child: MyPage(),
);

// 在UI中访问
BlocBuilder<CounterBloc, CounterState>(
  builder: (context, state) {
    return Text('Count: ${state.count}');
  },
);

FloatingActionButton(
  onPressed: () => context.read<CounterBloc>().add(IncrementEvent()),
)
```
- 优点：

  - 职责分离极致：UI 只关心渲染和发送事件，业务逻辑全部在 Bloc 中，易于测试。
  - 可预测性强：状态变化路径唯一，方便调试和追溯问题。
  - 强大的工具链：Bloc DevTools 可以时间旅行调试。
  - 天然支持异步：基于 Stream，处理复杂异步流非常方便。
- 缺点：

  - 模板代码非常多：即使是简单功能，也需要创建 Event、State 和 Bloc 类。
  - 学习曲线较陡：需要理解 Stream、RxDart 以及其设计模式。


### Riverpod(对Provider的升级版，解决其痛点、有依赖注入、路由等功能)

- 核心思想：由 Provider 的作者重写，旨在解决 Provider 的所有缺点。它的核心是 Provider（提供者）和 Ref（引用）。最大特点是编译安全、不依赖 BuildContext 和支持多种不同类型的 Provider。
- 适用场景：

  - 任何规模的项目，尤其是新项目。
  - 厌倦了 Provider 的 Context 依赖和 Bloc 的模板代码的开发者。
  - 需要更灵活、更强大的依赖注入。
- 代码示例：

  - 1. 创建 Provider:
  ```dart
  // 定义一个计数器状态Provider
final counterProvider = StateNotifierProvider<CounterNotifier, int>((ref) {
  return CounterNotifier();
});

// 状态通知器（类似Bloc，但更轻量）
class CounterNotifier extends StateNotifier<int> {
  CounterNotifier() : super(0); // 初始状态为0

  void increment() => state++;
}
```
- 2. 在UI中使用（无需Context!）:
```dart
class MyWidget extends ConsumerWidget { // 注意是ConsumerWidget
  @override
  Widget build(BuildContext context, WidgetRef ref) { // 多了一个ref参数
    final count = ref.watch(counterProvider); // 监听状态
    return Scaffold(
      body: Text('Count: $count'),
      floatingActionButton: FloatingActionButton(
        onPressed: () => ref.read(counterProvider.notifier).increment(),
      ),
    );
  }
}
```

- 优点：

  - 编译安全：拼写错误会在编译时报错，而不是运行时。
  - 不依赖 BuildContext：可以在任何地方（如非 Widget 类）轻松地读取状态。
  - 灵活的测试：可以非常容易地覆写 Provider 的行为进行测试。
  - 丰富的Provider类型：FutureProvider、StreamProvider、StateNotifierProvider 等开箱即用，极大简化异步操作和状态管理。
- 缺点：

  - 较新的生态：虽然发展迅速，但社区规模和经典方案如 Bloc 相比仍有差距。
  - 概念独特：需要理解 ref 和不同的 provider 类型。

### 总结与选型建议

| 特性	| setState |	Provider |	Bloc |	Riverpod
| :---   | :---  | :---   | :---  |:---|
|学习曲线	| 非常平缓 |	平缓|	陡峭	|中等 |
|模板代码	|少	|中等|	非常多	|少|
|可测试性	|差|	良好	|优秀	|优秀|
|可预测性	|低|	中等	|非常高	|高 |
|解耦程度	|耦合	|解耦|	完全解耦	|完全解耦 |
|性能	|可能差	|优秀|	优秀|	优|秀
|适用场景	|局部状态	|中小应用	|大型复杂应用|	任何规模应用 |

### 如何选择？

- 极简场景/初学者：从 setState 开始，理解状态管理的概念。
- 中小型项目/快速开发：选择 Provider。它是官方推荐且平衡性最好的方案。
- 大型复杂项目/团队协作：选择 Bloc。它的强结构和可预测性在长期维护和团队开发中优势明显。
- 新项目/追求现代和灵活性：强烈推荐 Riverpod。它解决了前人的诸多痛点，是未来趋势，功能和体验都非常出色。

### 最终建议：没有最好的，只有最合适的。 深入了解每个方案的思想和优缺点，根据你的项目规模、团队经验和具体需求来做决定。对于个人学习者，建议都尝试一遍，这能极大地提升你对 Flutter 的理解深度。

## Flutter和原生（iOS/Android）的混合开发

Flutter 和原生（iOS/Android）的混合编排与通信是整个混合开发框架的核心。

Flutter 与原生通信的核心是 Platform Channel（平台通道）。它建立了一条双向的、异步的通信桥梁，让 Dart 代码和原生代码（Objective-C/Swift, Java/Kotlin）可以相互调用并传递数据。

整个架构可以概括为下图所示的工作流程：

![Channel通道](<images/dart_channel.png>)

### 1. 通信的核心：Platform Channel (平台通道)

Platform Channel 是消息传递的媒介，它确保数据在 Dart 和原生端之间正确地序列化和反序列化。主要有三种类型：

- BasicMessageChannel：用于基本数据传递（字符串、字节码），更像是“事件监听”模式，可持续通信。
- MethodChannel：最常用，用于方法调用。Dart 端可以调用一个原生方法，并等待返回结果。这是典型的请求-响应模式。
- EventChannel：用于原生端向 Dart 端发送事件流（Stream），通常是原生端的传感器数据、广播等持续性的状态变化。

关键特性：

- 异步（Async）：所有通信都是异步的，这意味着 UI 线程不会被阻塞。
- 类型安全：传递的数据有严格的类型限制（如 String, int, double, bool, list, map 等）。

### 2. 混合编排 (Hybrid Composition)

“混合编排”指的是如何将 Flutter 生成的控件（Widget）和原生的 UI 控件（UIView/View）混合渲染在同一个页面上。这主要有两种方式：

a) 在原生应用中嵌入 Flutter (Add-to-App)

这是最常见的混合模式，即在已有的原生项目中，将某一个或几个页面/模块用 Flutter 来实现。

- 编排方式：

  - Flutter 引擎（FlutterEngine）被封装为一个原生的 FlutterViewController (iOS) / FlutterFragment 或 FlutterActivity (Android)。
  - 你可以像使用普通原生 ViewController 或 Activity 一样，通过导航控制器（如 UINavigationController）来 push 或 present 这个 Flutter 页面。
  - 通信：这个 Flutter 页面通过 MethodChannel 与它所在的原生容器（Hosting Native App）进行通信。

b) 在 Flutter 应用中嵌入原生控件 (Platform View)

有时我们不得不在 Flutter 页面里使用一个成熟的原生控件，比如 WebView 或地图控件（Google Maps/MapKit），这些控件用 Flutter 重写成本极高。

- 编排方式：

  - Flutter 提供了 UiKitView (iOS) 和 AndroidView (Android) 这两个特殊的 widget。
  - 你可以在 Flutter 的 widget 树中嵌入这些 widget，它们会在对应的平台上创建一个“虚拟的”原生视图，并将其渲染到 Flutter 的纹理中。
  - 工作原理：Flutter 引擎会为原生控件预留一个“画布区域”，并将原生控件的渲染内容同步到这块画布上，使其看起来就像是 Flutter 自己渲染的一部分。
  - 通信：嵌入的原生控件可以通过 MethodChannel 与包裹它的 Flutter 父组件进行通信。例如，Flutter 侧监听地图的点击事件，或者原生地图接收 Flutter 侧传来的坐标参数。

### 3. 通信流程详解 (以最常用的 MethodChannel 为例)

假设一个场景：Flutter 端需要获取手机的当前电量。

步骤 1: Flutter 端 (Dart) 发起调用

```dart
import 'package:flutter/services.dart';

// 1. 创建一个方法通道，通道名称'BatteryChannel'必须两端一致
static const methodChannel = MethodChannel('BatteryChannel');

// 2. 发起方法调用
Future<void> _getBatteryLevel() async {
  try {
    // 通过通道调用原生方法'getBatteryLevel'
    final int result = await methodChannel.invokeMethod('getBatteryLevel');
    print('当前电量: $result%');
  } on PlatformException catch (e) {
    // 处理通信失败或原生代码抛出的异常
    print("获取电量失败: '${e.message}'");
  }
}

```

步骤 2: iOS 端 (Swift) 实现接收
```swift
// 在 AppDelegate 或 FlutterViewController 中
import UIKit
import Flutter

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)

    // 1. 获取FlutterViewController
    let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
    // 2. 创建方法通道
    let batteryChannel = FlutterMethodChannel(name: "BatteryChannel",
                                              binaryMessenger: controller.binaryMessenger)
    // 3. 设置方法调用处理器
    batteryChannel.setMethodCallHandler({
      [weak self] (call: FlutterMethodCall, result: FlutterResult) -> Void in
      // 检查被调用的方法名
      guard call.method == "getBatteryLevel" else {
        result(FlutterMethodNotImplemented)
        return
      }
      // 调用原生方法获取电量
      self?.receiveBatteryLevel(result: result)
    })

    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  private func receiveBatteryLevel(result: FlutterResult) {
    // 使用iOS原生API获取电量的逻辑 ...
    let device = UIDevice.current
    device.isBatteryMonitoringEnabled = true
    if device.batteryState == .unknown {
      result(FlutterError(code: "UNAVAILABLE",
                          message: "电量信息不可用",
                          details: nil))
    } else {
      result(Int(device.batteryLevel * 100))
    }
  }
}
```

步骤 3: Android 端 (Kotlin) 实现接收
```kotlin
// 在您的 Activity 或 FlutterFragment 中
public class MainActivity : FlutterActivity() {
  private val CHANNEL = "BatteryChannel" // 通道名称必须与Dart端一致

  override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    // 设置方法调用处理器
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler {
      call, result ->
      // 检查被调用的方法名
      if (call.method == "getBatteryLevel") {
        val batteryLevel = getBatteryLevel()
        if (batteryLevel != -1) {
          // 成功，将结果返回给Dart端
          result.success(batteryLevel)
        } else {
          // 失败，返回错误信息
          result.error("UNAVAILABLE", "无法获取电量.", null)
        }
      } else {
        // 找不到该方法
        result.notImplemented()
      }
    }
  }

  private fun getBatteryLevel(): Int {
    // 使用Android原生API获取电量的逻辑 ...
  }
}
```

### 总结

- 通信机制：通过 Platform Channel 进行异步消息传递，核心是 MethodChannel。
混合编排：

  - 大粒度混合：将整个 Flutter 页面/模块作为原生应用的一部分来集成（FlutterActivity/FlutterViewController）。
  - 小粒度混合：在 Flutter 页面中嵌入单个原生控件（AndroidView/UiKitView）。

- 数据传递：数据在通道中被自动序列化和反序列化，支持基本数据类型和集合。

这种设计使得 Flutter 既保持了独立性（自绘UI），又能灵活地与原生系统深度交互，实现了真正的“混合”开发。





# 贴一下之前在极客时间里学习到的 Flutter核心技术与实践  

## 开篇词 | 为什么每一位大前端从业者都应该学习Flutter？ 

## 01 | 预习篇 · 从0开始搭建Flutter工程环境 

## 02 | 预习篇 · Dart语言概览 

## Flutter开发起步 (3讲)

## 03 | 深入理解跨平台方案的历史发展逻辑 

## 04 | Flutter区别于其他方案的关键技术是什么？ 

## 05 | 从标准模板入手，体会Flutter代码是如何运行在原生系统上的 

## Dart语言基础 (3讲)

## 06 | 基础语法与类型变量：Dart是如何表示信息的？ 

## 07 | 函数、类与运算符：Dart是如何处理信息的?

## 08 | 综合案例：掌握Dart核心特性 

## Flutter基础 (13讲)

## 09 | Widget，构建Flutter界面的基石 

## 10 | Widget中的State到底是什么？ 

## 11 | 提到生命周期，我们是在说什么？ 

## 12 | 经典控件（一）：文本、图片和按钮在Flutter中怎么用？

## 13 | 经典控件（二）：UITableView/ListView在Flutter中是什么？

## 14 | 经典布局：如何定义子控件在父容器中排版的位置？

## 15 | 组合与自绘，我该选用何种方式自定义Widget？ 

## 16 | 从夜间模式说起，如何定制不同风格的App主题？ 

## 17 | 依赖管理（一）：图片、配置和字体在Flutter中怎么用？ 

## 18 | 依赖管理（二）：第三方组件库在Flutter中要如何管理？ 

## 19 | 用户交互事件该如何响应？ 

## 20 | 关于跨组件传递数据，你只需要记住这三招 

## 21 | 路由与导航，Flutter是这样实现页面切换的 

## Flutter进阶 (17讲)

## 22 | 如何构造炫酷的动画效果？ 

## 23 | 单线程模型怎么保证UI运行流畅？ 

## 24 | HTTP网络编程与JSON解析 

## 25 | 本地存储与数据库的使用和优化 

## 26 | 如何在Dart层兼容Android/iOS平台特定实现？（一） 

## 27 | 如何在Dart层兼容Android/iOS平台特定实现？（二） 

## 28 | 如何在原生应用中混编Flutter工程？ 

## 29 | 混合开发，该用何种方案管理导航栈？ 

## 30 | 为什么需要做状态管理，怎么做？ 

## 31 | 如何实现原生推送能力？ 

## 32 | 适配国际化，除了多语言我们还需要注意什么? 

## 33 | 如何适配不同分辨率的手机屏幕？ 

## 34 | 如何理解Flutter的编译模式？ 

## 35 | Hot Reload是怎么做到的？ 

## 36 | 如何通过工具链优化开发调试效率？ 

## 37 | 如何检测并优化Flutter App的整体性能表现？ 

## 38 | 如何通过自动化测试提高交付质量？ 

## Flutter综合应用 (6讲)

## 39 | 线上出现问题，该如何做好异常捕获与信息采集？ 

## 40 | 衡量Flutter App线上质量，我们需要关注这三个指标 

## 41 | 组件化和平台化，该如何组织合理稳定的Flutter工程结构？ 

## 42 | 如何构建高效的Flutter App打包发布环境？ 

## 43 | 如何构建自己的Flutter混合开发框架（一）？ 

## 44 | 如何构建自己的Flutter混合开发框架（二）？ 

```
import 'package:flutter/material.dart';

class MyAppBar extends StatelessWidget {
  const MyAppBar({required this.title, super.key});

  // Fields in a Widget subclass are always marked "final".

  final Widget title;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 56, // in logical pixels
      padding: const EdgeInsets.symmetric(horizontal: 8),
      decoration: BoxDecoration(color: Colors.blue[500]),
      // Row is a horizontal, linear layout.
      child: Row(
        children: [
          const IconButton(
            icon: Icon(Icons.menu),
            tooltip: 'Navigation menu',
            onPressed: null, // null disables the button
          ),
          // Expanded expands its child
          // to fill the available space.
          Expanded(child: title),
          const IconButton(
            icon: Icon(Icons.search),
            tooltip: 'Search',
            onPressed: null,
          ),
        ],
      ),
    );
  }
}

class MyScaffold extends StatelessWidget {
  const MyScaffold({super.key});

  @override
  Widget build(BuildContext context) {
    // Material is a conceptual piece
    // of paper on which the UI appears.
    return Material(
      // Column is a vertical, linear layout.
      child: Column(
        children: [
          MyAppBar(
            title: Text(
              'Example title',
              style:
                  Theme.of(context) //
                      .primaryTextTheme
                      .titleLarge,
            ),
          ),
          const Expanded(child: Center(child: Text('Hello, world!'))),
        ],
      ),
    );
  }
}

void main() {
  runApp(
    const MaterialApp(
      title: 'My app', // used by the OS task switcher
      home: SafeArea(child: MyScaffold()),
    ),
  );
}
```


