---
date: 2025-07-05 13:12:51
title: Core Bluetooth框架详解
tags:
  - iOS
  - Bluetooth
  - CoreBluetooth
  - BLE
categories: iOS开发
---

> 说起这个蓝牙框架，就想起我在大四暑假的时候，在广州一家小型创业公司，里面的同事几乎都是华南农业大学的，因为三个合伙人就是华农毕业的，公司买了一个单片机带蓝牙模块，然后打算使用单片机通过蓝牙BLE 4.0协议和iPad通信实现一个乐谱翻页弹奏的功能。由于那时候刚接触iOS，蓝牙模块的使用我也只是在网上看了一些资料，然后我就开始研究它了，也开始了自己短暂的蓝牙开发之旅。现在在看鸿蒙的蓝牙模块，回过头来看看Core Bluetooth框架感觉几乎差不多一样的思路，查看文档时发现蓝牙服务发现连接配对时序图的步骤几乎一样。

## 一、BLE（蓝牙低功耗）概述

### 1.1 什么是BLE

**BLE (Bluetooth Low Energy)** 是蓝牙4.0规范中引入的一种低功耗无线通信技术。与传统蓝牙（BR/EDR）相比，BLE专注于低功耗和短距离通信，特别适合需要电池供电的物联网设备。

### 1.2 BLE核心特性

| 特性 | 说明 |
|------|------|
| **工作频段** | 2.4 GHz ISM频段（无需许可） |
| **调制方式** | GFSK (高斯频移键控) |
| **信道数量** | 40个RF信道（3个广播信道 + 37个数据信道） |
| **传输速率** | 最高2 Mbps（实际约1.37 Mbps考虑开销） |
| **传输距离** | 通常在100米以内 |
| **地址长度** | 48位唯一标识符（公共地址或随机地址） |

### 1.3 BLE协议栈架构

```
┌─────────────────────────────────────────────────────┐
│                    应用层 (Applications)            │
├─────────────────────────────────────────────────────┤
│           GATT (通用属性配置文件)                     │
│  ┌─────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Services│  │Characteristics│  │ Descriptors  │  │
│  └─────────┘  └──────────────┘  └───────────────┘  │
├─────────────────────────────────────────────────────┤
│              ATT (属性协议)                          │
├─────────────────────────────────────────────────────┤
│           L2CAP (逻辑链路控制与适配协议)               │
├─────────────────────────────────────────────────────┤
│           HCI (主机控制器接口)                        │
├──────────────────────┬──────────────────────────────┤
│     链路层 (LL)      │      物理层 (PHY)             │
└──────────────────────┴──────────────────────────────┘
```

---

## 二、蓝牙常见名称和缩写

- **BLE**: (Bluetooth Low Energy) 蓝牙4.0设备因为低耗电，也叫BLE设备
- **Peripheral**: 外设，被连接的设备（如运动手环、传感器）
- **Central**: 中心设备，发起连接的设备（如手机、电脑）
- **Service**: 服务，一组特征的集合，类似于服务端的API
- **Characteristic**: 特征，具体的数据操作单元，包含读(read)、写(write)、通知(notify)等属性
- **Descriptor**: 描述符，用于描述Characteristic的元数据（如范围、计量单位、用户描述）
- **UUID**: 唯一标识符，16位为SIG标准定义，128位为自定义

---

## 三、GATT与ATT协议详解

### 3.1 ATT（Attribute Protocol）属性协议

ATT是BLE通信的基础协议，定义了简单的客户端-服务器模型：

- **属性结构**：
  - **Handle**: 16位句柄（索引）
  - **UUID**: 16或128位UUID（类型标识）
  - **Value**: 值（字节数组）
  - **Permissions**: 权限（读/写访问、安全链接要求）

- **数据包类型**：
  - Commands（命令）
  - Requests（请求）
  - Responses（响应）
  - Notifications（通知）
  - Indications（指示）
  - Confirmations（确认）

### 3.2 GATT（Generic Attribute Profile）通用属性配置文件

