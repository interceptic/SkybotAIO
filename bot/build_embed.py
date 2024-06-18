import discord
import datetime


async def build(title, description, color):
    embed = discord.Embed(
        title=f"{title}",
        description=f"{description}",
        color=color
        )
    embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_5eca709aa35c37be7872d046e0d60a9d.webp?size=160')
    embed.timestamp = datetime.datetime.now()
    return embed