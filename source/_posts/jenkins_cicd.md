---
date: 2025-12-19 10:40:49
title: Mac环境下搭建Jenkins CI/CD完整指南（iOS自动打包篇）
tags: [iOS, Jenkins, CI/CD, 自动化打包]
---

# 一、Mac环境准备

## 1. 安装Homebrew（如果未安装）
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. 安装Java 11/17
```bash
# 安装Java 11（推荐）
brew install openjdk@11

# 或者安装Java 17
brew install openjdk@17

# 设置环境变量
echo 'export PATH="/opt/homebrew/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc
echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@11"' >> ~/.zshrc

# 重新加载配置
source ~/.zshrc

# 验证安装
java -version
```

## 3. 安装Git（如果未安装）
```bash
brew install git
```

## 4. 安装Xcode命令行工具
```bash
# 安装Xcode命令行工具
xcode-select --install

# 验证安装
xcodebuild -version
xcrun simctl list devices available
```

## 5. 安装CocoaPods
```bash
# 安装CocoaPods
sudo gem install cocoapods

# 验证安装
pod --version
```

# 二、安装Jenkins

## 方法1：使用Homebrew安装（推荐）
```bash
# 安装Jenkins LTS版本
brew install jenkins-lts

# 或者安装最新版本
brew install jenkins

# 启动Jenkins服务
brew services start jenkins-lts

# 查看服务状态
brew services list | grep jenkins
```

## 方法2：使用Docker安装
```bash
# 安装Docker Desktop for Mac
# 从官网下载：https://www.docker.com/products/docker-desktop

# 拉取Jenkins镜像
docker pull jenkins/jenkins:lts-jdk11

# 创建数据卷
docker volume create jenkins_home

# 运行Jenkins容器
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(which docker):/usr/bin/docker \
  --restart unless-stopped \
  jenkins/jenkins:lts-jdk11

# 查看初始密码
docker logs jenkins
```

# 三、初始访问与配置

## 1. 访问Jenkins
```bash
# 获取初始管理员密码（Homebrew安装）
cat ~/.jenkins/secrets/initialAdminPassword

# Docker安装查看密码
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# 打开浏览器访问
open http://localhost:8080
```

## 2. 安装推荐插件
在 Jenkins 管理界面安装：
```
✅ Xcode Integration Plugin
✅ Git Plugin / GitLab Plugin
✅ GitHub Plugin
✅ CocoaPods Integration
✅ Fastlane Plugin
✅ JUnit Plugin（测试报告）
✅ Slack Notification（可选）
✅ Email Extension
✅ Build Timeout
✅ Generic Webhook Trigger
```

安装命令（CLI）：
```
java -jar jenkins-cli.jar install-plugin xcode-plugin git-plugin fastlane-plugin
```
- 选择"安装推荐的插件"
- 等待插件安装完成

## 3. 创建管理员账户

- 设置用户名、密码、邮箱

# 四、iOS打包环境配置

## 1. 安装Xcode插件

Jenkins需要安装Xcode相关插件来支持iOS构建：

1. 进入 **系统管理** → **插件管理** → **可选插件**
2. 搜索并安装以下插件：
   - **Xcode Plugin** - Xcode集成
   - **Keychains and Provisioning Profiles Management** - 证书管理
   - **Credentials Binding Plugin** - 凭据管理
   - **CocoaPods** - 如果项目使用CocoaPods管理依赖

## 2. 配置Keychain

### 创建Jenkins专用Keychain
```bash
# 创建名为"jenkins"的新keychain
security create-keychain -p "jenkins_password" jenkins

# 设置为默认keychain
security default-keychain -s jenkins

# 解锁keychain（构建时需要）
security unlock-keychain -p "jenkins_password" jenkins

# 设置keychain超时时间（防止构建时锁住）
security set-keychain-settings -t 3600 -l jenkins
```

### 导入开发者证书
```bash
# 导入.p12证书文件
security import /path/to/your_certificate.p12 -P "证书密码" -A -t cert -f pkcs12 -k ~/Library/Keychains/jenkins.keychain

# 设置证书始终可用
security set-key-partition-list -S apple-tool:,apple: -k "jenkins_password" -D "iPhone Developer: Your Name (TEAMID)" jenkins
```

## 3. 配置描述文件

