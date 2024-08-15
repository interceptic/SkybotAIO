import aiosqlite, discord, json
from discord.ext import commands
from bot.modals.evalue import Embed
from bot.build_embed import build
from minecraft.info.tmbk import representTBMK
from minecraft.pricing.data_handler import user_stats, handle_stats
from minecraft.info.username import user_data
from minecraft.pricing.price_data import pricer
from discord import Guild

async def sell_account(ctx, username, price, bot, the_json, payment_method):
    try:
        embed = await build("Creating Channel...", "Please wait while everything is setup", 0x7A7878)
        response = await ctx.respond(embed=embed, ephemeral=True)
        async with aiosqlite.connect("./database/database.db") as database:
            async with database.execute('''SELECT category_id_sell, seller_id, coin_price_buy FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                result = await cursor.fetchone()
                sell_cat = result[0]
                seller_id = result[1]
                sell_price = result[2]
        if ctx.guild.id != 1227804021142589512:
            category = discord.utils.get(ctx.guild.categories, id=sell_cat)
        else: 
            category = discord.utils.get(ctx.guild.categories, id=1233558947328167946)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        }
        
        data = await user_stats(ctx, username)
        for s in data[username]['profiles']:
            if data[username]['profiles'][s]['current'] == True:
                active_profile = s
                cute = data[username]['profiles'][active_profile]['cute_name']

        uuid = await user_data(ctx, username)
        important, dumb_var = await handle_stats(cute, username)
        priced, dumb_var = await pricer(important, username)
        
        sell_ticket = await category.create_text_channel(f"sell｜account｜{username}", overwrites=overwrites)
        try:
            seller_role = ctx.guild.get_role(seller_id)
            user = await bot.fetch_user(ctx.author.id)
        except Exception as error:
            embed = await build('Ticker Error', f"{error}", 0xFF0000)
            await ctx.respond(embed=embed)
            return
        await sell_ticket.set_permissions(ctx.author, read_messages=True, send_messages=True)
        await sell_ticket.set_permissions(seller_role, read_messages=True, send_messages=True)
        embed = await build(f"Account | Sell | {username}", f"**<@{ctx.author.id}> wants ${round(price)} USD for account: {username}**\nPayment Method: **{payment_method}**", 0xFFFFFF)
        await sell_ticket.send(embed=embed)
        embed = await build("Account Value", f"[{username}: {cute}](https://sky.shiiyu.moe/stats/{username}/{cute})", 0xFFFFFF)
        embed.add_field(name="**Total Price**", value = f"${round(priced[username]['total'], 2)}", inline=False)
        embed.add_field(name="**Networth**", value = f"${round(priced[username]['total_nw'], 2)}")
        embed.add_field(name='**Catacombs**', value=f"${round(priced[username]['cata']['level'], 2)}")  
        embed.add_field(name="**HOTM**", value = f"${round(priced[username]['total_hotm'], 2)}")
        embed.add_field(name='**Crimson Isle**', value=f"${round(priced[username]['total_crimson'], 2)}")
        embed.add_field(name='**Slayers**', value=f"${round(priced[username]['total_slayers'], 2)}")
        embed.add_field(name='**Skills**', value=f"${round(priced[username]['total_skills'], 2)}")
        embed.set_thumbnail(url=f"https://mc-heads.net/head/{uuid['id']}.png/"   )
        
        await sell_ticket.send(embed=embed)
        embed = await build(f"Recommended Buy Price: ${round(priced[username]['total'] * 0.65, 2)}", "**A seller will likely offer at or near this price**", 0xFFFFFF)
        await sell_ticket.send(embed=embed)
        embed = await build("Ticket Created", f"Your ticket has been created, you can find it here: https://discord.com/channels/{ctx.guild.id}/{sell_ticket.id}", 0x2FF100)
        await response.edit(embed=embed)
        message = await sell_ticket.send(f"<@{ctx.author.id}>, <@&{seller_role.id}>")
        await message.delete()
        
        with open("ticket_management.json", 'r+') as ticket:
            the_json['ids'][str(ctx.guild.id)][str(ctx.author.id)] += 1
            json.dump(the_json, ticket, indent=4)
            
        async with aiosqlite.connect("./database/database.db") as database:
            await database.execute('''
            INSERT INTO ticket (guild_id, channel_id, open_ticket_id)
            VALUES (?, ?, ?)
        ''', (ctx.guild.id, sell_ticket.id, ctx.author.id))
            await database.commit()
        
    except Exception as error:
        embed = await build('Exception Caught', f"{error}", 0xFF0000)
        await response.edit(embed=embed) 

async def sell_coins(ctx, amount, bot, the_json, payment_method):
    try:
        embed = await build("Creating Channel...", "Please wait while everything is setup", 0x7A7878)
        response = await ctx.respond(embed=embed, ephemeral=True)
        async with aiosqlite.connect("./database/database.db") as database:
            async with database.execute('''SELECT category_id_sell, seller_id, coin_price_buy FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                result = await cursor.fetchone()
                sell_cat = result[0]
                seller_id = result[1]
                sell_price = result[2]
        if ctx.guild.id != 1227804021142589512:
            category = discord.utils.get(ctx.guild.categories, id=sell_cat)
        else: 
            category = discord.utils.get(ctx.guild.categories, id=1233558945789120593)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        }
        sell_ticket = await category.create_text_channel(f"sell｜coins｜{amount}M", overwrites=overwrites)
        seller_role = ctx.guild.get_role(seller_id)
        await sell_ticket.set_permissions(ctx.author, read_messages=True, send_messages=True)
        await sell_ticket.set_permissions(seller_role, read_messages=True, send_messages=True)
        tmbk = representTBMK(amount * 1000000)
        embed = await build(f"Sell | Coin | {tmbk}", f"**<@{ctx.author.id}> wants to sell {tmbk} Coins for ${round(amount * sell_price, 2)} USD**\nPayment Method: **{payment_method}**", 0xFFFFFF)
        await sell_ticket.send(embed=embed)
        embed = await build("Ticket Created", f"Your ticket has been created, you can find it here: https://discord.com/channels/{ctx.guild.id}/{sell_ticket.id}", 0x2FF100)
        await response.edit(embed=embed)
        message = await sell_ticket.send(f"<@{ctx.author.id}>, <@&{seller_role.id}>")
        await message.delete()
        with open("ticket_management.json", 'r+') as ticket:
            the_json['ids'][str(ctx.guild.id)][str(ctx.author.id)] += 1
            json.dump(the_json, ticket, indent=4)
        async with aiosqlite.connect("./database/database.db") as database:
            await database.execute('''
            INSERT INTO ticket (guild_id, channel_id, open_ticket_id)
            VALUES (?, ?, ?)
        ''', (ctx.guild.id, sell_ticket.id, ctx.author.id))
            
            await database.execute('''
            INSERT INTO queue (guild_id, channel_id, coins)
            VALUES (?, ?, ?)
        ''', (ctx.guild.id, sell_ticket.id, amount))
            
            
            await database.commit()
        

    except Exception as error:
        embed = await build('Exception Caught', f"{error}", 0xFF0000)
        await response.edit(embed=embed) 