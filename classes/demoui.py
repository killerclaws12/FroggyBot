from __future__     import annotations

from discord        import ButtonStyle, Interaction 
from discord.ui     import Button, InputText, Modal, Select, View
from typing         import TYPE_CHECKING
from ui.common      import FrogView

from utilities      import make_embed

if TYPE_CHECKING:
    pass 
###########################################################################################
class Demostration: 

    def __init__(self):

        pass 
###########################################################################################
    async def display_components(self, interaction: Interaction) -> None: 

        embed = make_embed(title="Demostration UI Elements")
        view = FrogView()

        await interaction.response.send_message(embed=embed, view=view)
###########################################################################################