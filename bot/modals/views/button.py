import discord
from discord.ui import View, Button, InputText, Modal
import aiosqlite
from bot.modals.views.button2 import button2
from bot.build_embed import build

def button_view(discord_int, title, label):
    open_menu_button = Button(label=title, style=discord.ButtonStyle.blurple)
    async def input_text_callback(interaction):
        class InputModal(Modal):
            def __init__(self):
                super().__init__(title=title)
                self.add_item(InputText(label=label))

            async def callback(self, int1: discord.interactions.Interaction):
                user_input = self.children[0].value
                
                
                await int1.response.defer()
                await button2(discord_int, "Account Category ID", "ID", user_input)
                

        await interaction.response.send_modal(InputModal())

    open_menu_button.callback = input_text_callback
    
    view = View()
    view.add_item(open_menu_button)
    return view