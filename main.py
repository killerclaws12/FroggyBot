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
load_dotenv()

bot.run(os.getenv("DISCORD_TOKEN"))

###########################################################################################