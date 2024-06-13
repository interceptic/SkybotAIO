import aiohttp
import discord
import datetime
from minecraft.pricing.data_handler import user_stats, handle_stats
from minecraft.info.username import user_data
from discord.ui import Select, View
class Embed:
    def __init__(self):
        self = self

    async def send_embed(self, ctx, username):
        global returned_value
        self.username = username
        embed = discord.Embed(
                        title = f"**Skyblock Value**",
                        description = f"**Price Breakdown: **",
                        color=0x00F3FF
                        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        uuid = await user_data(username)
        print(uuid)
        embed.thumbnail = f"https://mc-heads.net/head/{uuid['id']}.png/"   
        data = await user_stats(username)
        self.data = data
        self.select = Select(placeholder='Profile')    
        for i in data[username]['names']:
            # TODO: if i != data[username]['names'][0]:
            self.select.add_option(label=f'{i}')
        view = View()
        view.add_item(self.select)
        
        embed.add_field(name="**Total Price**", value = "$0", inline=False)
        embed.add_field(name="**Networth**", value = "$0")
        embed.add_field(name="**HOTM**", value = "$0")
        embed.add_field(name='**Catacombs**', value='$0')
        embed.add_field(name='**Skills**', value='$0')
        embed.add_field(name='**Slayers**', value='$0')
        embed.add_field(name='**Crimson Isle**', value='$0')

        self.select.callback = self.returned_value
        await ctx.send(embed=embed, view=view)

    async def returned_value(self, interaction):
            name = self.select.values[0]
            self.important, pointless_var = await handle_stats(name, self.username)
            await interaction.response.send_message(self.important)
