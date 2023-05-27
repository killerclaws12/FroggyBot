import os

from discord    import Bot, Intents
from dotenv     import load_dotenv
###########################################################################################
bot = Bot(
    description="The best multipurpose Discord bot.",
    intents=Intents.default(),
    debug_guilds=[1109243816822702180]
)
###########################################################################################
@bot.event
async def on_ready() -> None: 

    print("Bot is now online.")
###########################################################################################
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")
###########################################################################################
load_dotenv()

bot.run(os.getenv("DISCORD_TOKEN"))
###########################################################################################