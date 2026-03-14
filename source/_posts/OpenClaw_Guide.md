---
title: OpenClaw 小龙虾火爆全球
---

# OpenClaw 安装详细教程

> 本教程将详细介绍 OpenClaw 的完整安装过程，帮助你快速搭建 AI Agent 开发环境

---

## 什么是 OpenClaw？

OpenClaw 是一个强大的 AI 智能体框架，支持多渠道接入、多模型切换，适用于构建个人 AI 助手、智能客服、自动化工作流等多种场景。

---

## 一、环境准备 (macOS 平台)

### 1.1 系统要求

| 项目 | 最低要求 | 推荐配置 |
|------|----------|----------|
| 操作系统 | macOS 12+ (Monterey+) | macOS 14+ (Sonoma) |
| Node.js | ≥ 22.0.0 | 22.x.x LTS |
| npm | ≥ 10.0.0 | 10.x.x |
| 内存 | 4GB RAM | 8GB RAM 以上 |
| 存储空间 | 2GB 可用空间 | 5GB 以上 |
| 芯片 | Intel 或 Apple Silicon | Apple Silicon (M1/M2/M3) |

### 1.2 在 macOS 上安装 Node.js

#### 方法一：使用 Homebrew（推荐）

```bash
# 如果没有安装 Homebrew，先安装
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Node.js 22
brew install node@22

# 刷新环境变量
source ~/.zshrc

# 验证安装
node --version
npm --version
```

#### 方法二：使用 nvm（推荐开发人员）

```bash
# 安装 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# 将以下内容添加到 ~/.zshrc
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# 重新加载终端配置
source ~/.zshrc

# 安装 Node.js 22
nvm install 22
nvm use 22
nvm alias default 22

# 验证安装
node --version  # 输出: v22.x.x
```

#### 方法三：直接下载安装包