GATT建立在ATT之上，定义了数据层次结构：

```
Profile (配置文件)
└── Service (服务)
    ├── Characteristic (特征)
    │   ├── Properties (属性)
    │   ├── Value (值)
    │   └── Descriptor (描述符)
    └── ...
```

---

## 四、GAP角色定义

BLE设备在GAP层可以扮演四种角色：

| 角色 | 描述 |
|------|------|
| **Broadcaster** | 发送广播包，不接受连接（典型应用：Beacon） |
| **Observer** | 监听广播包，不发起连接 |
| **Central** | 发现并连接外设（典型应用：手机） |
| **Peripheral** | 广播并接受连接（典型应用：传感器、手环） |

> **注意**：同一设备可以同时扮演多个角色，例如手机可以同时作为Central连接手环，作为Peripheral连接电脑。

---

## 五、Core Bluetooth框架核心架构

### 5.1 框架概述

Core Bluetooth是苹果提供的iOS蓝牙通信框架，封装了BLE协议的复杂性，提供友好的API接口。

![结构图](images/CoreBluetooth.png)

### 5.2 核心组件

```
┌─────────────────────────────────────────────────────────┐
│              Core Bluetooth 框架                        │
├─────────────────────────────────────────────────────────┤
│  Central (中心设备)           │  Peripheral (外设)      │
│  ┌─────────────────────┐      │  ┌───────────────────┐  │
│  │ CBCentralManager   │      │  │ CBPeripheralManager│  │
│  │ - 扫描设备          │      │  │ - 发布服务         │  │
│  │ - 连接设备          │      │  │ - 广播服务         │  │
│  │ - 发现服务          │      │  │ - 响应读写请求     │  │
│  └─────────────────────┘      │  └───────────────────┘  │
│           │                   │           │             │
│           ▼                   │           ▼             │
│  ┌─────────────────────┐      │  ┌───────────────────┐  │
│  │    CBPeripheral     │◄─────┼──►│   CBMutableService │  │
│  │ (远程蓝牙设备)       │      │  │   CBMutableCharacteristic│  │
│  └─────────────────────┘      │  └───────────────────┘  │
│           │                   │                         │
│           ▼                   │                         │
│  ┌─────────────────────┐      │                         │
│  │  CBService          │      │                         │
│  │  CBCharacteristic   │      │                         │
│  │  CBDescriptor       │      │                         │
│  └─────────────────────┘      │                         │
└─────────────────────────────────────────────────────────┘
```

### 5.3 主要类说明

| 类名 | 作用 |
|------|------|
| `CBCentralManager` | 管理中心设备，负责扫描、连接蓝牙设备 |
| `CBPeripheral` | 代表远程外设，用于数据交互 |
| `CBPeripheralManager` | 管理本地外设，发布服务和广播 |
| `CBService` | 蓝牙设备提供的服务 |
| `CBCharacteristic` | 服务中的特征，具体数据单元 |
| `CBDescriptor` | 特征的描述符 |

---

## 六、Central模式开发（主机端）

### 6.1 开发流程

```
1. 初始化 CBCentralManager
      │
      ▼
2. 扫描附近蓝牙设备 (scanForPeripherals)
      │
      ▼
3. 发现目标设备 → 连接 (connect)
      │
      ▼
4. 发现服务 (discoverServices)
      │
      ▼
5. 发现特征 (discoverCharacteristics)
      │
      ▼
6. 读写特征值 / 订阅通知
      │
      ▼
7. 断开连接 (cancelPeripheralConnection)
```

### 6.2 代码实现

