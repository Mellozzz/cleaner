import discord
from discord.ext import commands
import os

# ---------------- CONFIG ----------------
TOKEN = os.environ['TOKEN']          # Your bot token
GUILD_ID = int(os.environ['GUILD_ID'])  # Your server ID

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- CLEAN & SYNC ----------------
@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)

    # 1️⃣ Clear all guild commands
    await bot.tree.clear_commands(guild=guild)
    print("✅ Cleared all old guild commands!")

    # 2️⃣ Sync only current commands
    synced = await bot.tree.sync(guild=guild)
    print(f"✅ Synced {len(synced)} commands to guild {GUILD_ID}")

    # Done — close the bot
    await bot.close()

bot.run(TOKEN)
