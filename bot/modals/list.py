import os
import aiosqlite
from bot.build_embed import build
import discord
from discord.ui import View, Button, InputText, Modal
from bot.modals.views.button import button_view
import asyncio


async def build(title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

class Setup:
    @staticmethod
    async def check(ctx):
        embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 1/6**", 0xFF0000)
        view = button_view(ctx, "Role ID of Sellers", "ID")
        print(embed)
        await ctx.edit(embed=embed, view=view)

            
            
