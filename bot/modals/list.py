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


class Setup:
    @staticmethod
    async def check(ctx):
        embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 1/6**", 0xFF0000)
        view = button_view(ctx, "Role ID of Sellers", "ID")
        print(embed)
        await ctx.edit(embed=embed, view=view)
    
    async def create_channel(ctx, username, price, profile, payment_methods):
        
        data = await user_stats(ctx, username)
        for s in data[username]['profiles']:
            if data[username]['profiles'][s]['current'] == True:
                active_profile = s
                cute_name = data[username]['profiles'][active_profile]['cute_name']
        important, rank = await handle_stats(cute_name, username)
        channel_embed = await build("Hypixel Skyblock Information", "Placeholder", 0xFF0000)

        try: 
            async with aiosqlite.connect('./database/database.db') as database:
                async with database.execute('''SELECT category_id_account FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                    result = await cursor.fetchone()
                    account_cat = result[0]
                
                
                category = discord.utils.get(ctx.guild.categories, id=account_cat)
                account_chan = await category.create_text_channel(f"💲{price}｜⭐{important[username]['level']}")
                embed = await build(f'{username} Listed', f'**{username} listed for ${price} - https://discord.com/channels/{ctx.guild.id}/{account_chan.id}**', 0x0CFF00)
                await asyncio.sleep(2)
                await ctx.respond(embed=embed, ephemeral=True)
                
                
                ranks = "MVP++"
                thumbnail = "images/mvp++_rank.png"
                if rank == 'MVP+':
                    ranks = '<:mvp0:1209162125390643210><:mvp1:1209158437833941173>'
                    thumbnail = "images/mvp+_rank.png"
                elif rank == 'MVP':
                    ranks = 'MVP'
                    thumbnail = "images/mvp_rank.png"
                elif rank == 'VIP+':
                    ranks = '<:vip0:1209164508413820948><:vip1:1209164538247647236>'
                    thumbnail = "images/vip+_rank.png"
                elif rank == 'VIP':
                    ranks = VIP
                    thumbnail = "images/vip_rank.png"
                elif rank == 'NON':
                    ranks = 'NON'
                    thumbnail = "images/non_rank.png"
                
                embed = await build("Hypixel Skyblock Information", f"Rank: {ranks}", 0xFF4CAE)
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
                embed.add_field(name="<:6p:1208902204614778941> Networth", value=f"Total: **{representTBMK(important[username]['networth']['unsoulbound'] + important[username]['networth']['soulbound'])}**\nUnsoulbound: **{representTBMK(important[username]['networth']['unsoulbound'])}**\nSoublound: **{representTBMK(important[username]['networth']['soulbound'])}**")
                embed.add_field(name=":scroll: Details", value=f"Owner: <@{ctx.author.id}>\n **Payment Methods: {payment_methods}**")
                # embed.add_field(name='<:magma:1209615107391361025> **Crimson Isle**', value=f"Faction: **{info['faction']}**\n<:Mage:1209035626381447178> Mage Reputation: **{info['mages_reputation']}**\n<:Barbarian:1209035674301243402> Barbarian Reputation: **{info['barbarians_reputation']}**")
                # embed.add_field(name=":pen_ballpoint: Extra Info", value=f'**{extra_info}**')
                embed.thumbnail= f"{thumbnail}"

                await asyncio.sleep(2)
                await account_chan.send(embed=embed)

                
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