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
        embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    except Exception as error:
        embed = discord.Embed(
            title=f"Exception Triggered",
            description=f"Error: {error}",
            color=0xFF007B
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
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
        embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)
    except Exception as error:
        embed = discord.Embed(
            title=f"Exception Triggered",
            description=f"Error: {error}",
            color=0xFF007B
        )
        embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
        embed.timestamp = datetime.datetime.now()
        await ctx.respond(embed=embed)