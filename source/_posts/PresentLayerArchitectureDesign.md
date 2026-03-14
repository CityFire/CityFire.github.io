---
title: 表现层框架设计
tags: 设计模式
categories: 框架设计
---

表现层框架设计是软件开发中的核心话题之一。随着应用规模的不断扩大，如何组织代码结构、分离关注点、提高代码可维护性成为开发者必须面对的问题。表现层架构模式为这一问题提供了成熟的解决方案，帮助开发者构建更加清晰、可维护的用户界面代码。

## 表现层设计模式

### 1、MVC模式

**MVC（Model-View-Controller）** 是最经典的表现层架构模式，最早由Trygve Reenskaug在1979年提出，后来被广泛用于桌面和Web应用开发。

传统的MVC模式分为三个核心组件：

- **Model（模型层）**：负责数据管理和业务逻辑。Model是应用的核心，包含了应用的数据和对数据的操作。在"胖Model"模式下，Model不仅存储数据，还包含数据验证、业务计算等逻辑；而在"瘦Model"模式下，Model仅作为单纯的数据容器。

- **View（视图层）**：负责用户界面的展示。View从Model获取数据并将其渲染成用户可见的界面，同时接收用户的输入事件。

- **Controller（控制器层）**：负责协调Model和View。Controller处理用户的输入，调用Model进行业务处理，然后选择合适的View进行展示。

MVC模式的工作流程是：用户与View进行交互，View将用户动作转发给Controller，Controller操作Model进行业务处理，Model更新后通知View重新渲染。MVC模式的优点是职责分离清晰，缺点是Controller和View耦合度较高，测试困难。

![MVC](<images/mvc.jpeg>)


### 2、MVP模式

**MVP（Model-View-Presenter）** 模式是对MVC模式的改进，旨在解决MVC中Controller难以测试的问题。MVP模式最初由IBM开发，现在广泛应用于桌面和移动应用开发。

MVP框架由三部分组成：

- **Model（模型层）**：提供数据接口，负责数据的获取和存储。Model层不包含任何UI相关的逻辑。

- **View（视图层）**：负责数据的显示。View是被动的，它不主动获取数据，而是由Presenter推送数据。

- **Presenter（展示层）**：负责逻辑处理。Presenter充当View和Model之间的桥梁，从Model获取数据并格式化后推送给View。

MVP模式的核心创新在于引入了**View Interface**（视图接口）。View需要实现ViewInterface接口，Presenter通过接口与View通信，这样可以完全解耦Presenter和具体View的实现，便于单元测试。

MVP模式的工作流程是：用户与View交互，View调用Presenter的方法处理业务，Presenter操作Model获取数据，Presenter将处理后的数据通过ViewInterface接口更新View。

![MVP](<images/mvp.webp>)

**MVP与MVC的区别**：
- MVC中Controller直接控制View，耦合度高；MVP中Presenter通过接口与View交互，解耦更好
- MVC中Model变化时通过观察者模式通知View；MVP中Presenter主动更新View
- MVP的Presenter更容易进行单元测试


### 3、MVVM模式

**MVVM（Model-View-ViewModel）** 模式是一种将用户界面从业务逻辑和数据模型中分离出来的架构模式。它是在MVC模式的基础上发展而来的，最初由微软提出并应用于WPF和Silverlight开发，后来被广泛应用于前端开发（Vue.js、Angular）和移动端开发（Android的Data Binding、iOS的SwiftUI）。

MVVM框架由三部分组成：

- **Model（模型层）**：负责数据管理和业务逻辑，包括数据结构、数据访问接口、数据验证等。Model层与ViewModel层进行数据交互，但不直接与View层通信。

- **View（视图层）**：负责用户界面的展示，包括UI组件、布局、样式等。View层通过数据绑定（Data Binding）与ViewModel层进行双向通信，当ViewModel中的数据发生变化时，View会自动更新。

- **ViewModel（视图模型层）**：是View层和Model层之间的桥梁，负责处理视图的逻辑和状态管理。ViewModel暴露View所需的数据和命令，同时将Model的数据转换为View可以展示的格式。

MVVM模式的核心特性是**数据绑定**。通过数据绑定，ViewModel中的数据变化可以自动反映到View上，而用户对View的操作也可以自动触发ViewModel中的逻辑处理。这种机制大大简化了代码，减少了手动更新UI的繁琐工作。

