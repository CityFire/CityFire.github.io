---
title: 从SwiftUI降级到UIKit的痛苦根源
tags: [iOS, SwiftUI, UIKit, Objective-C]
---

今年用惯了SwiftUI的声明式思想，现在的公司又用回了UIKit的命令式思想，还是Objective-C的元老编程语言。这种感觉就像是开惯了在高速公路上自动驾驶的智能汽车，突然让你回到上世纪90年代手动挡的桑塔纳——你不仅要自己控制方向，还要自己踩油门、换挡，甚至有时候还得自己推车。

## 声明式 vs 命令式：两种编程范式的鸿沟

SwiftUI采用声明式编程，你只需要告诉系统"我要什么样的界面"，而不是"怎么去实现这个界面"。数据变了，界面自动跟着变。这种感觉就像是在写一篇作文——你描述你想要的结果，编译器帮你搞定一切。

UIKit则是命令式的典型代表。你需要手动管理每一个UI元素的生命周期，创建、添加、删除、布局——一切都得亲力亲为。这感觉就像是在玩一盘复杂的棋局，每走一步都要考虑全局。

## 那些让人崩溃的瞬间

### 1. 状态管理的噩梦

在SwiftUI里，一个`@State`变量搞定一切。按钮点击？修改状态，视图自动刷新。数据来了？更新状态，界面自动渲染。

到了UIKit，你得自己实现`didSet`或者KVO，手动调用`setNeedsLayout()`和`layoutIfNeeded()`。有时候明明数据变了，界面却纹丝不动，你得反复检查是不是漏了哪个刷新方法。

```swift
// SwiftUI - 轻松写意
@State private var isLoading = false
var body: some View {
    Button("加载") {
        isLoading = true
    }
}
```

```objc
// UIKit + Objective-C - 繁琐不堪
- (void)startLoading {
    self.isLoading = YES;
    [self.loadingIndicator startAnimating];
    [self.tableView reloadData]; // 也许需要，也许不需要，看具体情况
}
```

### 2. Auto Layout的折磨

SwiftUI的布局系统简单直观：
```swift
VStack {
    Text("Hello")
    Image("icon")
}
.padding()
```

UIKit的Auto Layout需要写一堆约束代码，或者在Storyboard里点点点：
```objc
UIView *container = [[UIView alloc] init];
UILabel *label = [[UILabel alloc] init];
label.text = @"Hello";

[container addSubview:label];
label.translatesAutoresizingMaskIntoConstraints = NO;
[NSLayoutConstraint activateConstraints:@[
    [label.topAnchor constraintEqualToAnchor:container.topAnchor constant:16],
    [label.leadingAnchor constraintEqualToAnchor:container.leadingAnchor constant:16],
    // ... 更多约束
]];
```

每次写完约束，都要在真机上跑一遍，确认布局没有问题。这种"猜谜"式debugging，真是让人欲哭无泪。

### 3. 生命周期的复杂管理

SwiftUI的`onAppear`和`onDisappear`干净利落：
```swift
.onAppear {
    loadData()
}
.onDisappear {
    cancelRequest()
}
```

UIKit呢？你需要理解`viewDidLoad`、`viewWillAppear`、`viewDidAppear`、`viewWillDisappear`、`viewDidDisappear`、`viewDidUnload`——整整一套生命周期方法，每个都有特定的用途和副作用。稍有不慎，就会出现内存泄漏或者界面闪烁的问题。

### 4. 代理和数据源的困扰

SwiftUI和Combine配合，数据流单向清晰。UIKit的数据源和代理模式，需要你在各种回调方法里处理业务逻辑，一个不小心就是"回调地狱"。

```objc
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    
    DataItem *item = self.dataSource[indexPath.row];
    [self handleItemSelection:item];
    
    if (item.needsDetail) {
        DetailViewController *detail = [[DetailViewController alloc] initWithItem:item];
        detail.delegate = self;
        [self.navigationController pushViewController:detail animated:YES];
    }
}
```

这段代码看起来还算清晰，但想象一下一个复杂的页面有十几个代理方法，每个方法里都有业务逻辑，代码会变成什么样子。

## 额外的噩梦：Objective-C

如果说从SwiftUI到UIKit是"降级"，那么从Swift再到Objective-C简直是"穿越"。没有了可选类型的安全保障，没有了泛型的类型检查，没有了强大的闭包语法，一切都要靠手动管理内存（虽然有ARC，但心智负担依然很大）。

```objc
// Objective-C 的冗长
NSString *name = @"Tom";
NSInteger age = 25;
NSDictionary *person = @{@"name": name, @"age": @(age)};

for (NSString *key in person) {
    NSLog(@"Key: %@, Value: %@", key, person[key]);
}
```

对比Swift：
```swift
let name = "Tom"
let age = 25
let person = ["name": name, "age": age]

for (key, value) in person {
    print("Key: \(key), Value: \(value)")
}
```

每写一行Objective-C代码，都像是在提醒自己：这已经是21世纪了，为什么我还在用上世纪80年代的语法？

## 如何优雅地应对这种"降级"

既然无法改变工作环境，那就只能调整自己的心态和习惯了：

1. **接受现实**：不要试图用SwiftUI的思维去写UIKit，那只会让自己更痛苦
2. **建立规范**：给项目建立统一的代码规范，减少"随心所欲"带来的混乱
3. **封装复用**：把常用的UI操作封装成工具类或分类，减少重复代码
4. **善用工具**：使用Masonry、SnapKit等Auto Layout库，简化约束代码
5. **保持学习**：也许明天公司就全面转向SwiftUI了呢？

## 结语

从SwiftUI回到UIKit+Objective-C，确实是一件令人沮丧的事情。但这也许是一个机会——重新理解那些"被SwiftUI隐藏"的底层原理。当你对两者的差异有了深刻理解后，你会发现：无论哪种框架，核心的编程思想都是相通的。

也许在若干年后回头看，这段"复古"的经历，会成为你职业生涯中一笔独特的财富。
