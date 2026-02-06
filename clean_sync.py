import discord
from discord.ext import commands
import os

# ---------------- CONFIG ----------------
TOKEN = os.environ['TOKEN']          # Your bot token
GUILD_ID = int(os.environ['GUILD_ID'])  # Your server ID

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # Use Object() for guild
    guild = discord.Object(id=GUILD_ID)

    # Clear old slash commands for this guild
    try:
        await bot.tree.clear_commands(guild=guild)
        print("✅ Cleared all old guild commands!")
    except Exception as e:
        print("❌ Error clearing commands:", e)

    # Sync only current commands to this guild
    try:
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ Synced {len(synced)} commands to guild {GUILD_ID}")
    except Exception as e:
        print("❌ Error syncing commands:", e)

    # Done — close bot
    await bot.close()

bot.run(TOKEN)