1. 访问 [Node.js 官网](https://nodejs.org/)
2. 下载 macOS Installer (.pkg)
3. 双击安装包，按提示完成安装

#### Apple Silicon (M1/M2/M3) 特别说明

```bash
# 检查芯片架构
uname -m

# 如果输出 arm64，表示使用的是 Apple Silicon
# Node.js 已原生支持，无需额外配置
```

### 1.3 安装 Git（可选但推荐）

```bash
# 使用 Homebrew 安装
brew install git

# 验证安装
git --version
```

### 1.4 检查环境

安装完成后，在终端执行以下命令验证：

```bash
node --version
# 输出: v22.x.x

npm --version
# 输出: 10.x.x

# 验证 OpenClaw 安装（后续步骤）
openclaw --version
```

---

## 二、安装 OpenClaw

### 2.1 使用 npm 安装（推荐）

```bash
npm install -g openclaw@latest
```

### 2.2 使用 pnpm 安装（性能更优）

```bash
# 如果没有安装 pnpm，先安装
npm install -g pnpm

# 安装 OpenClaw
pnpm add -g openclaw@latest
```

### 2.3 使用 bun 安装

```bash
bun install -g openclaw@latest
```

### 2.4 验证安装

```bash
openclaw --version
```

正常情况下会显示版本号，例如：`openclaw/2.1.0`

---

## 三、初始化配置

### 3.1 启动引导程序

```bash
openclaw onboard --install-daemon
```

### 3.2 配置步骤

引导程序会提示你完成以下配置：

#### Step 1: 选择配置模式

```
? 请选择配置模式:
  ❯ QuickStart  - 快速开始配置 (推荐新手)
    Custom      - 自定义配置 (适合高级用户)
```

**建议新手选择 QuickStart**

#### Step 2: 选择 AI 模型

支持的模型供应商：

| 模型 | 特点 | 需要网络 |
|------|------|----------|
| MiniMax | 国内可用，中文支持好 | 否 |
| Kimi | 长文本处理强 | 否 |
| DeepSeek | 推理能力强，代码出色 | 否 |
| Claude | 综合能力强 | 是 |
| OpenAI GPT | 经典选择 | 是 |
| Ollama | 本地模型，离线可用 | 否 |

#### Step 3: 输入 API Key

根据选择的模型，输入对应的 API Key：

```bash
? 选择认证方式: MiniMax M2.5(CN)
? 输入 API Key: [粘贴你的 API Key]
✓ 认证成功
```

> **提示**: API Key 需要前往对应平台申请：
> - MiniMax: [platform.minimax.io](https://platform.minimax.io)
> - DeepSeek: [platform.deepseek.com](https://platform.deepseek.com)
> - Claude: [console.anthropic.com](https://console.anthropic.com)

#### Step 4: 跳过可选配置

首次安装可以暂时跳过以下配置：
- Channel (渠道) 配置
- Skill (技能) 安装
- Hooks (钩子) 配置

这些可以后续单独配置。

#### Step 5: 启动 Web UI

```
? 是否打开 Web UI? Yes
✓ 正在启动 Dashboard...
✓ Dashboard 已启动: http://127.0.0.1:18789
```

浏览器会自动打开管理界面。如果没有自动打开，手动访问：`http://127.0.0.1:18789`

---

## 四、常用命令速查

### 4.1 管理命令

| 命令 | 说明 |
|------|------|
| `openclaw dashboard` | 打开 Web 管理界面 |
| `openclaw status` | 查看运行状态 |
| `openclaw logs` | 查看日志 |
| `openclaw doctor` | 运行诊断 |
| `openclaw stop` | 停止所有服务 |
| `openclaw update` | 更新到最新版本 |

### 4.2 Agent 命令

```bash
# 与助手对话
openclaw agent --message "你好" --thinking high

# 列出所有 Agent
openclaw agents list

# 添加新 Agent
openclaw agents add <agent-name>
```

### 4.3 Channel 命令

```bash
# 列出所有渠道
openclaw channels list

# 添加新渠道
openclaw channels add

# 重启渠道
openclaw channels restart <channel-name>
```

### 4.4 技能命令

```bash
# 列出已安装技能
openclaw skills list

# 安装新技能 (需要先安装 clawhub)
clawhub install <skill-name>
```

---

## 五、从源码构建（开发者）

如果你想参与开发或使用最新功能：

### 5.1 克隆项目

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
```

### 5.2 安装依赖

```bash
# 使用 pnpm (推荐)
pnpm install

# 或使用 npm
npm install
```

### 5.3 构建项目

```bash
# 构建 UI
pnpm ui:build

# 构建核心
pnpm build
```

### 5.4 运行开发服务器

```bash
# 启动 Gateway (开发模式，热重载)
pnpm gateway:watch

# 或启动完整服务
pnpm dev
```

### 5.5 运行测试

```bash
# 单元测试
pnpm test

# 集成测试
pnpm test:integration

# 代码检查
pnpm lint
```

---

## 六、配置文件说明

### 6.1 配置文件位置

```
~/.openclaw/
├── config.json          # 主配置文件
├── agents/              # Agent 工作区
│   └── main/
├── channels/            # 渠道配置
├── skills/              # 已安装技能
└── logs/                # 日志文件
```

### 6.2 主配置文件示例

`~/.openclaw/config.json`:

```json
{
  "version": "2.1.0",
  "provider": "minimax",
  "api_key": "your-api-key-here",
  "gateway": {
    "port": 18789,
    "host": "127.0.0.1"
  },
  "channels": [],
  "plugins": []
}
```

---

## 七、常见问题

### Q1: 安装报错 `EACCES` 权限错误

```bash
# 方案 1: 使用 sudo
sudo npm install -g openclaw@latest

# 方案 2: 修复 npm 权限
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Q2: Node.js 版本过低

```bash
# 使用 nvm 升级
nvm install 22
nvm use 22
```

### Q3: Web UI 无法访问

```bash
# 检查服务状态
openclaw status

# 查看日志
openclaw logs

# 重启服务
openclaw stop
openclaw dashboard
```

### Q4: API Key 无效

- 确认 API Key 已正确复制，没有多余空格
- 检查 API Key 是否已过期
- 确认对应的服务在国内网络环境下可用

---

## 八、进阶配置

### 8.1 配置多个模型

编辑 `~/.openclaw/config.json`:

```json
{
  "models": {
    "default": "minimax",
    "alternatives": {
      "claude": {
        "provider": "anthropic",
        "api_key": "sk-ant-xxx"
      },
      "deepseek": {
        "provider": "deepseek",
        "api_key": "sk-xxx"
      }
    }
  }
}
```

### 8.2 配置飞书渠道

飞书是 OpenClaw 支持的重要渠道之一，以下是详细配置步骤：

#### 8.2.1 创建飞书应用

1. **访问飞书开放平台**
   - 打开 [飞书开放平台](https://open.feishu.cn/)
   - 使用企业账号登录（如没有需要先注册企业账号）

2. **创建应用**
   - 进入「应用开发」
   - 点击「创建应用」
   - 填写应用名称（如 OpenClaw Bot）
   - 点击「确认创建」

3. **获取 App ID 和 App Secret**
   - 创建成功后，在应用详情页面
   - 复制 `App ID` 和 `App Secret` 备用

#### 8.2.2 配置应用权限

在飞书开放平台后台：

1. 进入「权限管理」
2. 添加以下权限：

| 权限名称 | 说明 |
|----------|------|
| im:message:send_as_bot | 以机器人身份发送消息 |
| im:message:receive | 接收消息 |
| im:chat:list | 获取群聊列表 |
| im:chat:create | 创建群聊 |
| im:chat:update | 更新群聊信息 |
| im:chat:members:get | 获取群成员 |
| contact:user.base:readonly | 读取用户基本信息 |
| contact:user.id:readonly | 获取用户 user_id |

3. 点击「批量开通」

#### 8.2.3 配置事件订阅

1. 进入「事件订阅」
2. 点击「添加事件」
3. 添加以下事件：

| 事件名称 | 说明 |
|----------|------|
| im.message.receive_v1 | 接收消息事件 |
| im.chat.member.user_added_v1 | 成员入群事件 |
| im.chat.member.user_removed_v1 | 成员退群事件 |

4. 点击「批量开通」
5. 点击「发布」按钮发布版本

#### 8.2.4 获取验证 Token

在应用详情页面：

1. 进入「凭证与基础信息」
2. 找到 `App ID` 和 `App Secret`
3. 复制备用

#### 8.2.5 在 OpenClaw 中配置飞书

**方式一：使用命令行配置**

```bash
# 添加飞书渠道
openclaw channels add feishu

# 配置 App ID
openclaw channels config feishu app_id "your-app-id"

# 配置 App Secret  
openclaw channels config feishu app_secret "your-app-secret"

# 配置验证 Token (可选)
openclaw channels config feishu verification_token "your-verification-token"
```

**方式二：编辑配置文件**

编辑 `~/.openclaw/config.json`:

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "app_id": "your-app-id",
      "app_secret": "your-app-secret",
      "verification_token": "your-verification-token",
      "encrypt_key": "your-encrypt-key (可选)"
    }
  }
}
```

#### 8.2.6 启动飞书渠道

```bash
# 重启渠道服务
openclaw channels restart feishu

# 查看渠道状态
openclaw channels list

# 查看飞书渠道日志
openclaw logs --channel feishu
```

#### 8.2.7 添加机器人到群聊

1. 在飞书中创建或打开一个群聊
2. 点击群设置 → 添加成员
3. 搜索你的应用名称（OpenClaw Bot）
4. 添加机器人为成员

#### 8.2.8 测试飞书渠道

```bash
# 发送测试消息到飞书
openclaw message send --channel feishu --to "群聊ID" --message "Hello from OpenClaw!"

# 或者使用 agent 命令
openclaw agent --message "你好" --channel feishu
```

### 8.3 配置渠道

支持的渠道类型：
- Telegram
- Discord
- Slack
- 微信公众号
- 企业微信
- 飞书 ✅
- 自定义 Webhook

```bash
# 添加飞书渠道
openclaw channels add feishu
```

### 8.4 安装技能

```bash
# 安装 clawhub
npm install -g clawhub

# 搜索技能
clawhub search <关键词>

# 安装技能
clawhub install <skill-name>
```

---

## 九、更新与卸载

### 9.1 更新 OpenClaw

```bash
# 更新到最新稳定版
openclaw update

# 切换版本通道
openclaw update --channel stable   # 稳定版
openclaw update --channel beta    # 测试版
openclaw update --channel dev     # 开发版
```

### 9.2 卸载 OpenClaw

```bash
# 停止服务
openclaw stop

# 卸载全局包
npm uninstall -g openclaw

# 删除配置目录 (可选)
rm -rf ~/.openclaw
```

---

## 十、相关资源

- 官方网站: [openclawgithub.cc](https://openclawgithub.cc)
- GitHub 仓库: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- 中文文档: [openclawgithub.cc/guide](https://openclawgithub.cc/guide)
- QQ 交流群: 123456789

---

> 祝你在 OpenClaw 的旅程愉快！🎉