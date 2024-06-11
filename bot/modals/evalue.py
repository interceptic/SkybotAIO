import aiohttp
import discord
import datetime
async def send_embed(ctx, username):
    embed = discord.Embed(
                    title = f"**{username}**",
                    description = f"**Select any profile below**",
                    color=0x00F3FF
                    )
    embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
    embed.timestamp = datetime.datetime.now()   
    await ctx.send(embed=embed)