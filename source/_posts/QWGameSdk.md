---
title: QWGameSdk For iOS开发手册
---

# QWGameSdk For iOS开发手册
## 对接内容更新
```
<table>
  <tr>
      <td>2018.01.29</td>
      <td>QWGameSdk v2.0.0：更改SDK界面；增加游客模式</td>
  </tr>
  <tr>
      <td>2018.02.05</td>
      <td>QWGameSdk v2.0.1：增加SDK所需依赖库；QWGameConfig增加设备状态栏显示隐藏设置；bug fix</td>
  </tr>
  <tr>
  <td>2018.07.16</td>
  <td>QWGameSdk v2.0.2：智齿更新、适配；界面调整；bug fix</td>
  </tr>
</table>
```

## 一.开发环境搭建

SDK支持iOS7.0以上系统，支持armv7,armv7s,arm64架构。

### 1.导入QWGameSdk工程

#### 1.1 把Release-fat文件夹拖入工程，包含
	QWGameSdk.framework
	QWGameSdkResources.bundle
	SobotKit.bundle
	
#### 1.2 若项目无法找到framework文件，工程设置里面需要添加.framework文件所在路径(Build Settings->Search Paths->Framework Search Paths)，以Demo为例
	$(PROJECT_DIR)/../Release-fat
	
### 2.工程设置里面需要添加以下依赖库(General->Linked Frameworks and Libraries)
	QWGameSdk.framework	(此framework为TT方提供)
	AdSupport.framework
	CoreData.framework
	Photos.framework
	StoreKit.framework
	CoreMotion.framework
	AVFoundation.framework
	MobileCoreServices.framework
	SystemConfiguration.framework
	AudioToolbox.framework
	AssetsLibrary.framework
	libsqlite3.0.tbd
	libz.tbd
	libz.1.2.5.tbd
	libstdc++.tbd
	
### 3.工程设置里面进行Other Linker Flags设置(Build Settings->linking->Other Linker Flags)
	通常情况下，只需添加-ObjC参数即可。
	
	注：若仍然出现"unrecognized selector sent to instance"，且归因于SDK，则使用-force_load。以Demo为例
	-force_load $(PROJECT_DIR)/../Release-fat/QWGameSdk.framework/QWGameSdk
	
### 4.工程设置里面进行Enable Bitcode设置(Build Settings->Build Options->Enable Bitcode)
	设置Enable Bitcode为No。
	
### 5.配置 info.plist
使用包含您的应用数据的 XML 代码段配置信息属性列表文件（info.plist）。 右键点击 info.plist，然后选择 Open As Source Code（作为源代码打开）。

#### 5.1 配置LSApplicationQueriesSchemes白名单
	<key>LSApplicationQueriesSchemes</key>
	<array>
  		<string>tt</string>
  		<string>weixin</string>
  		<string>alipay</string>
  		<string>alipays</string>
	</array>
	
#### 5.2 配置NSAppTransportSecurity,允许APP进行HTTP请求
	<key>NSAppTransportSecurity</key>
	<dict>
	<key>NSAllowsArbitraryLoads</key>
	<true/>
	</dict>

#### 5.3 配置相关访问权限（相册、相机、麦克风）
注意：NSPhotoLibraryAddUsageDescription为iOS 11新特性

	<key>NSPhotoLibraryUsageDescription</key>
	<string>使用相册保存图片</string>
	<key>NSPhotoLibraryAddUsageDescription</key>
	<string>使用相册保存图片</string>
	<key>NSCameraUsageDescription</key>
	<string>访问相机</string>
	<key>NSMicrophoneUsageDescription</key>
	<string>访问麦克风</string>


## 二:API具体应用说明
### 1.QWGameSdk.h 
QWGameSdk.h已经#import其他公开头文件,您只需要#import\<QWGameSdk/QWGameSdk.h>即可。

### 2.QWGameConfig.h
SDK配置Model类，用于初始化时传入
#### 属性说明
	@property (nonatomic, assign) UInt32 gameId;// TT后台分配给游戏的ID
	@property (nonatomic, strong) NSString * gameKey;// TT后台分配给游戏的gameKey(SDK交互秘钥)
	@property (nonatomic, copy) NSString *trackAppKey;// TT后台分配给游戏的热云appKey(注:越狱包无需热云appKey，请传nil)
	@property (nonatomic, assign) BOOL sdkCanLogout;// 是否允许SDK退出账号，默认允许
	@property (nonatomic, assign) QWGameSupportedOrientation supportedOrientation;// 游戏支持的屏幕方向，默认横屏（该设置将会影响SDK中相关UI适配）
	@property (nonatomic, assign) BOOL showStatusBar;// 是否显示设备状态栏(即设备顶部信号、时间、电量状态栏)，默认不显示
	
### 3.QWGameManager.h
通常API类(初始化、登录、退出、支付)