### 创建描述文件目录
```bash
# 创建Jenkins可访问的描述文件目录
mkdir -p ~/Library/MobileDevice/Provisioning\ Profiles

# 复制描述文件到该目录
cp /path/to/*.mobileprovision ~/Library/MobileDevice/Provisioning\ Profiles/
```

### 在Jenkins中配置描述文件

1. 进入 **系统管理** → **Keychains and Provisioning Profiles**
2. 添加Keychain：
   - Keychain path: `~/Library/Keychains/jenkins.keychain`
   - Keychain password: `jenkins_password`
3. 添加Provisioning Profile：
   - Provisioning Profile path: `~/Library/MobileDevice/Provisioning Profiles/`
   - UUID: （自动识别）

# 五、创建iOS构建任务

## 1. 新建任务

1. 点击Jenkins首页的"新建任务"
2. 输入任务名称（如：`iOS-AutoBuild`）
3. 选择"构建一个自由风格的软件项目"
4. 点击"确定"

## 2. 配置源码管理

```bash
# 选择Git
# Repository URL: 你的iOS项目Git仓库地址
# Credentials: 添加Git仓库访问凭据（用户名/密码或SSH密钥）
# Branch: */main 或 */master
```

## 3. 配置构建触发器

### 定时构建
```bash
# 每天下午6点自动构建
H 18 * * 1-5
```

### 轮询SCM
```bash
# 每15分钟检查代码变化
H/15 * * * *
```

### Webhook触发（推荐）
1. 安装 **Generic Webhook Trigger** 插件
2. 在构建触发器中勾选"Generic Webhook Trigger"
3. 设置Token：`ios-build-token`
4. 在GitLab/GitHub配置Webhook：`http://your-jenkins-server/generic-webhook-trigger/invoke?token=ios-build-token`

## 4. 配置构建步骤

### 步骤1：使用CocoaPods安装依赖
```bash
# 进入项目目录
cd ${WORKSPACE}

# 如果使用CocoaPods
pod install --repo-update

# 或者使用CocoaPods的Alternate版本
${WORKSPACE}/Pods
```

### 步骤2：设置代码签名
```bash
# 解锁keychain
security unlock-keychain -p "jenkins_password" ~/Library/Keychains/jenkins.keychain

# 选择正确的签名标识
CODE_SIGN_IDENTITY="Apple Distribution: Your Company (TEAMID)"
PROVISIONING_PROFILE="Your Provisioning Profile Name"
```

### 步骤3：构建Debug版本
```bash
# 清理之前的构建
xcodebuild clean \
  -workspace ${WORKSPACE}/*.xcworkspace \
  -scheme YourSchemeName \
  -configuration Debug

# 构建Debug版本
xcodebuild \
  -workspace ${WORKSPACE}/*.xcworkspace \
  -scheme YourSchemeName \
  -configuration Debug \
  -codeSignIdentity "iPhone Developer" \
  -provisioningProfile "Your Provisioning Profile" \
  -derivedDataPath ${WORKSPACE}/build
```

### 步骤4：构建Release版本
```bash
xcodebuild \
  -workspace ${WORKSPACE}/*.xcworkspace \
  -scheme YourSchemeName \
  -configuration Release \
  -codeSignIdentity "Apple Distribution" \
  -provisioningProfile "Your App Store Profile" \
  -derivedDataPath ${WORKSPACE}/build
```

### 步骤5：导出IPA文件
```bash
# 使用xcodebuild导出
xcodebuild -exportArchive \
  -archivePath ${WORKSPACE}/build/Build/Products/*.xcarchive \
  -exportPath ${WORKSPACE}/output \
  -exportOptionsPlist ExportOptions.plist
```

### ExportOptions.plist内容
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>method</key>
    <string>app-store</string>
    <key>signingStyle</key>
    <string>manual</string>
    <key>teamID</key>
    <string>YOUR_TEAM_ID</string>
    <key>uploadBitcode</key>
    <false/>
    <key>uploadSymbols</key>
    <true/>
</dict>
</plist>
```

# 六、使用Fastlane简化构建

Fastlane是iOS/Android自动化打包的利器，可以大幅简化Jenkins配置。

## 1. 安装Fastlane
```bash
# 使用Ruby安装
sudo gem install fastlane -NV

# 或者使用Bundler
bundle init
echo 'gem "fastlane"' >> Gemfile
bundle install
```

## 2. 配置Fastfile
```ruby
# Fastfile
default_platform(:ios)

