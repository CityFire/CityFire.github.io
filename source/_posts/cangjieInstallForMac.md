---
title: 仓颉开发语言MAC版本安装
categories: [鸿蒙、仓颉]
---

## 仓颉编程语言通用版本开发环境搭建（以 MAC 平台为例）

### 下载 VScode 以及 仓颉语言 VScode 插件

IDE下载这里不做赘述，点击[仓颉语言 VScode 插件]((https://gitcode.com/Cangjie/CangjieVScodePlugin/overview))进入代码仓下载并解压缩
![](images/CangjieVScodePlugin.png)

### 下载仓颉编程语言通用版本SDK
点击[仓颉编程语言通用版本SDK（MAC）](https://gitcode.com/Cangjie/CangjieSDK-Darwin/overview) 进入代码仓下载并解压缩
![](images/CangjieSDKMac.png)

建议点击文件跳转页面后点击右上角下载按钮进行下载，或使用`git lfs clone https://gitcode.com/Cangjie/CangjieSDK-Darwin.git`进行下载。

### 仓库中压缩包介绍

克隆下来仓库后，里面有三个文件

README.md（不用管）
Cangjie-0.53.4-darwin_x64.tar.gz（英特尔芯片Mac 使用此SDK）
Cangjie-0.53.4-darwin_aarch64.tar.gz（M系列芯片Mac 使用此SDK）
解压 2 和 3 中的一个

#### 解压 SDK 文件
解压后的文件夹，里面有两个比较重要的文件夹

bin (里面有仓颉编译器可执行文件 cjc cjc-frontend)
tools/bin ( 里面有仓颉内置的工具：cjpm、cjlint、 cjdoc 等 )

```

# 查看编译器版本
./bin/cjc -v 
# 查看仓颉包管理工具 cjpm 版本
./tools/bin/cjpm -v

```

#### 全局安装可执行脚本
（编译器cjc 和 包管理工具cjpm 等）
如果你使用 zsh 则需要编辑 配置文件.zshrc，如果你使用bash 则需要编辑 配置文件.bashrc。

```
# 我使用的是zsh，.zshrc文件最底部加入两个代码
export PATH=${你解压后的仓颉文件路径}/bin:$PATH
export PATH=${你解压后的仓颉文件路径}/tools/bin:$PATH
```

重启终端的配置文件
```
source ~/.zshrc
```

#### 安装依赖
```
brew install libffi
```

#### 配置仓颉内置工具
```
source ${你的仓颉路径}/envsetup.sh
```

执行下面命令：

```
cjc -v
cjpm -v
```

![](images/CangjieShellEnv.png)

### 配置环境

解压Cangjie-vscode-0.53.4.tar.gz后的文件夹Cangjie-vscode-0.53.4中选择Cangjie-0.53.4.vsix文件，如下图操作。
![](images/CangjieVSCodeInstallFromDisk.png)

![](images/CangjieVSCodeIDE.png)


### 初始化工程
`Command + Shift + P` 打开VScode功能搜索栏，输出 `Cangjie`，选择 `Create Cangjie Project`

根据提示初始化仓颉项目（`CJNative`），如下图名为 `CangjieDemo` 的仓颉工程

![](images/CangjieVScodeCodeExample.png)


### 编译运行
右上角三角按钮编译运行，或使用`cjpm run`运行