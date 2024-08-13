import discord
from discord.ui import View, Button, InputText, Modal
from bot.build_embed import build
from bot.modals.views.button5 import button5


async def button4(discord_int, title, label, seller_role, account_cat, profile_cat):
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
               
                await button5(discord_int, "Coin Price that YOU will sell for", "Price", seller_role, account_cat, profile_cat, user_input)
        await interaction.response.send_modal(InputModal())

    open_menu_button.callback = input_text_callback
    
    view = View()
    view.add_item(open_menu_button)
    embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 4/9**", 0xFF0000)
    await discord_int.edit(embed=embed, view=view)
