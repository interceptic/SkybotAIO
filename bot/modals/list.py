import os
import aiosqlite
from bot.build_embed import build
import discord
from discord.ui import View, Button, InputText, Modal
from bot.modals.views.button import button_view
import asyncio


class Setup:
    @staticmethod
    async def check(ctx):
        embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 1/6**", 0xFF0000)
        view = button_view(ctx, "Role ID of Sellers", "ID")
        print(embed)
        await ctx.edit(embed=embed, view=view)
    
    async def create_channel(ctx, username, price, profile, payment_methods):
        try: 
            async with aiosqlite.connect('./database/database.db') as database:
                async with database.execute('''SELECT category_id_account FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                    result = await cursor.fetchone()
                    account_cat = result[0]
                
                
                category = discord.utils.get(ctx.guild.categories, id=account_cat)
                account_chan = await category.create_text_channel(f"{username} | {price}")
                embed = await build('Account Listed', f'# https://discord.com/channels/{ctx.guild.id}/{account_chan.id}', 0x0CFF00)
                await ctx.respond(embed=embed)

                
                await database.execute(
                    '''
                    INSERT INTO account (
                        guild_id, channel_id, ign, price, seller_id
                    ) VALUES (?, ?, ?, ?, ?)
                    ''',
                    (ctx.guild.id, account_chan.id, username, price, ctx.author.id)
                )
                
        except Exception as error:
            embed = await build("Database Error", error, 0xFF0000)
            await ctx.send(embed=embed)