# 全自动扣字QQ机器人

## 功能介绍

- 发送 `开战吧各位！` → 触发AI输出，流式逐条发送
- 发送 `停战吧！是我赢了` → 立即停止AI会话，停止发送消息
- `[XYH]` 分隔多条消息，每条实时发送
- 一轮结束自动开始下一轮，直到停战
- 只响应本号消息，其他人触发无效
- 自动获取当前登录QQ号

## 自定义配置

编辑 `bot.py` 顶部配置区：

```python
# NapCat OneBot API地址
NAPCAT_HTTP = "http://127.0.0.1:3001"

# AI API配置
AI_API_URL = "https://your-api-url/v1/chat/completions"
AI_API_KEY = "your-api-key"
AI_MODEL = "your-model"

# 触发/停战关键词
TRIGGER_START = "开战吧各位！"
TRIGGER_STOP = "停战吧！是我赢了"

# 消息分隔符
SEPARATOR = "[XYH]"

# 训练语料（学习风格用）
TRAINING_DATA = """
你的示例语录...
"""
```

### 训练语料说明

`TRAINING_DATA` 是给AI学习风格的参考，AI会：
- 学习语调、节奏、攻击方式
- 自己创造新内容，不会照抄
- 保持轻佻、蔑视的语气
- 不使用标点，只用逗号或空格

## NapCat 配置

### 1. 打开NapCat WebUI

```
http://你的服务器IP:6099/webui?token=你的token
```

### 2. 配置 OneBot11

进入 **配置** → **OneBot11配置**：

**HTTP API：**
- 开启：是
- 端口：`3001`
- 地址：`0.0.0.0`
- 跨域：开启

**WebSocket 服务器：**
- 开启：是
- 端口：`3002`
- 地址：`0.0.0.0`
- 上报自身消息：开启（重要！）

### 3. 保存并重启QQ

配置修改后需要重启QQ才能生效。

## 安装依赖

```bash
# 使用国内镜像
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple aiohttp websockets
```

## 启动机器人

### 前台运行（可看日志）

```bash
cd /opt/qq_bot
python3 -u bot.py
```

### 后台运行

```bash
cd /opt/qq_bot
nohup python3 -u bot.py > bot.log 2>&1 &
```

### 查看日志

```bash
tail -f /opt/qq_bot/bot.log
```

### 停止机器人

```bash
pkill -f bot.py
```

## 文件结构

```
qq_bot/
├── bot.py           # 主程序
├── bot.log          # 运行日志
├── README.md        # 说明文档
└── deploy.py        # 部署脚本（可选）
```

## 工作流程

```
开战吧各位！
    ↓
[第1轮] AI流式输出 → [XYH]分隔 → 逐条发送
    ↓ (一轮结束)
[第2轮] 自动继续...
    ↓ (收到停战)
停战吧！是我赢了
    ↓
立即断开AI → 停止发送
```

## 常见问题

### Q: 触发词不生效？
A: 检查NapCat是否开启了"上报自身消息"

### Q: AI不输出内容？
A: 检查AI API配置是否正确，测试API连通性

### Q: 停战后还继续发？
A: 检查bot日志是否有 `[停战]` 记录

### Q: 其他人也能触发？
A: 检查启动日志是否显示 `[设置] 只响应本号(xxx)的消息`
