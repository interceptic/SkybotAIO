import os
import aiosqlite
from bot.build_embed import build
import discord
from discord.ui import View, Button, InputText, Modal
from bot.modals.views.button import button_view
import asyncio
from minecraft.pricing.data_handler import user_stats, handle_stats
from minecraft.info.username import user_data
from minecraft.info.tmbk import representTBMK
import json
from discord import Guild


class Setup:
    
    @staticmethod
    async def check(ctx):
        if not ctx.author.guild_permissions.administrator:
            await ctx.respond('Sorry, you need admin permissions to setup the database', ephemeral=True)
            return
        embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 1/9**", 0xFF0000)
        view = button_view(ctx, "Role ID of Sellers", "ID")
        print(embed)
        await ctx.edit(embed=embed, view=view)
    
    async def create_channel(ctx, username, price, profile, payment_methods, extra_info, offers):
        data = await user_stats(ctx, username)
        
        for s in data[username]['profiles']:
            if data[username]['profiles'][s]['current'] == True:
                active_profile = s
                cute_name = data[username]['profiles'][active_profile]['cute_name']
        important, rank = await handle_stats(cute_name, username)
        channel_embed = await build("Hypixel Skyblock Information", "Placeholder", 0xFF0000)

        try:
            async with aiosqlite.connect('./database/database.db') as database:
                
                if not profile: 
                    async with database.execute('''SELECT category_id_account FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                        result = await cursor.fetchone()
                        account_cat = result[0]
                elif profile: 
                    async with database.execute('''SELECT category_id_profile FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                        result = await cursor.fetchone()
                        account_cat = result[0]  
                
                
                
                category = discord.utils.get(ctx.guild.categories, id=account_cat)
                if not profile:
                    account_chan = await category.create_text_channel(f"💲{price}｜⭐{important[username]['level']}")
                if profile:
                    account_chan = await category.create_text_channel(f"💲{price}")
                embed = await build(f'{username} Listed', f'**{username} listed for ${price} - https://discord.com/channels/{ctx.guild.id}/{account_chan.id}**', 0x0CFF00)
                await asyncio.sleep(2)
                await ctx.respond(embed=embed, ephemeral=True)
                
                
                if payment_methods == '':
                    payment_methods = "None Provided"
                
                if extra_info == '':
                    extra_info = "None Provided"
                
                ranks = "MVP++"
                thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/mvp++_rank.png?raw=true"
                if rank == 'MVP+':
                    ranks = '<:mvp0:1209162125390643210><:mvp1:1209158437833941173>'
                    thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/mvp+_rank.png?raw=true"
                elif rank == 'MVP':
                    ranks = 'MVP'
                    thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/mvp_rank.png?raw=true"
                elif rank == 'VIP+':
                    ranks = '<:vip0:1209164508413820948><:vip1:1209164538247647236>'
                    thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/vip+_rank.png?raw=true"
                elif rank == 'VIP':
                    ranks = 'VIP'
                    thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/vip_rank.png?raw=true"
                elif rank == 'NON':
                    ranks = 'NON'
                    thumbnail = "https://github.com/interceptic/SkyblockValueParser/blob/main/images/non_rank.png?raw=true"
                if not profile:
                    embed = await build("Hypixel Skyblock Information", f"Rank: {ranks}", 0x1D0FC7)
                    embed.add_field(name="<:3p:1208902333719781497> Skyblock Level", value=f"**{important[username]['level']}**")
                    embed.add_field(name="<:sword:1208909044106920026> Skill Average", value=f"**{important[username]['skills']['average']}**")

                    
                    
                    
                    slayer_string = ""
                    # transform all the levels into a "level / level / level" string
                    for _, level in important[username]['slayers'].items():
                        slayer_string += f"{level} / "
                    # remove the last " / "
                    slayer_string = slayer_string[:-3]


                    embed.add_field(name="<:4p:1208902286961680445> Slayer", value=f"**{slayer_string}**")
                    embed.add_field(name="<:7p:1208902172675411968> Weight", value=f"Senither: **{int(important[username]['weight']['senither'])}**\nLily: **{int(important[username]['weight']['lily'])}**")
                    embed.add_field(name="<:8p:1208902120934215770> Dungeons", value=f"Catacombs: **{important[username]['cata']['level']}**")
                    embed.add_field(name="<:2p:1208902431770017803> Minions", value=f"Total Slots: **{important[username]['minions']['total']}**\nBonus Slots: **{important[username]['minions']['bonus']}**")
                    embed.add_field(name="<:funny:1208908515846918204> Mining", value=f"HOTM Level: **{important[username]['hotm']['level']}**\nMithril Powder: **{representTBMK(important[username]['hotm']['mithril_powder'])}**\nGemstone Powder: **{representTBMK(important[username]['hotm']['gemstone_powder'])}**\nGlacite Powder: **{representTBMK(important[username]['hotm']['glacite_powder'])}**")
                    embed.add_field(name="<:6p:1208902204614778941> Networth", value=f"Total: **{representTBMK(important[username]['networth']['unsoulbound'] + important[username]['networth']['soulbound'])}**\nUnsoulbound: **{representTBMK(important[username]['networth']['unsoulbound'])}\n**Soulbound: **{representTBMK(important[username]['networth']['soulbound'])}**")
                    embed.add_field(name=":scroll: Details", value=f"Owner: <@{ctx.author.id}>\n **Payment Methods:** \n*{payment_methods}*")
                    embed.add_field(name='<:magma:1209615107391361025> **Crimson Isle**', value=f"Faction: **{important[username]['crimson']['faction']}**\n<:Mage:1209035626381447178> Mage Reputation: **{important[username]['crimson']['mage']}**\n<:Barbarian:1209035674301243402> Barbarian Reputation: **{important[username]['crimson']['barbarian']}**")
                    embed.add_field(name=":pen_ballpoint: Extra Info", value=f'*{extra_info}*')
                    embed.thumbnail= f"{thumbnail}"
                
                elif profile:
                    embed = await build("Hypixel Skyblock Profile Information", f"**Total Networth:** {representTBMK(important[username]['networth']['unsoulbound'] + important[username]['networth']['soulbound'])}", 0x1D0FC7)
                    embed.add_field(name="<:6p:1208902204614778941> Networth", value=f"Unsoulbound: **{representTBMK(important[username]['networth']['unsoulbound'])}**\nSoulbound: **{representTBMK(important[username]['networth']['soulbound'])}**\nPurse: **{representTBMK(data[username]['profiles'][active_profile]['data']['networth']['purse'] + data[username]['profiles'][active_profile]['data']['networth']['bank'])}**")
                    embed.add_field(name="<:2p:1208902431770017803> Minions", value=f"Total Slots: **{important[username]['minions']['total']}**")
                    if 'collections' not in data[username]['profiles'][active_profile]['data']:
                        collections = "**N/A (API ERROR)**"
                    else: 
                        collections = f"**{data[username]['profiles'][active_profile]['data']['collections']['maxedCollections']} / 84**"
                    embed.add_field(name="<:collections:1257437677536542832> Collections", value=f'Maxed Collections: {collections}')
                    embed.add_field(name=":scroll: Details", value=f"Owner: <@{ctx.author.id}>\n **Payment Methods:** \n*{payment_methods}*")
                    embed.add_field(name=":pen_ballpoint: Extra Info", value=f'*{extra_info}*')
                    if 'misc' not in data[username]['profiles'][active_profile]['data']:
                        embed.add_field(name="<:profile:1257440019073994884> Profile Upgrades", value="Island Size: **N/A**\nBonus Minion Slots: **N/A**\nBonus Guests: **N/A**\nAdditional Co-op Slots: **N/A**\nDaily Coin Allowance: **N/A**", inline=False)
                    else:
                        embed.add_field(name="<:profile:1257440019073994884> Profile Upgrades", value=f"Island Size: **{data[username]['profiles'][active_profile]['data']['misc']['profile_upgrades']['island_size']}**\nBonus Minion Slots: **{data[username]['profiles'][active_profile]['data']['misc']['profile_upgrades']['minion_slots']}**\nBonus Guests: **{data[username]['profiles'][active_profile]['data']['misc']['profile_upgrades']['guests_count']}**\nAdditional Co-op Slots: **{data[username]['profiles'][active_profile]['data']['misc']['profile_upgrades']['coop_slots']}**\nDaily Coin Allowance: **{(data[username]['profiles'][active_profile]['data']['misc']['profile_upgrades']['coins_allowance'] * 10000)}**", inline=False)
                    embed.thumbnail= f"https://mc-heads.net/body/anonymous"

                

                await asyncio.sleep(2)
                async with database.execute('SELECT ping_role FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
                    value = await cursor.fetchone()
                
                await account_chan.send(f'<@&{value[0]}>')
                await account_chan.send(embed=embed)
                await account_chan.send('**If you wish to buy, use the /buy command \nIf you wish to offer, use the /offer command; Please note that false offers will result in a ban, and offer increments must be a multiple of 5.**')

                
                await database.execute(
                    '''
                    INSERT INTO account (
                        guild_id, channel_id, ign, price, seller_id, offer, channel_name
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''',
                    (ctx.guild.id, account_chan.id, username, price, ctx.author.id, 0, account_chan.name)
                )
                print(account_chan.id)

                
                await database.commit()
                if offers:
                    await account_chan.send('# :bar_chart: Current Offer: $0') 
                    return
                
                
                await account_chan.send('# Not taking offers, Price is Non-Negotiable')   
                
            
                
        except Exception as error:
            embed = await build("Database Error", error, 0xFF0000)
            await ctx.send(embed=embed)