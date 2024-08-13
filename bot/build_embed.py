import discord
import datetime
from discord import Guild


async def build(title, description, color):
    embed = discord.Embed(
        title=f"{title}",
        description=f"{description}",
        color=color
        )
    # embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
    # embed.timestamp = datetime.datetime.now()
    return embed