# 🧾 Discord Role Exporter Bot ｜角色成员导出工具

一个用于导出特定角色成员列表的 Discord Bot，支持自动生成 CSV 文件，适合 Ambassador、KOL、社区管理等场景。
A Discord bot that exports all members with a specific role to a CSV file. Useful for ambassador tracking, KOL campaigns, and community management.

---

## ✅ 功能 Features

- 获取指定服务器中指定角色的所有成员
- 导出用户名 + Discord ID 到 CSV 文件
- 自动处理 Discord ID 精度，避免 Excel 截断

---

## 📥 Discord Bot 创建指引｜Bot Setup Guide

前往 Discord Developer Portal 创建你的 Bot：  
Go to the Discord Developer Portal to create your bot:
👉 https://discord.com/developers/applications

### 必做操作 Required Steps：

1. 创建一个新的 Application / Create a new Application
2. 进入「Bot」标签页，点击「Add Bot」 / Go to "Bot" tab → Add Bot
3. 复制你的 Bot Token（用于代码中） / Copy your Bot Token
4. 进入「OAuth2 → URL Generator」生成邀请链接 / Go to OAuth2 → URL Generator
   - 勾选 scope: `bot`
   - 勾选权限：`View Members`、`Read Messages/View Channels`、`Send Messages`
5. 使用生成的链接邀请 Bot 加入你的服务器 / Invite bot to your server using the generated link

---

## 📦 使用方法 How to Use

### 1️⃣ 安装依赖 Install dependencies

```bash
pip install -U discord.py
```

### 2️⃣ 修改配置 Edit config

在 `role_exporter.py` 中填入以下内容：
Fill in the following fields in `role_exporter.py`:

```python
TOKEN = "your-bot-token"
GUILD_ID = 你的服务器ID / Your server (guild) ID
ROLE_ID = 目标角色ID / Target role ID
```

### 3️⃣ 运行脚本 Run the bot

```bash
python role_exporter.py
```

完成后会生成一个 `members_with_role.csv` 文件。  
After success, a file named `members_with_role.csv` will be created.

---

## 📄 注意事项 Excel Tips

⚠️ Discord 用户 ID 是 18~19 位纯数字，超出 Excel 精度上限（15 位）。  
Discord IDs are 18–19 digit pure numbers, which exceed Excel’s precision limit (15 digits).

为避免被四舍五入或显示为科学计数法，脚本会在 ID 前添加 `\t`，确保被识别为文本。  
To prevent rounding or scientific notation, the script adds a `\t` prefix so Excel treats it as text.

---

## 🧪 示例输出 Sample CSV

| Username       | Discord ID           |
|----------------|----------------------|
| testuser       | 1234567890987654321  |

---

## 🪪 开源协议 License

本项目采用 [MIT License](LICENSE)。  
Licensed under the [MIT License](LICENSE).

---

欢迎 PR，欢迎 Star⭐️！  
PRs and Stars are welcome! ⭐️
![image](https://github.com/user-attachments/assets/6d177c25-0bc5-4286-afc4-30eea6ba4dba)
