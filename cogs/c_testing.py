from __future__         import annotations

from discord            import ApplicationContext, Cog, EmbedField, slash_command
from typing             import TYPE_CHECKING 

from classes.demoui     import Demostration
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

        demo = Demostration()
        await demo.display_components(ctx.interaction)

###########################################################################################
def setup(bot: Bot) -> None: 

    bot.add_cog(Testing(bot))
###########################################################################################