```swift
import CoreBluetooth

class CentralManager: NSObject {
    
    // 中心管理者
    private var centralManager: CBCentralManager!
    // 外设
    private var peripheral: CBPeripheral?
    // 可读写特征
    private var readWriteCharacteristic: CBCharacteristic?
    
    // 目标服务UUID
    private let targetServiceUUID = CBUUID(string: "FFE0")
    // 目标特征UUID
    private let targetCharacteristicUUID = CBUUID(string: "FFF2")
    
    override init() {
        super.init()
        centralManager = CBCentralManager(delegate: self, queue: DispatchQueue.main)
    }
}

// MARK: - CBCentralManagerDelegate
extension CentralManager: CBCentralManagerDelegate {
    
    // 蓝牙状态更新
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        switch central.state {
        case .poweredOn:
            print("蓝牙已开启，开始扫描...")
            // 扫描指定服务的外设
            central.scanForPeripherals(withServices: [targetServiceUUID], 
                                        options: [CBCentralManagerScanOptionAllowDuplicatesKey: false])
        case .poweredOff:
            print("蓝牙未开启")
        case .unauthorized:
            print("未授权蓝牙权限")
        case .unsupported:
            print("设备不支持蓝牙")
        default:
            print("其他状态")
        }
    }
    
    // 发现外设
    func centralManager(_ central: CBCentralManager, 
                        didDiscover peripheral: CBPeripheral,
                        advertisementData: [String: Any],
                        rssi RSSI: NSNumber) {
        
        print("发现设备: \(peripheral.name ?? "未知设备")")
        
        // 保存外设引用
        self.peripheral = peripheral
        // 停止扫描
        central.stopScan()
        // 连接外设
        central.connect(peripheral, options: nil)
    }
    
    // 连接成功
    func centralManager(_ central: CBCentralManager, 
                        didConnect peripheral: CBPeripheral) {
        print("连接成功: \(peripheral.name ?? "")")
        // 设置外设代理
        peripheral.delegate = self
        // 发现服务
        peripheral.discoverServices([targetServiceUUID])
    }
    
    // 连接失败
    func centralManager(_ central: CBCentralManager, 
                        didFailToConnect peripheral: CBPeripheral,
                        error: Error?) {
        print("连接失败: \(error?.localizedDescription ?? "未知错误")")
    }
    
    // 断开连接
    func centralManager(_ central: CBCentralManager, 
                        didDisconnectPeripheral peripheral: CBPeripheral,
                        error: Error?) {
        print("连接断开")
    }
}

// MARK: - CBPeripheralDelegate
extension CentralManager: CBPeripheralDelegate {
    
    // 发现服务
    func peripheral(_ peripheral: CBPeripheral, 
                   didDiscoverServices error: Error?) {
        guard error == nil else {
            print("服务发现错误: \(error!.localizedDescription)")
            return
        }
        
        guard let services = peripheral.services else { return }
        
        for service in services {
            print("发现服务: \(service.uuid)")
            // 发现特征
            peripheral.discoverCharacteristics(nil, for: service)
        }
    }
    
    // 发现特征
    func peripheral(_ peripheral: CBPeripheral, 
                   didDiscoverCharacteristicsFor service: CBService,
                   error: Error?) {
        guard error == nil else {
            print("特征发现错误: \(error!.localizedDescription)")
            return
        }
        
        guard let characteristics = service.characteristics else { return }
        
        for characteristic in characteristics {
            print("发现特征: \(characteristic.uuid)")
            
            // 订阅通知特征
            if characteristic.properties.contains(.notify) {
                peripheral.setNotifyValue(true, for: characteristic)
            }
            
            // 读取可读特征
            if characteristic.properties.contains(.read) {
                peripheral.readValue(for: characteristic)
            }
            
            // 保存可写特征
            if characteristic.properties.contains(.write) {
                readWriteCharacteristic = characteristic
            }
        }
    }
    
    // 读取特征值
    func peripheral(_ peripheral: CBPeripheral, 
                   didUpdateValueFor characteristic: CBCharacteristic,
                   error: Error?) {
        guard error == nil else {
            print("特征值读取错误")
            return
        }
        
        if let value = characteristic.value, 
           let stringValue = String(data: value, encoding: .utf8) {
            print("收到数据: \(stringValue)")
        }
    }
    
    // 写入特征值
    func writeData(_ data: Data) {
        guard let characteristic = readWriteCharacteristic else {
            print("无可写特征")
            return
        }
        
        // WithResponse: 需要外设确认
        // WithoutResponse: 无需确认，可能丢失数据
        peripheral?.writeValue(data, for: characteristic, type: .withResponse)
    }
    
    // 写入回调
    func peripheral(_ peripheral: CBPeripheral, 
                    didWriteValueFor characteristic: CBCharacteristic,
                    error: Error?) {
        if let error = error {
            print("写入失败: \(error.localizedDescription)")
        } else {
            print("写入成功")
        }
    }
}
```

