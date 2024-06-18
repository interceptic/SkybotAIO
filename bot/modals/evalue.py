import aiohttp
import discord
import datetime
from minecraft.pricing.data_handler import user_stats, handle_stats
from minecraft.info.username import user_data
from minecraft.pricing.price_data import pricer
from discord.ui import Select, View
class Embed:
    def __init__(self):
        self = self

    async def send_embed(self, ctx, username):
        global returned_value
        self.list = []
        self.username = username
        data = await user_stats(ctx, username)
        self.data = data
        for s in data[username]['profiles']:
            if data[username]['profiles'][s]['current'] == True:
                active_profile = s
                self.name = data[username]['profiles'][active_profile]['cute_name']
                self.list.append(s)
        
        embed = discord.Embed(
                        title = f"**Price Breakdown**",
                        description = f"[{self.username}: {self.name}](https://sky.shiiyu.moe/stats/{self.username}/{self.name})",
                        color=0xFFFFFF
                        )
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        self.uuid = await user_data(ctx, username)
        embed.thumbnail = f"https://mc-heads.net/head/{self.uuid['id']}.png/"   
        
        self.important, pointless_var = await handle_stats(self.name, self.username)
        self.priced, more_var = await pricer(self.important, self.username)

        self.select = Select(placeholder='Profile')    
        for i in data[username]['names']:
            if i != self.name and len(self.list) != 1:
                self.select.add_option(label=f'{i}')
            elif len(self.list) == 1:
                self.select.add_option(label=f"{i}")
        view = View()
        view.add_item(self.select)
        self.ctx = ctx

        embed.add_field(name="**Total Price**", value = f"${round(self.priced[self.username]['total'], 2)}", inline=False)
        embed.add_field(name="**Networth**", value = f"${round(self.priced[self.username]['total_nw'], 2)}")
        embed.add_field(name='**Catacombs**', value=f"${round(self.priced[self.username]['cata']['level'], 2)}")  
        embed.add_field(name="**HOTM**", value = f"${round(self.priced[self.username]['total_hotm'], 2)}")
        embed.add_field(name='**Crimson Isle**', value=f"${round(self.priced[self.username]['total_crimson'], 2)}")
        embed.add_field(name='**Slayers**', value=f"${round(self.priced[self.username]['total_slayers'], 2)}")
        embed.add_field(name='**Skills**', value=f"${round(self.priced[self.username]['total_skills'], 2)}")
        


        self.select.callback = self.returned_value
        await ctx.edit(embed=embed, view=view)

    async def returned_value(self, interaction):
        if self.ctx.author.id != interaction.user.id:
            return
        name = self.select.values[0]
        self.name = name
        self.important, pointless_var = await handle_stats(name, self.username)
        self.priced, more_var = await pricer(self.important, self.username)
        await Embed.more_profiles(self)

    async def more_profiles(self):
        
        self.select.options = []
        for i in self.data[self.username]['names']:
            if i != self.name and len(self.list) != 1:
                self.select.add_option(label=f'{i}')
            elif len(self.list) == 1:
                self.select.add_option(label=f"{i}")
        self.select.placeholder = self.name        
        
        self.important, pointless_var = await handle_stats(self.name, self.username)
        self.priced, more_var = await pricer(self.important, self.username)
        
        embed = discord.Embed(
            title = f"**Price Breakdown**",
            description = f"[{self.username}: {self.name}](https://sky.shiiyu.moe/stats/{self.username}/{self.name})",
            color=0xFFFFFF)
        embed.set_footer(text='Made by interceptic', icon_url='https://cdn.discordapp.com/avatars/1227394151847297148/a_17e8e189d32a91dc7a40f25a1ebcd9c0.webp?size=160')
        embed.timestamp = datetime.datetime.now()
        embed.thumbnail = f"https://mc-heads.net/head/{self.uuid['id']}.png/"   
        view = View()
        view.add_item(self.select)
        embed.add_field(name="**Total Price**", value = f"${round(self.priced[self.username]['total'], 2)}", inline=False)
        embed.add_field(name="**Networth**", value = f"${round(self.priced[self.username]['total_nw'], 2)}")
        embed.add_field(name='**Catacombs**', value=f"${round(self.priced[self.username]['cata']['level'], 2)}")  
        embed.add_field(name="**HOTM**", value = f"${round(self.priced[self.username]['total_hotm'], 2)}")
        embed.add_field(name='**Crimson Isle**', value=f"${round(self.priced[self.username]['total_crimson'], 2)}")
        embed.add_field(name='**Slayers**', value=f"${round(self.priced[self.username]['total_slayers'], 2)}")
        embed.add_field(name='**Skills**', value=f"${round(self.priced[self.username]['total_skills'], 2)}")
        


        self.select.callback = self.returned_value
        await self.ctx.edit(embed=embed, view=view)
        await self.ctx.respond(f'Profile changed to **{self.name}**', ephemeral=True)