import discord
from discord.ui import View, Button, InputText, Modal
from bot.build_embed import build
import aiosqlite


async def button6(discord_int, title, label, seller_role, account_cat, profile_cat, buy_price, sell_price):
    open_menu_button = Button(label=title, style=discord.ButtonStyle.blurple)

    async def input_text_callback(interaction):
        class InputModal(Modal):
            def __init__(self):
                super().__init__(title=title)
                self.add_item(InputText(label=label))

            async def callback(self, interaction: discord.Interaction):
                global embed
                ticket_cat = self.children[0].value
                await interaction.response.defer()
                guild_id = discord_int.guild.id
                try:
                    async with aiosqlite.connect('./database/database.db') as database:
                        await database.execute(
                            '''
                            INSERT INTO info (
                                guild_id, seller_id, category_id_account, category_id_profile, category_id_tickets, coin_price_buy, coin_price_sell
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)
                            ''',
                            (guild_id, seller_role, account_cat, profile_cat, ticket_cat, buy_price, sell_price)
                        )
                        await database.commit()
                except Exception as error:
                    embed = await build('Error Setting up database', f"{error}", 0xFF0000)
                    await discord_int.edit(embed=embed)
                    return
                embed = await build("Database Setup!", "Run the /list command again to list your account!", 0x0CFF00)
                view = View()
                await discord_int.edit(embed=embed, view=view)
                return
               
        await interaction.response.send_modal(InputModal())

    open_menu_button.callback = input_text_callback
    
    view = View()
    view.add_item(open_menu_button)
    embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 6/6**", 0xFF0000)
    await discord_int.edit(embed=embed, view=view)