platform :ios do
  desc "Build iOS app for Debug"
  lane :build_debug do
    # 安装CocoaPods依赖
    cocoapods
    
    # 解锁keychain
    unlock_keychain(
      path: "~/Library/Keychains/jenkins.keychain",
      password: "jenkins_password"
    )
    
    # 构建
    build_app(
      workspace: "YourApp.xcworkspace",
      scheme: "YourScheme",
      configuration: "Debug",
      code_sign_identity: "iPhone Developer",
      provisioning_profile: "Your Debug Profile",
      derived_data_path: "./build"
    )
  end

  desc "Build iOS app for Release"
  lane :build_release do
    cocoapods
    
    build_app(
      workspace: "YourApp.xcworkspace",
      scheme: "YourScheme",
      configuration: "Release",
      code_sign_identity: "Apple Distribution",
      provisioning_profile: "Your App Store Profile",
      derived_data_path: "./build",
      export_options: {
        method: "app-store",
        teamID: "YOUR_TEAM_ID"
      }
    )
    
    # 上传到TestFlight
    # upload_to_testflight
  end
end
```

## 3. Jenkins中配置Fastlane构建

添加新的构建步骤：
```bash
# 使用Fastlane构建
cd ${WORKSPACE}
fastlane build_release
```

# 七、构建产物管理

## 1. 保存IPA文件
在构建后添加"Archive the artifacts"步骤：
```bash
# 保存IPA文件
**/*.ipa

# 保存构建日志
**/*.log
```

## 2. 配置构建历史保留策略

1. 进入任务配置 → "保留构建天数"和"最大构建数"
2. 建议保留最近30天或50个构建

# 八、常见问题与解决方案

## 问题1：证书找不到
**症状**：`codesign: Certificate is not valid`
**解决方案**：
```bash
# 列出可用的签名证书
security find-identity -v -p codesigning
```

## 问题2：描述文件找不到
**症状**：`No matching provisioning profile found`
**解决方案**：
```bash
# 查看已安装的描述文件
ls ~/Library/MobileDevice/Provisioning\ Profiles/
```

## 问题3：Keychain被锁定
**解决方案**：确保在构建脚本开头添加解锁命令
```bash
security unlock-keychain -p "jenkins_password" ~/Library/Keychains/jenkins.keychain
```

## 问题4：xcodebuild权限问题
**解决方案**：
```bash
# 重置xcodebuild权限
sudo DevToolsSecurity -enable
```

## 问题5：Pod依赖问题
**症状**：`diff: /../Podfile.lock: No such file or directory`
**解决方案**：
```bash
# 确保在workspace目录下执行pod install
cd ${WORKSPACE}/YourApp.xcworkspace/..
pod install
```

# 九、进阶配置：蒲公英/Fir.im自动分发

## 1. 安装分发工具
```bash
# 安装pgyer（蒲公英）
sudo gem install pgyer

# 或者fir-cli
sudo gem install fir-cli
```

## 2. 配置自动上传
在Fastlane中添加：
```ruby
lane :distribute do
  # 构建Release版本
  build_release
  
  # 上传到蒲公英
  pgyer(api_key: "YOUR_API_KEY", user_key: "YOUR_USER_KEY")
  
  # 或者上传到Fir.im
  fir_cli login: "YOUR_FIR_TOKEN"
  fir_cli publish: "./YourApp.ipa"
end
```

# 十、飞书机器人通知配置

飞书机器人是企业微信开发中常用的消息推送工具，可以通过Webhook实现自动化构建通知。本章节详细介绍如何在Jenkins构建完成后发送通知到飞书群聊。

## 1. 飞书机器人消息类型概述

飞书自定义机器人支持多种消息类型：

| 消息类型 | 说明 | 适用场景 |
|---------|------|---------|
| `text` | 纯文本消息 | 简单通知、快速提示 |
| `post` | 富文本消息 | 需要格式化的内容 |
| `interactive` | 消息卡片 | 包含按钮、图片等交互元素 |
| `image` | 图片消息 | 展示截图、二维码 |
| `file` | 文件消息 | 发送日志、安装包 |

## 2. 创建飞书机器人

### 方式一：通过群聊创建（推荐）
1. 打开飞书电脑客户端
2. 进入需要接收通知的群聊
3. 点击右上角「群设置」→「群机器人」→「添加机器人」
4. 选择「自定义机器人」
5. 设置机器人名称（如：iOS构建通知）
6. 复制生成的Webhook地址

### 方式二：通过开发者后台创建
1. 打开飞书开发者后台：https://open.feishu.cn/
2. 创建企业应用
3. 在应用权限中添加「群会话」相关权限
4. 发布应用并添加到群聊
5. 获取Webhook地址

### Webhook地址格式
```
https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

