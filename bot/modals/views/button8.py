import discord
from discord.ui import View, Button, InputText, Modal
from bot.build_embed import build
from bot.modals.views.button9 import button9


async def button8(discord_int, title, label, seller_role, account_cat, profile_cat, buy_price, sell_price, ticket_cat_buy, ticket_cat_sell):
    open_menu_button = Button(label=title, style=discord.ButtonStyle.blurple)

    async def input_text_callback(interaction):
        class InputModal(Modal):
            def __init__(self):
                super().__init__(title=title)
                self.add_item(InputText(label=label))

            async def callback(self, interaction: discord.Interaction):
                global embed
                user_input = self.children[0].value
                await interaction.response.defer()
               
                await button9(discord_int, "Vouch Channel ID", "ID", seller_role, account_cat, profile_cat, buy_price, sell_price, ticket_cat_buy, ticket_cat_sell, user_input)
        await interaction.response.send_modal(InputModal())

    open_menu_button.callback = input_text_callback
    
    view = View()
    view.add_item(open_menu_button)
    embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 8/9**", 0xFF0000)
    await discord_int.edit(embed=embed, view=view)
