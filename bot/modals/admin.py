import discord
import datetime
from discord.ext import commands


async def give_admin(ctx, author_id, role_id):
    guild = ctx.guild
    user = await guild.fetch_member(author_id)
    role = guild.get_role(role_id)
    try:
        await user.add_roles(role)
        embed = discord.Embed(
            title=f"Role Given",
            description=f"<@&{role_id}> given to user <@{author_id}>",
            color=0x1D0FC7
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    except Exception as error:
        embed = discord.Embed(
            title=f"Exception Triggered",
            description=f"Error: {error}",
            color=0xFF007B
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)

async def remove_admin(ctx, author_id, role_id):
    guild = ctx.guild
    user = await guild.fetch_member(author_id)
    role = guild.get_role(role_id)
    try:
        await user.remove_roles(role)
        embed = discord.Embed(
            title=f"Role Removed",
            description=f"<@&{role_id}> removed from user <@{author_id}>",
            color=0x1D0FC7
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    except Exception as error:
        embed = discord.Embed(
            title=f"Exception Triggered",
            description=f"Error: {error}",
            color=0xFF007B
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)