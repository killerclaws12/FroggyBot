from __future__     import annotations 

from datetime       import datetime 
from discord        import Colour, Embed, EmbedField 
from discord.embeds import EmptyEmbed
from typing         import TYPE_CHECKING, Any, List, Optional, Tuple, Union

if TYPE_CHECKING: 
    pass
###########################################################################################
__all__ = (
    "make_embed",
)
###########################################################################################
def make_embed(
    *,
    title: str = EmptyEmbed,
    description: str = EmptyEmbed,
    url: str = EmptyEmbed,
    color: Union[Colour, int] = EmptyEmbed,
    thumbnail_url: str = EmptyEmbed,
    image_url: str = EmptyEmbed,
    author_text: str = EmptyEmbed,
    author_url: str = EmptyEmbed,
    author_icon: str = EmptyEmbed,
    footer_text: str = EmptyEmbed,
    footer_icon: str = EmptyEmbed,
    timestamp: Union[datetime, bool] = False,
    fields: Optional[List[Union[Tuple[str, Any, bool], EmptyEmbed]]] = None
) -> Embed: 
    embed = Embed(
        colour=color,
        title=title,
        description=description,
        url=url
    )

    embed.set_thumbnail(url=thumbnail_url)
    embed.set_image(url=image_url)

    if author_text is not EmptyEmbed:
        embed.set_author(
            name=author_text,
            url=author_url,
            icon_url=author_icon
        )

    if footer_text is not EmptyEmbed: 
        embed.set_footer(
            text=footer_text,
            icon_url=footer_icon
        )

    if isinstance(timestamp, datetime):
        embed.timestamp = timestamp
    elif timestamp is True:
        embed.timestamp = datetime.now()

    if fields is not None: 
        if all(isinstance(f, EmbedField) for f in fields):
            embed.fields = fields
        else: 
            for f in fields: 
                if isinstance(f, EmbedField):
                    embed.fields.append(f)
                elif isinstance(f, tuple):
                    embed.add_field(name=f[0], value=f[1], inline=f[2])
                else: 
                    continue
    return embed
###########################################################################################