MVVM模式的主要优点包括：

- **低耦合性**：ViewModel与View解耦，可以独立开发和测试
- **可维护性**：业务逻辑集中在ViewModel中，便于维护和修改
- **可测试性**：ViewModel不依赖UI组件，可以独立进行单元测试
- **数据驱动**：通过数据绑定实现自动更新，减少样板代码

![MVVM](<images/mvvm.webp>)

**MVVM与MVP的区别**：
- MVP中Presenter需要手动调用View的更新方法；MVVM中通过数据绑定自动更新
- MVVM通常使用双向数据绑定；MVP中View是被动的
- MVVM更适合数据驱动型的应用


### 4、VIPER模式

**VIPER** 是一种更加细粒度的架构模式，它从另一个角度对职责进行了划分，将应用分为五个层次。这种模式最初由Mutual Mobile开发，特别适用于大型iOS应用。

VIPER模式的五个组件：

- **Interactor（交互器）**：包含数据操作和网络相关的业务逻辑。例如创建新的数据实体或从服务器获取数据。Interactor是业务逻辑的核心，不直接依赖UI。

- **Presenter（展示器）**：包含与UI无关的业务逻辑，可以调用Interactor中的方法。Presenter负责将Interactor返回的数据转换为View可以展示的格式。

- **Entities（实体）**：纯粹的数据对象，不包含任何业务逻辑。数据访问层属于Interactor的职责，而非Entities。

- **Router（路由）**：负责VIPER模块之间的导航转场。VIPER是第一个将导航职责单独划分出来的架构模式。

- **View（视图）**：负责用户界面的展示和用户交互事件的捕获。

VIPER模式与MV(X)系列的主要区别：

| 特性 | MV(X)系列 | VIPER |
|------|-----------|-------|
| 数据逻辑 | 在Model中 | 在Interactor中 |
| 数据结构 | 包含业务逻辑的Model | 纯粹的Entities对象 |
| 导航 | 嵌入在Controller/Presenter中 | 独立的Router层 |
| 粒度 | 较粗 | 较细 |


### 5、Flux与Redux

#### Flux

**Flux** 是Facebook（现Meta）开发的单向数据流架构，最初用于React应用。Flux的核心思想是通过单向数据流来管理应用状态，避免传统MVC模式中数据流向混乱的问题。

Flux将应用分成四个核心部分：

- **View（视图层）**：用户界面组件，负责渲染和用户交互。

- **Action（动作）**：View发出的消息，表示用户意图或系统事件，如点击按钮、网络请求完成等。

- **Dispatcher（派发器）**：中央枢纽，接收所有Action并分发给注册的回调函数。

- **Store（数据层）**：存储应用状态和业务逻辑，当状态变化时发出"change"事件通知View更新。

Flux的单向数据流：

```
1、用户访问View
2、View发出Action
3、Dispatcher接收Action，调用Store的回调函数
4、Store更新状态后，发出"change"事件
5、View收到"change"事件，重新渲染
```

这种单向流动使得应用状态变化可预测、可追踪，便于调试和维护。

![Flux](<images/flux.png>)

#### Redux

**Redux** 是JavaScript状态容器，提供可预测化的状态管理。Redux由Flux演变而来，但进行了简化和规范化，成为React生态中最流行的状态管理方案。

Redux的三大核心概念：

**Store（仓库）**：整个应用的状态存储在唯一的Store中，是一个单一的object tree。Store是只读的，不能直接修改，必须通过dispatch action来触发状态变化。

```javascript
// Store结构示例
{
  todos: [
    { text: 'Eat food', completed: true },
    { text: 'Exercise', completed: false }
  ],
  visibilityFilter: 'SHOW_COMPLETED'
}
```

**Action（动作）**：描述发生事件的普通对象，是改变state的唯一方式。每个action必须有一个type字段来描述动作类型：

```javascript
{ type: 'ADD_TODO', text: 'Go to swimming pool' }
{ type: 'TOGGLE_TODO', index: 1 }
{ type: 'SET_VISIBILITY_FILTER', filter: 'SHOW_ALL' }
```