⚠️ **安全提示**：
- 请妥善保管Webhook地址，不要泄露到公开仓库
- 建议将地址存储在Jenkins凭据中
- 可以设置关键词验证增强安全性

## 3. 消息卡片详解

消息卡片（Interactive Card）是飞书机器人最强大的消息格式，支持丰富的交互元素。

### 卡片结构
```json
{
  "msg_type": "interactive",
  "card": {
    "header": {
      "title": { "tag": "plain_text", "content": "标题" },
      "template": "green"
    },
    "elements": [
      {
        "tag": "div",
        "text": { "tag": "plain_text", "content": "内容" }
      }
    ]
  }
}
```

### 卡片元素类型

| 元素标签 | 说明 |
|---------|------|
| `div` | 文本块，支持Markdown |
| `text` | 纯文本 |
| `markdown` | Markdown格式文本 |
| `image` | 图片 |
| `button` | 按钮 |
| `action` | 按钮组容器 |
| `hr` | 分割线 |
| `note` | 提示信息 |

### 卡片模板颜色
- `green` - 绿色（成功）
- `blue` - 蓝色（信息）
- `red` - 红色（错误）
- `yellow` - 黄色（警告）
- `grey` - 灰色（普通）
- `purple` - 紫色（特殊）

## 4. Jenkins中配置飞书通知

### 方式一：使用Shell脚本（推荐）

在Jenkins构建后步骤中添加Shell脚本：

```bash
#!/bin/bash

# 飞书Webhook地址（建议使用Jenkins凭据管理）
FEISHU_WEBHOOK="${FEISHU_WEBHOOK_URL}"

# 构建信息（从Jenkins环境变量获取）
BUILD_VERSION="1.0.0"
BUILD_NUMBER="${BUILD_NUMBER}"
BUILD_URL="${BUILD_URL}"
PGYER_URL="https://www.pgyer.com/xxxx"
BUILD_STATUS="成功"

# 发送文本消息
send_feishu_text() {
  local message="$1"
  curl -X POST "${FEISHU_WEBHOOK}" \
    -H "Content-Type: application/json" \
    -d "{\"msg_type\": \"text\", \"content\": {\"text\": \"${message}\"}}"
}

# 发送卡片消息
send_feishu_card() {
  local status="$1"
  local template="$2"
  
  # 根据状态选择颜色
  if [ "$status" == "成功" ]; then
    local color="green"
    local emoji="🎉"
  else
    local color="red"
    emoji="❌"
  fi
  
  curl -X POST "${FEISHU_WEBHOOK}" \
    -H "Content-Type: application/json" \
    -d '{
      "msg_type": "interactive",
      "card": {
        "header": {
          "title": {
            "tag": "plain_text",
            "content": "'"${emoji} iOS App 构建${status}"'"
          },
          "template": "'"${color}"'"
        },
        "elements": [
          {
            "tag": "div",
            "fields": [
              {
                "is_short": true,
                "text": {
                  "tag": "lark_md",
                  "content": "**📦 版本：**'"${BUILD_VERSION}"'"
                }
              },
              {
                "is_short": true,
                "text": {
                  "tag": "lark_md",
                  "content": "**🔢 构建号：**'"${BUILD_NUMBER}"'"
                }
              }
            ]
          },
          {
            "tag": "hr"
          },
          {
            "tag": "div",
            "text": {
              "tag": "lark_md",
              "content": "**🔗 下载链接：**\n['"${PGYER_URL}"']('"${PGYER_URL}"')"
            }
          },
          {
            "tag": "div",
            "text": {
              "tag": "lark_md",
              "content": "**⏰ 构建时间：**'"$(date '+%Y-%m-%d %H:%M:%S')"'"
            }
          },
          {
            "tag": "action",
            "actions": [
              {
                "tag": "button",
                "text": {
                  "tag": "plain_text",
                  "content": "立即下载"
                },
                "type": "primary",
                "url": "'"${PGYER_URL}"'"
              },
              {
                "tag": "button",
                "text": {
                  "tag": "plain_text",
                  "content": "查看构建"
                },
                "url": "'"${BUILD_URL}"'"
              }
            ]
          }
        ]
      }
    }'
}

# 调用发送函数
send_feishu_card "${BUILD_STATUS}" "${color}"
```