---

## 七、Peripheral模式开发（外设端）

### 7.1 开发流程

```
1. 初始化 CBPeripheralManager
      │
      ▼
2. 创建服务 (CBMutableService)
      │
      ▼
3. 创建特征 (CBMutableCharacteristic)
      │
      ▼
4. 添加服务到外设管理器
      │
      ▼
5. 开始广播 (startAdvertising)
      │
      ▼
6. 响应Central的读写请求
      │
      ▼
7. 发送通知（可选）
```

### 7.2 代码实现

```swift
import CoreBluetooth
import UIKit

class PeripheralViewController: UIViewController {
    
    // MARK: - 常量定义
    private let service1UUID = CBUUID(string: "FFF0")
    private let service2UUID = CBUUID(string: "FFE0")
    
    private let notifyCharacteristicUUID = CBUUID(string: "FFF1")
    private let readWriteCharacteristicUUID = CBUUID(string: "FFF2")
    private let readCharacteristicUUID = CBUUID(string: "FFE1")
    
    private let localNameKey = "MyPeripheralDemo"
    
    // MARK: - 属性
    @IBOutlet weak var timeLabel: UILabel!
    private var peripheralManager: CBPeripheralManager!
    private var timer: Timer?
    private var subscribedCentral: CBCentral?
    private var notifyCharacteristic: CBMutableCharacteristic?
    
    // MARK: - 服务和特征
    private lazy var services: [CBMutableService] = {
        // 服务1 - 包含通知特征和读写特征
        let notifyChar = CBMutableCharacteristic(
            type: notifyCharacteristicUUID,
            properties: .notify,
            value: nil,
            permissions: .readable
        )
        self.notifyCharacteristic = notifyChar
        
        let readWriteChar = CBMutableCharacteristic(
            type: readWriteCharacteristicUUID,
            properties: [.read, .write],
            value: nil,
            permissions: [.readable, .writeable]
        )
        
        // 添加特征描述
        let description = CBMutableDescriptor(
            type: CBUUID(string: CBUUIDCharacteristicUserDescriptionString),
            value: "读写特征"
        )
        readWriteChar.descriptors = [description]
        
        let service1 = CBMutableService(type: service1UUID, primary: true)
        service1.characteristics = [notifyChar, readWriteChar]
        
        // 服务2 - 只读特征
        let readChar = CBMutableCharacteristic(
            type: readCharacteristicUUID,
            properties: .read,
            value: "Hello".data(using: .utf8),
            permissions: .readable
        )
        
        let service2 = CBMutableService(type: service2UUID, primary: true)
        service2.characteristics = [readChar]
        
        return [service1, service2]
    }()
    
    // MARK: - 生命周期
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // 开启外设模式
    @IBAction func startPeripheralMode(_ sender: UIButton) {
        peripheralManager = CBPeripheralManager(
            delegate: self,
            queue: DispatchQueue.main
        )
    }
    
    // 添加服务
    private func setupPeripheral() {
        for service in services {
            peripheralManager.add(service)
        }
    }
    
    // 开始广播
    private func startAdvertising() {
        let advertisementData: [String: Any] = [
            CBAdvertisementDataLocalNameKey: localNameKey,
            CBAdvertisementDataServiceUUIDsKey: services.map { $0.uuid }
        ]
        peripheralManager.startAdvertising(advertisementData)
    }
    
    // 更新通知特征值
    @objc private func updateNotifyValue() {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "HH:mm:ss"
        let timeString = dateFormatter.string(from: Date())
        
        if let data = timeString.data(using: .utf8),
           let characteristic = notifyCharacteristic {
            // 发送给订阅的Central
            peripheralManager.updateValue(
                data,
                for: characteristic,
                onSubscribedCentrals: nil
            )
            timeLabel.text = timeString
        }
    }
}

// MARK: - CBPeripheralManagerDelegate
extension PeripheralViewController: CBPeripheralManagerDelegate {
    
    // 状态更新
    func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager) {
        switch peripheral.state {
        case .poweredOn:
            print("蓝牙已开启")
            setupPeripheral()
        case .poweredOff:
            print("蓝牙未开启")
        default:
            print("其他状态")
        }
    }
    
    // 添加服务
    func peripheralManager(_ peripheral: CBPeripheralManager,
                          didAdd service: CBService,
                          error: Error?) {
        if let error = error {
            print("服务添加失败: \(error.localizedDescription)")
            return
        }
        print("服务添加成功: \(service.uuid)")
        
        // 所有服务添加完成后开始广播
        startAdvertising()
    }
    
    // 广播开始
    func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager,
                                               error: Error?) {
        if let error = error {
            print("广播失败: \(error.localizedDescription)")
            return
        }
        print("广播已开启")
    }
    
    // 读请求
    func peripheralManager(_ peripheral: CBPeripheralManager,
                          didReceiveRead request: CBATTRequest) {
        
        guard request.characteristic.properties.contains(.read) else {
            peripheral.respond(to: request, withResult: .readNotPermitted)
            return
        }
        
        // 返回特征值
        if let value = request.characteristic.value {
            request.value = value
        }
        
        peripheral.respond(to: request, withResult: .success)
    }
    
    // 写请求
    func peripheralManager(_ peripheral: CBPeripheralManager,
                          didReceiveWrite requests: [CBATTRequest]) {
        
        for request in requests {
            guard request.characteristic.properties.contains(.write) else {
                peripheral.respond(to: request, withResult: .writeNotPermitted)
                continue
            }
            
            // 更新特征值
            if let characteristic = request.characteristic as? CBMutableCharacteristic {
                characteristic.value = request.value
            }
            
            peripheral.respond(to: request, withResult: .success)
        }
    }
    
    // 订阅通知
    func peripheralManager(_ peripheral: CBPeripheralManager,
                          central: CBCentral,
                          didSubscribeTo characteristic: CBCharacteristic) {
        
        print("Central订阅了特征: \(characteristic.uuid)")
        subscribedCentral = central
        
        // 开始定时发送通知
        timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { [weak self] _ in
            self?.updateNotifyValue()
        }
    }
    
    // 取消订阅
    func peripheralManager(_ peripheral: CBPeripheralManager,
                          central: CBCentral,
                          didUnsubscribeFrom characteristic: CBCharacteristic) {
        
        print("Central取消订阅")
        timer?.invalidate()
        timer = nil
        subscribedCentral = nil
    }
}
```