#### 3.1 属性说明
	@property (nonatomic, strong) QWGameConfig *gameConfig;// 初始化时传入的配置对象
	@property(nonatomic, weak) id<QWGameManagerDelegate> delegate;// SDK回调代理(请对其赋值，否则为nil)

#### 3.2 QWGameManagerDelegate协议说明
QWGameSdk执行完部分操作后，给游戏进行的回调。注:请自行配置 [QWGameManager sharedInstance].delegate = “delegate”;
##### 3.2.1 登錄成功回調
	- (void)didLoginSuccessfullyWithUid:(UInt32)uid sessionString:(NSString *)sessionString;
##### 3.2.2 切換賬號成功回調
	- (void)didLogoutSuccessfullyWithUid:(UInt32)uid;
##### 3.2.3 支付回調
	- (void)ttZFCallBackWithResult:(QWGameManagerPayResult)result orderId:(NSString *)orderId;

#### 3.3 函数说明
##### 3.3.1 QWGameManager单例
	+ (instancetype)sharedInstance;
##### 3.3.2 AppDelegate生命周期函数 初始化
	- (BOOL)applicationDidFinishLaunchingWithGameConfig:(QWGameConfig *)gameConfig;
###### 代码示例
```
	- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    	QWGameConfig *gameConfig = [[QWGameConfig alloc] init];
    	gameConfig.gameId = CustomGameID;
    	gameConfig.gameKey = CustomGameKey;
    	// gameConfig.trackAppKey = @"3c265e0399ecfa5a67b1b36c126e9da4";// 越狱无需设置。
    	gameConfig.supportedOrientation = QWGameSupportedOrientationPortrait;
    	[[QWGameManager sharedInstance] applicationDidFinishLaunchingWithGameConfig:gameConfig];
    	return YES;
	}
```
##### 3.3.3 调起登录頁面
	- (void)login;
##### 3.3.4 注销
游戏主动注销时，请调用该方法

	- (void)logout;
##### 3.3.5 显示悬浮球
	+ (void)showSuspensionView;
##### 3.3.6 隐藏悬浮球
	+ (void)hideSuspensionView;
##### 3.3.7 支付
	- (void)payForGood:(CGFloat)price
          serverId:(NSInteger)serverId
          orderStr:(NSDictionary*)ordInfo;
###### 参数说明
```
	price:			价格
 	serverId:		游戏服务器ID
 	ordInfo:		订单参数,详见以下的"订单参数"字段
####### 订单参数

	static NSString* const kKeyCpOrderId        = @"cpOrderId";     //订单号,必选
	static NSString* const kKeyProductId        = @"productId";     //appStore商品id(越狱端无需此参数)
	static NSString* const kKeySubject          = @"subject";       //商品名称
	static NSString* const kKeyBody             = @"body";          //商品描述
	static NSString* const kKeyExInfo           = @"exInfo";        //扩展信息
	static NSString* const kRespKeyCpCallbackUrl= @"cpCallbackUrl"; //支付回调地址
```
##### 3.3.8 获取渠道名称
 	- (NSString *)getChannelName;

### 4.QWGameTracking.h
#### 函数说明
##### 开启SDK事件跟踪打印日志
	+ (void)setPrintLog:(BOOL)print;
##### 提交角色数据
	+ (void)submitGameRoleInfoWithAction:(QWGameRoleInfoAction)action
                            serverId:(NSInteger)serverId
                          serverName:(NSString *)serverName
                              roleId:(NSString *)roleId
                            roleName:(NSString *)roleName
                           roleLevel:(int)roleLevel
                            vipLevel:(NSString *)vipLevel
                               power:(long)power
                          roleExInfo:(nullable NSDictionary *)roleExInfo;
###### 参数说明
	action: 		角色信息提交的场景
	serverId: 		服务器ID
	serverName: 	服务器名称
	roleId: 		角色ID
	roleName: 		角色名称
	roleLevel: 		角色等级
	vipLevel: 		vip等级
	power: 			角色战力值
	roleExInfo: 	角色扩展参数(可为空)


## 三:接入注意
### 1.横竖屏注意
若游戏同时支持横竖屏，建议在根ViewController内添加以下方法

	- (BOOL)shouldAutorotate
	{
    	return NO;
	}
	
### 2.文件冲突 duplicate symbol
参考 https://www.jianshu.com/p/c7274dca62f7

补充，针对我们的静态framework，请解QWGameSdk.framework/QWGameSdk

### 3.登录出现闪退
1）若使用Quick，可能是重复引用sdk导致。可尝试不引用此sdk，详细咨询Qucik技术。

2）sdk会使用[[[UIApplication sharedApplication] delegate] window]。检查此时游戏[[UIApplication sharedApplication] delegate]是否有window，且不为nil。(可以尝试把window变量，更改为强引用的属性。)