### 方式二：使用Fastlane

#### 安装飞书通知插件
```bash
sudo gem install fastlane-plugin-feishu_notify
```

#### 配置Fastfile
```ruby
lane :distribute do
  # 构建Release版本
  build_release
  
  # 上传到蒲公英
  pgyer_result = pgyer(
    api_key: "YOUR_API_KEY", 
    user_key: "YOUR_USER_KEY"
  )
  
  # 获取蒲公英返回的下载链接
  pgyer_url = pgyer_result["buildQRCodeURL"]
  
  # 发送飞书通知
  send_feishu_notification(
    webhook_url: "YOUR_WEBHOOK_URL",
    build_status: "success",
    version: "1.0.0",
    build_number: "100",
    pgyer_url: pgyer_url
  )
end

# 封装飞书通知方法
def send_feishu_notification(config)
  webhook_url = config[:webhook_url]
  status = config[:build_status]
  
  # 根据状态设置颜色和消息
  if status == "success"
    template = "green"
    title = "🎉 iOS App 构建成功"
    status_text = "成功"
  else
    template = "red"
    title = "❌ iOS App 构建失败"
    status_text = "失败"
  end
  
  # 构建卡片JSON
  card_json = {
    msg_type: "interactive",
    card: {
      header: {
        title: {
          tag: "plain_text",
          content: title
        },
        template: template
      },
      elements: [
        {
          tag: "div",
          fields: [
            {
              is_short: true,
              text: {
                tag: "lark_md",
                content: "**📦 版本：**#{config[:version]}"
              }
            },
            {
              is_short: true,
              text: {
                tag: "lark_md",
                content: "**🔢 构建号：**#{config[:build_number]}"
              }
            }
          ]
        },
        { tag: "hr" },
        {
          tag: "div",
          text: {
            tag: "lark_md",
            content: "**🔗 下载链接：**\n#{config[:pgyer_url]}"
          }
        },
        {
          tag: "action",
          actions: [
            {
              tag: "button",
              text: { tag: "plain_text", content: "立即下载" },
              type: "primary",
              url: config[:pgyer_url]
            }
          ]
        }
      ]
    }
  }.to_json
  
  # 发送请求
  uri = URI.parse(webhook_url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = true
  
  request = Net::HTTP::Post.new(uri.request_uri)
  request['Content-Type'] = 'application/json'
  request.body = card_json
  
  http.request(request)
end
```

### 方式三：使用Jenkins插件

1. 安装「Feishu Notification」插件
2. 在构建后操作中添加「Feishu Notification」
3. 配置Webhook地址和消息内容

## 5. 构建失败通知

### Jenkins构建失败时通知
```bash
# 在Shell脚本最后检查构建状态
if [ $? -ne 0 ]; then
  # 构建失败，发送红色卡片通知
  curl -X POST "${FEISHU_WEBHOOK}" \
    -H "Content-Type: application/json" \
    -d '{
      "msg_type": "interactive",
      "card": {
        "header": {
          "title": {
            "tag": "plain_text",
            "content": "❌ iOS App 构建失败"
          },
          "template": "red"
        },
        "elements": [
          {
            "tag": "div",
            "text": {
              "tag": "lark_md",
              "content": "**🔢 构建号：**'"${BUILD_NUMBER}"'"
            }
          },
          {
            "tag": "div",
            "text": {
              "tag": "lark_md",
              "content": "**⏰ 失败时间：**'"$(date '+%Y-%m-%d %H:%M:%S')"'"
            }
          },
          {
            "tag": "action",
            "actions": [
              {
                "tag": "button",
                "text": {
                  "tag": "plain_text",
                  "content": "查看日志"
                },
                "url": "'"${BUILD_URL}"'/console"
              }
            ]
          }
        ]
      }
    }'
  exit 1
fi
```

