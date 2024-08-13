from discord.ext import commands
import discord
import aiosqlite, json
from bot.modals.evalue import Embed
from bot.build_embed import build
from minecraft.info.tmbk import representTBMK

async def create_ticket(ctx, account, bot, the_json, payment_method):
    embed = await build("Creating Channel...", "Please wait while everything is setup", 0x7A7878)
    response = await ctx.respond(embed=embed, ephemeral=True)
    with open("ticket_management.json", 'r+') as ticket:
        the_json['ids'][str(ctx.guild.id)][str(ctx.author.id)] += 1
        json.dump(the_json, ticket, indent=4)
    try:
        channel = discord.utils.get(ctx.guild.channels, name=account)
        async for message in channel.history(limit=10):
            if message.embeds:
                embed = message.embeds #fetches embed 
    
        async with aiosqlite.connect("./database/database.db") as database:
            async with database.execute('SELECT seller_id, ign FROM account WHERE guild_id = ? AND channel_id = ?', (ctx.guild.id, channel.id)) as cursor:
                value = await cursor.fetchone()
                
            async with database.execute('''SELECT category_id_buy FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                result = await cursor.fetchone()
                buy_cat = result[0]
        seller = value[0] # defines seller id
        seller = await bot.fetch_user(seller)
        buyer = await bot.fetch_user(ctx.author.id)
        
        if ctx.guild.id != 1227804021142589512:
            category = discord.utils.get(ctx.guild.categories, id=buy_cat)
        else: 
            category = discord.utils.get(ctx.guild.categories, id=1233558946611200051)
        
        
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        }
        
        buy_ticket = await category.create_text_channel(f"Buy {account}-{seller.name}", overwrites=overwrites)
        await buy_ticket.set_permissions(buyer, read_messages=True, send_messages=True)
        await buy_ticket.set_permissions(seller, read_messages=True, send_messages=True)
        
        await buy_ticket.send(f"**<@{ctx.author.id}> is interested in buying https://discord.com/channels/{ctx.guild.id}/{channel.id} with payment method: {payment_method}**")

        async for message in channel.history(limit=10):
            if message.embeds:
                for embed in message.embeds:
                    await buy_ticket.send(embed=embed)#fetches embed 
                    
        ign = value[1]            
        await buy_ticket.send(f"**<@{seller.id}>, the first character of the account is {ign[0]}, and the last is {ign[-1]}**")
        embed = await build("Ticket Created", f"Your ticket has been created, you can find it here: https://discord.com/channels/{ctx.guild.id}/{buy_ticket.id}", 0x2FF100)
        await response.edit(embed=embed)
        
        async with aiosqlite.connect("./database/database.db") as database:
            await database.execute('''
            INSERT INTO ticket (guild_id, channel_id, open_ticket_id)
            VALUES (?, ?, ?)
        ''', (ctx.guild.id, buy_ticket.id, ctx.author.id))
            await database.commit()
            
            
    except Exception as error:
        embed = await build('Exception Triggered', f"{error}", 0xFF0000)
        await response.edit(embed=embed)
    
        
async def create_ticket_coins(ctx, amount, bot, the_json, payment_method):
    embed = await build("Creating Channel...", "Please wait while everything is setup", 0x7A7878)
    response = await ctx.respond(embed=embed, ephemeral=True)
    try:
        with open("ticket_management.json", 'r+') as ticket:
            the_json['ids'][str(ctx.guild.id)][str(ctx.author.id)] += 1
            json.dump(the_json, ticket, indent=4)
        async with aiosqlite.connect("./database/database.db") as database:
            async with database.execute('''SELECT category_id_buy, seller_id, coin_price_sell FROM info WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                result = await cursor.fetchone()
                buy_cat = result[0]
                seller_role = result[1]
                price = result[2]
        try:
            if ctx.guild.id != 1227804021142589512:
                category = discord.utils.get(ctx.guild.categories, id=buy_cat)
            else: 
                category = discord.utils.get(ctx.guild.categories, id=1233558945176752220)
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            }
        except Exception as error:
            embed = await build('Ticker Error', f"{error}", 0xFF0000)
            await ctx.respond(embed=embed)
            return
        
        try:
            seller_role = ctx.guild.get_role(seller_role)
            user = await bot.fetch_user(ctx.author.id)
        except Exception as error:
            embed = await build('Ticker Error', f"{error}", 0xFF0000)
            await ctx.respond(embed=embed)
            return
        if ctx.guild.id == 1227804021142589512 and amount < 300:
            price = 0.08
        elif ctx.guild.id == 1227804021142589512 and amount >= 300 and amount < 600:
            price = 0.06
        elif ctx.guild.id == 1227804021142589512 and amount >= 600:
            price = 0.045
        
        tmbk = representTBMK(amount * 1000000)
        buy_ticket = await category.create_text_channel(f"buy｜coins｜{amount}M", overwrites=overwrites)
        await buy_ticket.set_permissions(ctx.author, read_messages=True, send_messages=True)
        await buy_ticket.set_permissions(seller_role, read_messages=True, send_messages=True)
        embed = await build(f"{ctx.author.name} | Buy | {tmbk} | ${round(amount * price,2)}", f"<@{ctx.author.id}> is interested in buying {tmbk} for ${round(amount * price,2)}\nPayment Method: **{payment_method}**", 0xFFFFFF)
        await buy_ticket.send(embed=embed)
        await buy_ticket.send('# Please state your in game name, aswell as any other important information.')
        message = await buy_ticket.send(f"<@{ctx.author.id}>, <@&{seller_role.id}>")
        await message.delete()
        
        
        embed = await build("Ticket Created", f"Your ticket has been created, you can find it here: https://discord.com/channels/{ctx.guild.id}/{buy_ticket.id}", 0x2FF100)
        await response.edit(embed=embed)
        
        async with aiosqlite.connect("./database/database.db") as database:
            await database.execute('''
            INSERT INTO ticket (guild_id, channel_id, open_ticket_id)
            VALUES (?, ?, ?, ?)
        ''', (ctx.guild.id, buy_ticket.id, ctx.author.id))
            await database.commit()
        

    except Exception as error:
        embed = await build('Exception Triggered', f"{error}", 0xFF0000)
        await response.edit(embed=embed)