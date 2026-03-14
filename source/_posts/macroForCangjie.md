---
title: 仓颉-宏
categories: 仓颉
---

## 宏的简介

宏可以理解为一种特殊的函数。一般的函数在输入的值上进行计算，然后输出一个新的值，而宏的输入和输出都是程序本身。在输入一段程序（或程序片段，例如表达式），输出一段新的程序，这段输出的程序随后用于编译和执行。为了把宏的调用和函数调用区分开来，我们在调用宏时使用 @ 加上宏的名称。

让我们从一个简单的例子开始：假设我们想在调试过程中打印某个表达式的值，同时打印出表达式本身。

```
let x = 3
let y = 2
@dprint(x)        // 打印 "x = 3"
@dprint(x + y)    // 打印 "x + y = 5"
```

显然，dprint 不能被写为常规的函数，由于函数只能获得输入的值，不能获得输入的程序片段。但是，我们可以将 dprint 实现为一个宏。一个基本的实现如下：
```
macro package define

import std.ast.*

public macro dprint(input: Tokens): Tokens {
    let inputStr = input.toString()
    let result = quote(
        print($(inputStr) + " = ")
        println($(input)))
    return result
}
```
在解释每行代码之前，我们先测试这个宏可以达到预期的效果。首先，在当前目录下创建一个 macros 文件夹，并在 macros 文件夹中创建 dprint.cj 文件，将以上内容复制到 dprint.cj 文件中。另外在当前目录下创建 main.cj，包含以下测试代码：
```
import define.*

main() {
    let x = 3
    let y = 2
    @dprint(x)
    @dprint(x + y)
}
```
请注意，得到的目录结构如下：
```
// Directory layout.
src
|-- macros
|     `-- dprint.cj
`-- main.cj
```
在当前目录（src）下，运行编译命令：
```
cjc macros/*.cj --compile-macro
cjc main.cj -o main
```
然后运行 ./main，可以看到如下输出：
```
x = 3
x + y = 5
```
让我们依次查看代码的每个部分：

- 第 1 行：macro package define

  宏必须声明在独立的包中（不能和其他 public 函数一起），含有宏的包使用 macro package 来声明。这里我们声明了一个名为 define 的宏包。

- 第 2 行：import std.ast.*

  实现宏需要的数据类型，例如 Tokens 和后面会讲到的语法节点类型，位于仓颉标准库的 ast 包中，因此任何宏的实现都需要首先引入 ast 包。

- 第 3 行：public macro dprint(input: Tokens): Tokens

  在这里我们声明一个名为 dprint 的宏。由于这个宏是一个非属性宏（之后我们会解释这个概念），它接受一个类型为 Tokens 的参数。该输入代表传给宏的程序片段。宏的返回值也是一个程序片段。

- 第 4 行：let inputStr = input.toString()

  在宏的实现中，首先将输入的程序片段转化为字符串。在前面的测试案例中，inputStr 成为 "x" 或 "x + y"

- 第 5-7 行：let result = quote(...)

  这里 quote 表达式是用于构造 Tokens 的一种表达式，它将括号内的程序片段转换为 Tokens。在 quote 的输入中，可以使用插值 $(...) 来将括号内的表达式转换为 Tokens，然后插入到 quote 构建的 Tokens 中。对于以上代码，$(inputStr) 插入 inputStr 字符串的值（包含字符串两端的引号），$(input) 插入 input，即输入的程序片段。因此，如果输入的表达式是 x + y，那么形成的Tokens为：
```
print("x + y" + " = ")
println(x + y)
```
- 第 8 行：return result

  最后，我们将构造出来的代码返回，这两行代码将被编译，运行时将输出 x + y = 5。

回顾 dprint 宏的定义，我们看到 dprint 使用 Tokens 作为入参，并使用 quote 和插值构造了另一个 Tokens 作为返回值。为了使用仓颉宏，我们需要详细了解 Tokens、quote 和插值的概念，下面我们将分别介绍它们。

## Tokens 相关类型和 quote 表达式

### Token 类型

