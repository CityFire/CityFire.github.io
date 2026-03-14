---
title: CMake 入门实战
---

## 什么是 CMake
```
All problems in computer science can be solved by another level of indirection.

- David Wheeler
```
你或许听过好几种 Make 工具，例如 `GNU Make` ，QT 的 `qmake` ，微软的 `MS nmake`，BSD Make（`pmake`），`Makepp`，等等。这些 Make 工具遵循着不同的规范和标准，所执行的 Makefile 格式也千差万别。这样就带来了一个严峻的问题：如果软件想跨平台，必须要保证能够在不同平台编译。而如果使用上面的 Make 工具，就得为每一种标准写一次 Makefile ，这将是一件让人抓狂的工作。

CMake 就是针对上面问题所设计的工具：它首先允许开发者编写一种平台无关的 CMakeList.txt 文件来定制整个编译流程，然后再根据目标用户的平台进一步生成所需的本地化 Makefile 和工程文件，如 Unix 的 Makefile 或 Windows 的 Visual Studio 工程。从而做到“Write once, run everywhere”。显然，CMake 是一个比上述几种 make 更高级的编译配置工具。一些使用 CMake 作为项目架构系统的知名开源项目有 `VTK`、`ITK`、`KDE`、`OpenCV`、`OSG` 等 `[1]`。

在 linux 平台下使用 CMake 生成 Makefile 并编译的流程如下：

1.编写 CMake 配置文件 CMakeLists.txt 。
2.执行命令 `cmake PATH` 或者 `ccmake PATH` 生成 Makefile（`ccmake` 和 `cmake` 的区别在于前者提供了一个交互式的界面）。其中， `PATH` 是 CMakeLists.txt 所在的目录。
3.使用 `make` 命令进行编译。

## 入门案例：单个源文件
对于简单的项目，只需要写几行代码就可以了。例如，假设现在我们的项目中只有一个源文件 `main.cc` ，该程序的用途是计算一个数的指数幂。
```
#include <stdio.h>
#include <stdlib.h>

/**
 * power - Calculate the power of number.
 * @param base: Base value.
 * @param exponent: Exponent value.
 *
 * @return base raised to the power exponent.
 */
double power(double base, int exponent)
{
    int result = base;
    int i;
    
    if (exponent == 0) {
        return 1;
    }
    
    for(i = 1; i < exponent; ++i){
        result = result * base;
    }

    return result;
}

int main(int argc, char *argv[])
{
    if (argc < 3){
        printf("Usage: %s base exponent \n", argv[0]);
        return 1;
    }
    double base = atof(argv[1]);
    int exponent = atoi(argv[2]);
    double result = power(base, exponent);
    printf("%g ^ %d is %g\n", base, exponent, result);
    return 0;
}
```
## 编写 CMakeLists.txt
首先编写 CMakeLists.txt 文件，并保存在与 `main.cc` 源文件同个目录下：

```
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (Demo1)

# 指定生成目标
add_executable(Demo main.cc)
```
CMakeLists.txt 的语法比较简单，由命令、注释和空格组成，其中命令是不区分大小写的。符号 `#` 后面的内容被认为是注释。命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。

对于上面的 CMakeLists.txt 文件，依次出现了几个命令：

1.`cmake_minimum_required`：指定运行此配置文件所需的 CMake 的最低版本；
2.`project`：参数值是 Demo1，该命令表示项目的名称是 `Demo1` 。
3.`add_executable`： 将名为 `main.cc` 的源文件编译成一个名称为 Demo 的可执行文件。

## 编译项目
之后，在当前目录执行 `cmake .` ，得到 Makefile 后再使用 `make` 命令编译得到 Demo1 可执行文件。

```
[wjc-MacBook-Pro Demo1]$ cmake .
-- The C compiler identification is GNU 4.8.2
-- The CXX compiler identification is GNU 4.8.2
-- Check for working C compiler: /usr/sbin/cc
-- Check for working C compiler: /usr/sbin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/sbin/c++
-- Check for working CXX compiler: /usr/sbin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ehome/Documents/programming/C/power/Demo1
[wjc-MacBook-Pro Demo1]$ make
Scanning dependencies of target Demo
[100%] Building C object CMakeFiles/Demo.dir/main.cc.o
Linking C executable Demo
[100%] Built target Demo
[wjc-MacBook-Pro Demo1]$ ./Demo 5 4
5 ^ 4 is 625
[wjc-MacBook-Pro Demo1]$ ./Demo 7 3
7 ^ 3 is 343
[wjc-MacBook-Pro Demo1]$ ./Demo 2 10
2 ^ 10 is 1024
```