**Reducer**：纯函数，接收state和action，返回新的state：

```javascript
function visibilityFilter(state = 'SHOW_ALL', action) {
  if (action.type === 'SET_VISIBILITY_FILTER') {
    return action.filter;
  }
  return state;
}

function todos(state = [], action) {
  switch (action.type) {
    case 'ADD_TODO':
      return [...state, { text: action.text, completed: false }];
    case 'TOGGLE_TODO':
      return state.map((todo, index) =>
        index === action.index
          ? { ...todo, completed: !todo.completed }
          : todo
      );
    default:
      return state;
  }
}

// 合并多个reducer
import { combineReducers, createStore } from 'redux';
const reducer = combineReducers({ visibilityFilter, todos });
const store = createStore(reducer);
```

Redux的三大原则：

- **单一数据源**：整个应用状态存储在一棵object tree中，只存在于唯一的Store
- **State是只读的**：唯一改变state的方法是dispatch action
- **使用纯函数执行修改**：Reducer必须是纯函数，不产生副作用


### 6、响应式编程模式

**响应式编程（Reactive Programming）** 是一种面向数据流和变化传播的编程范式。它强调异步数据流和观察者模式，使得程序能够对数据流的变化做出自动响应。在传统的命令式编程中，我们需要主动获取和更新数据；而在响应式编程中，我们只需定义数据变化的处理逻辑，系统会自动通知并处理这些变化。

响应式编程的核心概念：

- **Observable（可观察对象）**：表示一个数据流，可以发射零个、一个或多个数据项，并能在数据流结束时发射一个错误或完成信号。

- **Observer（观察者）**：订阅Observable的对象，当Observable发射数据、错误或完成信号时，Observer会收到相应的通知。

- **Operator（操作符）**：用于对数据流进行转换、过滤、组合等操作，如map、filter、reduce、flatMap等。

- **Scheduler（调度器）**：控制数据流在哪个线程或队列上执行。

响应式编程的主要优点：

- **声明式**：通过组合操作符来表达数据转换逻辑，代码简洁易读
- **异步友好**：天然支持异步操作，简化异步编程复杂性
- **错误处理**：提供统一的错误处理机制
- **背压（Backpressure）**：支持背压策略，防止数据流过载
- **时间操作**：方便处理超时、节流、防抖等时间相关操作

常见的响应式编程框架：

| 框架 | 语言 | 应用场景 |
|------|------|----------|
| ReactiveCocoa | Objective-C/Swift | iOS/macOS开发 |
| RxSwift | Swift | iOS开发 |
| RxJava | Java | Android开发 |
| RxJS | JavaScript/TypeScript | 前端开发 |
| Project Reactor | Java | Spring生态 |


### 7、声明式编程

**声明式编程** 是一种与命令式编程相对应的编程范式，强调描述"做什么"而不是"怎么做"。在声明式编程中，我们只需要描述期望的结果或规则，而不需要显式指定执行步骤。

声明式编程的主要特点：

- **专注于结果**：描述期望的结果，而非实现步骤
- **更高抽象层次**：隐藏底层实现细节
- **更好可读性**：代码表达"做什么"，更易理解
- **更好可维护性**：减少副作用，代码更易推理

声明式编程的典型应用：

- **SQL**：描述查询什么数据，不关心遍历过程
- **函数式编程**：Haskell、Erlang等
- **配置管理**：Dockerfile、Kubernetes配置
- **现代UI框架**：SwiftUI、ArkUI、Flutter、React

声明式编程代表了现代软件开发的重要趋势，使开发者更专注于业务逻辑表达。


### 总结

表现层架构模式经历了从MVC到MVVM、从Flux到Redux的演进过程。每种模式都有其适用场景和优缺点：

- **MVC**：经典模式，适合小型应用
- **MVP**：改进了测试性，适合中型应用
- **MVVM**：数据绑定强大，适合大型应用
- **VIPER**：职责最细，适合超大型应用
- **Flux/Redux**：单向数据流，适合React生态
- **响应式编程**：数据流驱动，适合复杂异步场景
- **声明式编程**：未来趋势，代表UI开发方向

在实际项目中，需要根据应用规模、团队经验、技术栈等因素选择合适的架构模式，有时甚至需要组合使用多种模式。
