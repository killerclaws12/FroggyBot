from __future__     import annotations

from discord        import ButtonStyle, Interaction, Member, User
from discord.interactions import Interaction
from discord.ui     import Button, InputText, Modal, Select, View 
from typing         import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    pass 
###########################################################################################

_all__ = (
    "FrogView",
)
###########################################################################################
class FrogView(View):

    def __init__(
            self, 
            owner: Union[Member, User], 
            *args, 
            close_on_complete: bool = False, 
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.owner: Union[Member, User] = owner 
        self.value: Optional[Any] = None
        self.complete: bool = False

        self._interaction: Optional[Interaction] = None
        self._close_on_complete: bool = close_on_complete 
###########################################################################################
    async def interaction_check(self, interaction: Interaction) -> bool:

        if interaction.user == self.owner: 
            self._interaction = interaction 
            return True
        
        return False
###########################################################################################
    async def stop(self) -> None: 

        super().stop()

        if self._close_on_complete: 
            if self._interaction is not None: 
                try: 
                    await self._interaction.message.delete()
                except: 
                    try: 
                        await self._interaction.delete_original_response()
                    except: 
                        pass 
###########################################################################################