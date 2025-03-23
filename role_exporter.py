import discord
import csv
import asyncio

# ====== 配置区（请替换为你自己的 Token 和 ID）======
TOKEN = "your-token-here"           # Discord Bot 的 Token / Bot token
GUILD_ID = 123456789012345678       # 目标服务器的 ID / Target server ID
ROLE_ID = 987654321098765432        # 目标角色的 ID / Target role ID
# ========================================================

# 启用所需权限 / Enable necessary intents
intents = discord.Intents.default()
intents.members = True  # 成员列表 / Members
intents.guilds = True   # 服务器信息 / Guild info

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ 已登录为 Logged in as {client.user}')

    # 获取服务器对象 / Fetch the target guild (server)
    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("❌ 未找到服务器，请检查 GUILD_ID 是否正确 / Guild not found, check GUILD_ID")
        await client.close()
        return

    # 强制拉取所有成员（解决 role.members 不完整的问题）
    # Force-fetch members to ensure role.members works correctly
    await guild.chunk()

    # 获取角色对象 / Fetch the target role
    role = guild.get_role(ROLE_ID)
    if not role:
        print("❌ 未找到角色，请检查 ROLE_ID 是否正确 / Role not found, check ROLE_ID")
        await client.close()
        return

    # 获取所有拥有该角色的成员 / Get all members with the target role
    members_with_role = role.members

    # 导出到 CSV 文件 / Export to CSV
    with open("members_with_role.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Discord ID"])  # 表头 / CSV Header
        for member in members_with_role:
            # ⚠️ Discord 用户 ID 是 18~19 位纯数字，超出了 Excel 的精度范围（15 位）；
            # ⚠️ Excel 会将其四舍五入、变为 0 或科学计数法。
            # ✅ 所以这里在前面加一个 \t，让 Excel 把它当作字符串处理，防止精度丢失。
            # Discord IDs are 18-19 digits and exceed Excel's precision limit (15 digits).
            # Add \t to prevent Excel from rounding or converting to scientific notation.
            writer.writerow([f"{member.name}#{member.discriminator}", f"\t{member.id}"])

    print(f"✅ 成功导出 {len(members_with_role)} 名成员 / Exported {len(members_with_role)} members")
    await client.close()

# 启动 Bot / Run the bot
async def run_bot():
    async with client:
        await client.start(TOKEN)

asyncio.run(run_bot())