宏操作的基本类型是 Tokens，代表一个程序片段。Tokens 由若干个 Token 组成，每个 Token 可以理解为用户可操作的词法单元。一个 Token 可能是一个标识符（例如变量名等）、字面量（例如整数、浮点数、字符串）、关键字或运算符。每个 Token 包含它的类型、内容和位置信息。

Token 的类型取值为 enum TokenKind 中的元素。TokenKind 的可用值详见《仓颉编程语言库 API》文档。通过提供 TokenKind 和（对于标识符和字面量）Token 的字符串，可以直接构造任何 Token。具体的构造函数如下：
```
Token(k: TokenKind)
Token(k: TokenKind, v: String)
```
下面给出一些Token构造的例子：
```
import std.ast.*

let tk1 = Token(TokenKind.ADD)   // '+'运算符
let tk2 = Token(TokenKind.FUNC)   // func关键字
let tk3 = Token(TokenKind.IDENTIFIER, "x")   // x标识符
let tk4 = Token(TokenKind.INTEGER_LITERAL, "3")  // 整数字面量
let tk5 = Token(TokenKind.STRING_LITERAL, "xyz")  // 字符串字面量
```

### Tokens 类型
一个 Tokens 代表由多个 Token 组成的序列。我们可以通过 Token 数组直接构造 Tokens。下面是 3 种基本的构造 Tokens 实例的方式：
```
Tokens()   // 构造空列表
Tokens(tks: Array<Token>)
Tokens(tks: ArrayList<Token>)
```
此外，Tokens 类型支持以下函数：

- size：返回 Tokens 中包含 Token 的数量
- get(index: Int64)：获取指定下标的 Token 元素
- []：获取指定下标的 Token 元素
- +：拼接两个 Tokens，或者直接拼接 Tokens 和 Token
- dump()：打印包含的所有 Token，供调试使用
- toString()：打印 Tokens 对应的程序片段
  
在下面的案例中，我们使用构造函数直接构造 Token 和 Tokens，然后打印详细的调试信息：
```
let tks = Tokens(Array<Token>([
    Token(TokenKind.INTEGER_LITERAL, "1"),
    Token(TokenKind.ADD),
    Token(TokenKind.INTEGER_LITERAL, "2")
]))
println(tks)
tks.dump()
```
预期输出如下（具体的位置信息可能不同）：
```
1 + 2
description: integer_literal, token_id: 139, token_literal_value: 1, fileID: 108, line: 79, column: 9
description: add, token_id: 12, token_literal_value: +, fileID: 108, line: 80, column: 9
description: integer_literal, token_id: 139, token_literal_value: 2, fileID: 108, line: 81, column: 9
```
在 dump 信息中，包含了每个 Token 的类型（description）和值（token_literal_value），最后打印每个 Token 的位置信息。

### quote 表达式和插值
在大多数情况下，直接构造和拼接 Tokens 会比较繁琐。因此，仓颉语言提供了 quote 表达式来从代码模版来构造 Tokens。之所以说是代码模版，因为在 quote 中可以使用 $(...) 来插入上下文中的表达式。插入的表达式的类型需要支持被转换为 Tokens（具体来说，实现了 ToTokens 接口）。在标准库中，以下类型实现了 ToTokens 接口：

- 所有的节点类型（节点将在语法节点中讨论）
- Token 和 Tokens 类型
- 所有基础数据类型：整数、浮点数、Bool、Rune和String
- Array<T> 和 ArrayList<T>，这里对 T 的类型有限制，并根据 T 的类型不同，输出不同的分隔符，详细请见《仓颉编程语言库 API》文档。
  
下面的例子展示 Array 和基础数据类型的插值。
```
let intList = Array<Int64>([1, 2, 3, 4, 5])
let float: Float64 = 1.0
let str: String = "Hello"
let tokens = quote(
    arr = $(intList)
    x = $(float)
    s = $(str)
)
println(tokens)
```
输出结果是：
```
arr =[1, 2, 3, 4, 5]
x = 1.000000
s = "Hello"
```
更多插值的用法可以参考 `使用 quote 插值语法节点`。

## 语法节点

## 宏的实现

## 编译、报错与调试

## 宏包定义和导入

## 内置编译标记