---

## 八、数据传输机制

### 8.1 特征值操作

| 操作 | 方法 | 说明 |
|------|------|------|
| **读取** | `readValue(for:)` | 从外设读取特征值 |
| **写入** | `writeValue(_:for:type:)` | 写入数据到特征 |
| **通知** | `setNotifyValue(_:for:)` | 订阅/取消订阅通知 |
| **指示** | `setIndicateValue(_:for:)` | 订阅/取消指示（需确认） |

### 8.2 数据分片

> BLE单包数据传输限制为 **20字节**（LE 4.0）或 **244字节**（LE 4.2+），超过限制需要分包发送。

```swift
// 分包发送大数据的示例
func sendLargeData(_ data: Data, to characteristic: CBCharacteristic) {
    let maxLength = 20  // 或 244 for LE 4.2+
    var offset = 0
    
    while offset < data.count {
        let end = min(offset + maxLength, data.count)
        let chunk = data.subdata(in: offset..<end)
        
        peripheral.writeValue(chunk, for: characteristic, type: .withResponse)
        offset = end
    }
}
```

---

## 九、BLE安全

### 9.1 安全机制

BLE提供多层安全保护：

| 层级 | 机制 | 说明 |
|------|------|------|
| **配对 (Pairing)** | STK (短期密钥) | 临时安全连接 |
| **绑定 (Bonding)** | LTK (长期密钥) | 持久安全连接，重连后自动恢复 |
| **加密** | AES-CCM | 数据加密 |
| **隐私** | IRK (身份解析密钥) | 防止设备追踪 |

