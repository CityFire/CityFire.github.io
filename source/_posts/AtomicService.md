---
title: HarmonyOS元服务
categories: [鸿蒙]
---

## 元服务概述

### 什么是元服务

在万物互联时代，人均持有设备量不断攀升，设备种类和使用场景更加多样，使得应用开发、应用入口变得更加复杂。在此背景下，应用提供方和用户迫切需要一种新的服务提供方式，使应用开发更简单、服务（如听音乐、打车等）的获取和使用更便捷。为此，HarmonyOS除支持传统的需要安装的应用（以下简称传统应用）外，还支持更加方便快捷的免安装的应用，即元服务。

元服务是HarmonyOS提供的一种轻量应用程序形态，具备服务直达、跨设备等特征。

元服务可独立上架、分发、运行，独立实现业务闭环，可大幅提升信息与服务的获取效率。

元服务基于HarmonyOS SDK（只能使用“[元服务API集](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/development-intro-api-V5)”）开发，支持运行在1+8+N设备上，供用户在合适的场景、合适的设备上便捷使用。

元服务的设计原则及规范，请查看[元服务设计指导](https://developer.huawei.com/consumer/cn/doc/design-guides-V1/service-overview-0000001139795693-V1)。

元服务与传统应用的对比请见下表。

**表1** 元服务与传统应用对比

区别 | 特征 | 载体 | API范围 | 经营
:--- |:--- |:--- |:--- |:---
传统应用 | 手动下载安装</br> 包大小无限制</br> 按需使用</br> 应用内或应用市场更新</br> 功能齐全，开发成本高，周期长 | 跟随设备 | 全量API | 自主运营</br> 人找应用成本高
元服务 | 免安装</br> 包大小有限制</br> 即用即走</br> 自动更新</br> 轻量化完整功能，开发成本较低 | 跟随华为帐号 | 只能使用“元服务API集” | 支付、地图、广告等经营履约能力辅助经营</br> 负一屏等系统分发入口帮助人找服务、服务找人


开发者基于经营目标、效率、成本、收益等因素，自主决定开发传统应用或元服务，也可以同时提供。

从应用程序入口看，下图展示了元服务与传统应用、服务卡片之间的关系。对于传统应用和元服务，均可选择服务卡片作为入口。

**图1** 元服务与传统应用、服务卡片之间的关系

![](images/atomicService.png)

元服务在开发态和运行态的基本视图如下图所示。

**图2** 元服务视图
![](images/atomicServiceView.png)

### 元服务特征及使用场景

元服务区别于传统应用，具备如下特征。

- 服务直达
   - 元服务支持免安装使用。
   - 服务卡片：支持用户无需打开元服务便可获取服务内重要信息的展示和动态变化，如天气、关键事务备忘、热点新闻列表等。
- 跨设备
   - 元服务支持运行在1+8+N设备上，如手机、平板、2in1、智慧屏等设备。
   - 支持跨设备分享：用户可分享元服务给好友，好友确认后打开分享的服务。
基于上述特征，元服务的典型使用场景如下。

**1.常用服务卡片添加到桌面，体验快捷服务**
例如：将常用的天气、备忘录及热点新闻列表等服务卡片添加到桌面上，解锁手机即可在桌面上查看即时信息。

同时，通过负一屏发现服务卡片，无需安装即可使用热点服务卡片。

**2.释放手机，让用户在更合适的设备上享受服务**
例如：打车是人们日常生活中经常使用的服务，通常人们在手机上打车，需要一直停留在手机界面才能准确获取司机的状态信息。

有了元服务的分布式能力，在手机打车后，将司机状态实时同步到手表，无需查看手机，抬腕即可获取司机状态。

### 元服务程序包基础知识

元服务的程序包结构与传统[应用程序包](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/application-package-structure-stage-V5)相同，也是以App Pack（.app）形式发布到应用市场。

但元服务相对于需要安装的应用形态更加轻量、便捷，其程序包也具备一些独有特征，如免安装、分包、预加载、老化。

#### 免安装
免安装是指无需用户通过应用市场显式安装，用户点击元服务后，由系统程序框架后台安装后即可使用。

元服务中所有包HAP（Harmony Ability Package）、HSP（Harmony Shared Package）均需支持免安装。

#### 分包
HarmonyOS每个应用程序包（.app）可以包含多个包文件（以.hap为后缀的HAP或以.hsp为后缀的HSP）。元服务在此基础上，进一步限制每个HAP或HSP（含其依赖的所有共享包）的大小，以实现快速启动体验，元服务的这种多包开发方案称为“分包”。

具体的分包规格：

- 首包：将Entry HAP作为首包，包含元服务首次启动时会打开的页面（即首页）代码和资源。
- 分包：将其他包含功能页的模块以及HSP动态共享模块作为分包，包含功能页和元服务依赖的代码和资源。
- 单个包文件（加上其依赖的所有共享包），大小不能超过2MB，超过限制DevEco Studio会打包失败。
- 同一个元服务下所有包文件（加上其依赖的所有共享包）的大小总和不能超过10MB，超过限制DevEco Studio会打包失败。如因业务需要，可向平台申请总包大小放宽至20M。

这样，启动元服务时，只需下载和安装首包，即可立即启动元服务，大大缩短元服务启动时间。

**图1** 采用分包的元服务开发态视图

![](images/atomicServiceA.png)

分包建议：

- 单个HAP或HSP（加上其依赖的所有共享包）大小超过2M，就需要考虑分包。
- 建议开发者按照不同的功能进行分包。
- 重复代码和资源抽离出来作为HSP，进一步减小包大小。

下图展示了一个元服务的开发态视图，该元服务具有：

- 一个名为HomeModule的首包模块
- 一个名为FeatureModule的分包模块
- 一个名为SharedLibraryModule的HSP动态共享模块
- 一个名为StaticLibraryModule的静态共享模块

**图2** 元服务分包的工程目录结构图
![](images/atomicServiceProject.png)

- 其中HomeModule模块为元服务的“首包”，type字段为entry，以下是HomeModule模块的module.json5文件：
```
{  
  "module": {
    "name": "HomeModule",
    "type": "entry",
    "pages": "$profile:main_pages",    
    ...
  }
}
```
- FeatureModule模块为功能页“分包”，type字段为feature，以下是FeatureModule模块的module.json5文件：
```
{  
  "module": {
    "name": "FeatureModule",
    "type": "feature",
    ...
  }
}
```
- SharedLibraryModule模块为共享“分包”，type字段为shared，以下是SharedLibraryModule模块的module.json5文件：
```
{  
  "module": {
    "name": "SharedLibraryModule",
    "type": "shared",
    ...
  }
}
```
- StaticLibraryModule模块为静态共享包，type字段为har，以下是StaticLibraryModule模块的module.json5文件：
```
{  
  "module": {
    "name": "StaticLibraryModule",
    "type": "har",
    ...
  }
}
```

#### 预加载
开发者可以通过配置预加载，由系统自动下载和安装可能需要的分包模块，从而提升进入后续模块的速度。

对于配置了预加载的分包模块，当点击进入该模块并完成页面加载后，将触发关联模块的预加载。

#### 配置预加载
预加载在相应分包模块[module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/module-configuration-file-V5)配置文件中“atomicService”标签下的preloads字段配置。以HomeModule模块的module.json5为例：

```
{  
  "module": {
    "name": "HomeModule",
    "type": "entry",
    "installationFree": true,
    "pages": "$profile:main_pages",
    "atomicService": {
      "preloads": [
        {
          "moduleName": "FeatureModule"
        }
      ]
    },
    ...
  }
}
```
在HomeModule模块的页面加载结束后，系统会自动执行预加载，去下载和安装模块名为FeatureModule的模块。

```
注意
preloads列表配置的moduleName对应的ModuleType（模块类型）不能为entry。
```

#### 老化
系统会按照一定策略清理不活跃的元服务，释放空间，这个过程称为老化。具体老化机制如下。

- 老化时机：由系统定时器触发老化，当系统中所有元服务占用总空间大于既定阈值时，将启动老化，同时要求设备处于熄屏状态，且剩余电量不低于10%。
- 老化顺序：优先老化长时间未使用及使用频率较低且未添加桌面卡片的元服务。
- 分级老化：根据数据重要性排序，分级老化。当系统满足老化时机的要求时，按照老化顺序优先清理元服务的Cache目录数据，再按照老化顺序清理元服务的其他目录数据，直到系统中所有元服务占用总空间小于既定阈值的80%。因此，开发者应合理规划数据存放目录，仅将非重要数据（例如网络缓存图片等）存放到Cache目录，避免重要数据被频繁老化清理。
**图3** 元服务老化示意图
![](images/atomicServiceOld.png)

#### 元服务程序包更新机制
元服务在重新加载启动时（首次打开或销毁后被用户再次打开），会异步检查是否有更新版本。如果发现有新版本，将会异步下载新版本的程序包。但当次启动仍会使用客户端本地的旧版本程序，新版本的元服务将在下一次重新加载启动时使用。


### 元服务开发旅程

元服务的开发旅程如下图所示。

**图1** 元服务开发旅程
![](images/atomicServiceDev.jpg)

元服务开发主要包括以下环节。

- 开发前
创建元服务项目前，需要[注册华为开发者帐号](https://developer.huawei.com/consumer/cn/doc/distribution/service/fa-registe-0000001491834888)并[创建您的元服务](https://developer.huawei.com/consumer/cn/doc/distribution/service/fa-create-app-0000001491994788)；然后[搭建开发环境](https://developer.huawei.com/consumer/cn/doc/atomic-guides-V5/atomic-service-start-overview-V5#%E5%B7%A5%E5%85%B7%E5%87%86%E5%A4%87)，通过DevEco Studio[创建元服务工程](https://developer.huawei.com/consumer/cn/doc/atomic-guides-V5/atomic-service-create-project-V5)。
```
说明
元服务包名命名格式需要使用com.atomicservice.[appid]，请先在网站创建元服务，获取AppID后再创建工程。

在AGC网站上，可以通过“我的元服务”选择对应元服务，在“应用信息”可查询元服务的appid。
```
- 开发中
元服务包含页面和卡片两个部分，请参考[UI开发](https://developer.huawei.com/consumer/cn/doc/atomic-guides-V5/atomic-ui-development-V5)和[服务卡片开发](https://developer.huawei.com/consumer/cn/doc/atomic-guides-V5/atomic-widget-development-V5)。

DevEco Studio提供[真机调试](https://developer.huawei.com/consumer/cn/doc/atomic-guides-V5/atomic-running-debugging-V5)能力，开发者可快速通过真机运行调试查看运行效果。

- 打包
可通过DevEco Studio快速[打包生成发布版本](https://developer.huawei.com/consumer/cn/doc/service/fa-packing-release-version-0000001557779433)，使用此版本，可以用于开放式测试或提交上架审核。

- 测试
在正式发布元服务前，您可以发布一个[开放式测试版本](https://developer.huawei.com/consumer/cn/doc/service/fa-open-test-0000001542634933)，邀请部分用户提前体验新版本，并收集用户的反馈，以便提前发现问题进行改进，从而保证全网版本的质量，提升用户体验。

- 上架
当元服务经过全面测试，确保版本没有问题，即可[发布正式版本](https://developer.huawei.com/consumer/cn/doc/service/fa-official-release-0000001491515152)。


