from __future__         import annotations

from discord            import ApplicationContext, Cog, EmbedField, slash_command
from typing             import TYPE_CHECKING 

from utilities          import make_embed

if TYPE_CHECKING:
    from discord    import Bot 
###########################################################################################
class Testing(Cog):

    def __init__(self, bot: Bot):

        self.bot: Bot = bot 
###########################################################################################
    @slash_command(name="testing")
    async def testing_command(self, ctx: ApplicationContext) -> None:

        embed = make_embed( 
            title="FroggyBot test Embed",
            description=(
                "Best multipurpose bot"
            ),
            url="https://discord.com/",
            image_url="https://media.discordapp.net/attachments/1111834027545079818/1111873534973722634/2Q.png",
            thumbnail_url="https://media.discordapp.net/attachments/1111834027545079818/1111873534973722634/2Q.png",
            author_text="FroggyBot",
            author_url="https://media.discordapp.net/attachments/1111834027545079818/1111873534973722634/2Q.png",
            author_icon="https://media.discordapp.net/attachments/1111834027545079818/1111873534973722634/2Q.png",
            footer_text="Footer",
            footer_icon="https://media.discordapp.net/attachments/1111834027545079818/1111873534973722634/2Q.png",
            timestamp=True,
            fields=[
                EmbedField(name="Field1", value="Inline Field", inline=True),
                EmbedField(name="Field2", value="Inline Field", inline=True),
                EmbedField(name="Field3", value="Inline Field", inline=True),
                EmbedField(name="Field4", value="Not Inline Field", inline=False),
                EmbedField(name="Field5", value="Inline Field", inline=True),
                EmbedField(name="Field6", value="Inline Field", inline=True),
                EmbedField(name="Field7", value="Inline Field", inline=True),
            ],
            color=int("4ABC23", 16)
        )
        await ctx.respond(embed=embed)

###########################################################################################
def setup(bot: Bot) -> None: 

    bot.add_cog(Testing(bot))
###########################################################################################