### 9.2 iOS中的安全特征

```swift
// 设置加密读写的特征
let secureCharacteristic = CBMutableCharacteristic(
    type: uuid,
    properties: [.read, .write],
    value: nil,
    permissions: [.readable, .writeable, .encryptedRequired]
)

// 加密通知
let encryptedNotifyChar = CBMutableCharacteristic(
    type: uuid,
    properties: [.notify],
    value: nil,
    permissions: [.readable]
)
// 需要加密才能订阅通知
encryptedNotifyChar._properties = CBCharacteristicProperties.notifyEncryptionRequired
```

---

## 十、开发最佳实践

### 10.1 性能优化

```swift
// 1. 指定服务UUID扫描，减少无效扫描
centralManager.scanForPeripherals(
    withServices: [targetServiceUUID], 
    options: nil
)

// 2. 使用CBCentralManagerScanOptionAllowDuplicatesKey谨慎
// 设为false避免重复回调，节省资源

// 3. 及时停止扫描
centralManager.stopScan()

// 4. 连接后及时发现服务，避免超时
peripheral.discoverServices(targetServiceUUIDs)
```

### 10.2 状态处理

```swift
// 蓝牙状态处理
func centralManagerDidUpdateState(_ central: CBCentralManager) {
    switch central.state {
    case .poweredOn:
        // 可以开始扫描
        break
    case .poweredOff:
        // 提示用户开启蓝牙
        showAlert(title: "提示", message: "请开启蓝牙")
    case .unauthorized:
        // 引导用户授权
        if let url = URL(string: UIApplication.openSettingsURLString) {
            UIApplication.shared.open(url)
        }
    case .unsupported:
        // 提示设备不支持
        showAlert(title: "提示", message: "设备不支持蓝牙")
    default:
        break
    }
}
```

### 10.3 错误处理

```swift
// 连接超时处理
func centralManager(_ central: CBCentralManager,
                    didFailToConnect peripheral: CBPeripheral,
                    error: Error?) {
    // 重试机制
    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
        central.connect(peripheral, options: nil)
    }
}

// 心跳机制检测连接状态
private func startHeartbeat() {
    timer = Timer.scheduledTimer(withTimeInterval: 10.0, repeats: true) { [weak self] _ in
        self?.checkConnection()
    }
}
```

---

## 十一、常见问题与解决方案

### 11.1 连接问题

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 无法发现设备 | 设备未开启广播/距离过远 | 检查设备状态，靠近设备 |
| 连接成功但无数据 | 服务未发现/特征权限不对 | 检查GATT服务配置 |
| 连接断开 | 信号弱/设备重启 | 实现重连机制 |

### 11.2 数据问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 数据不完整 | 超过单包限制 | 分包接收/发送 |
| 解析失败 | 编码格式不对 | 确认数据编码格式 |
| 通知收不到 | 未正确订阅 | 检查notify属性 |

---

## 十二、总结

Core Bluetooth框架为iOS开发者提供了强大的BLE通信能力。通过理解：

1. **BLE协议栈**：GAP定义角色，GATT/ATT定义数据结构
2. **Central/Peripheral模式**：根据业务需求选择合适的角色
3. **数据操作**：特征值的读写和通知机制
4. **安全考虑**：配对、加密、权限控制

开发者可以构建各种物联网应用，如智能家居、健康监测、设备配网等。

> 技术的学习在于实践，只有动手去做，才能真正掌握。蓝牙开发虽然有一定门槛，但只要按照规范的流程操作，就能实现稳定的通信。
