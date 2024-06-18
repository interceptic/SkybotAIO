import discord
from discord.ui import View, Button, InputText, Modal
from bot.modals.views.button3 import button3
from bot.build_embed import build


async def button2(discord_int, title, label):
    open_menu_button = Button(label=title, style=discord.ButtonStyle.blurple)

    async def input_text_callback(interaction):
        class InputModal(Modal):
            def __init__(self):
                super().__init__(title=title)
                self.add_item(InputText(label=label))

            async def callback(self, interaction: discord.Interaction):
                global embed
                user_input = self.children[0].value
                await button3(discord_int, "Profile Category ID", "ID")
        await interaction.response.send_modal(InputModal())

    open_menu_button.callback = input_text_callback
    
    view = View()
    view.add_item(open_menu_button)
    embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 2/3**", 0xFF0000)
    await discord_int.edit(embed=embed, view=view)