### Fastlane中使用try-catch
```ruby
lane :distribute do
  begin
    build_release
    pgyer(api_key: "YOUR_API_KEY", user_key: "YOUR_USER_KEY")
    
    # 构建成功通知
    send_feishu_notification(
      webhook_url: "YOUR_WEBHOOK_URL",
      build_status: "success",
      version: "1.0.0",
      build_number: "100",
      pgyer_url: "https://www.pgyer.com/xxxx"
    )
  rescue => ex
    # 构建失败通知
    send_feishu_notification(
      webhook_url: "YOUR_WEBHOOK_URL",
      build_status: "failed",
      version: "1.0.0",
      build_number: "100",
      error_message: ex.message
    )
    
    # 抛出异常，让Jenkins标记构建失败
    raise
  end
end
```

## 6. 高级特性

### 6.1 使用飞书卡片搭建工具

飞书提供了可视化的卡片搭建工具：https://open.feishu.cn/tool/cardbuilder

可以可视化的设计卡片，然后导出JSON代码。

### 6.2 @指定人员

在消息中使用`at`来@群成员：
```json
{
  "msg_type": "text",
  "content": {
    "text": "<at id=all></at> 构建完成"
  }
}
```

### 6.3 消息图片

发送图片需要先上传图片获取image_key：
```bash
# 1. 先上传图片
IMAGE_KEY=$(curl -X POST "https://open.feishu.cn/open-apis/image/v3/upload/" \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  -F "image_type=message" \
  -F "image=@/path/to/image.png" | jq -r '.data.image_key')

# 2. 发送图片消息
curl -X POST "${FEISHU_WEBHOOK}" \
  -H "Content-Type: application/json" \
  -d '{
    "msg_type": "image",
    "content": {
      "image_key": "'"${IMAGE_KEY}"'"
    }
  }'
```

### 6.4 富文本消息（post类型）

```json
{
  "msg_type": "post",
  "content": {
    "post": {
      "zh_cn": {
        "title": "构建通知",
        "content": [
          [
            { "tag": "text", "text": "版本：" },
            { "tag": "text", "text": "1.0.0", "bold": true }
          ],
          [
            { "tag": "text", "text": "构建号：" },
            { "tag": "text", "text": "100" }
          ]
        ]
      }
    }
  }
}
```

## 7. 环境变量与凭据管理

### 在Jenkins中配置凭据

1. 进入 **Jenkins** → **系统管理** → **凭据** → **添加凭据**
2. 类型选择「Secret text」
3. 填写：
   - ID：`feishu_webhook`
   - Secret：Webhook地址
   - 描述：飞书机器人Webhook

### 在脚本中使用凭据

```bash
# 方法1：使用环境变量注入
FEISHU_WEBHOOK="${FEISHU_WEBHOOK_SECRET}"

# 方法2：使用Credentials Binding插件
# 在构建环境中勾选"绑定"→"_secret text"
# 然后使用变量名
```

## 8. 错误排查

### 常见错误

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| 99991663 | 签名校验失败 | 检查timestamp和sign是否正确 |
| 99991664 | token不存在 | 确认Webhook地址是否正确 |
| 99991665 | 请求体过大 | 减少消息内容或分包发送 |

### 调试技巧

1. **使用curl测试**：
```bash
# 测试发送文本消息
curl -X POST "YOUR_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"msg_type": "text", "content": {"text": "测试消息"}}'
```

2. **检查返回结果**：
```bash
# 查看飞书返回的错误信息
curl -X POST "YOUR_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '...' \
  -w "\nHTTP Code: %{http_code}\n"
```

3. **日志记录**：
```bash
# 在脚本中添加日志
echo "发送飞书通知..." >> /tmp/feishu.log
curl -X POST ... >> /tmp/feishu.log 2>&1
echo "发送完成" >> /tmp/feishu.log
```

---

# 十一、完整构建流程示例

```
┌─────────────────────────────────────────┐
│           iOS自动打包流程                │
├─────────────────────────────────────────┤
│  1. 代码拉取 (Git)                       │
│  2. 依赖安装 (CocoaPods/Fastlane)        │
│  3. 解锁Keychain                        │
│  4. 代码签名 (证书+描述文件)             │
│  5. 编译构建 (xcodebuild)               │
│  6. 导出IPA (archive + export)          │
│  7. 保存产物 (IPA + dSYM)               │
│  8. 清理工作 (可选)                      │
└─────────────────────────────────────────┘
```

---

通过以上配置，你就可以在Mac环境下使用Jenkins实现iOS应用的自动打包了。首次配置可能需要一些时间，但一旦配置完成，后续的打包工作将变得非常简单。只需提交代码，Jenkins就会自动完成构建、签名和打包的全过程。
