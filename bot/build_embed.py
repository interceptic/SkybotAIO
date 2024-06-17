import discord
import datetime


async def build(title, description, color):
    embed = discord.Embed(
        title=f"{title}",
        description=f"{description}",
        color=color
        )
    embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
    embed.timestamp = datetime.datetime.now()
    return embed