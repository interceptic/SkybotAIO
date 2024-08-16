import discord
from discord.ext import commands
from discord.ui import Button, View
import aiosqlite
from bot.modals.buy import create_ticket
from discord import Guild
from bot.modals.calculator import random_action




async def handle_offers(ctx, account, offer, payment_method, clear, bot):
    channel = discord.utils.get(ctx.guild.channels, name=account)
    print('gathered channel')
    
    async with aiosqlite.connect("./database/database.db") as database:
        async with database.execute('SELECT offer, seller_id FROM account WHERE guild_id = ? AND channel_id = ?', (ctx.guild.id, channel.id,)) as cursor:
            row = await cursor.fetchone()
            value = row[0]
            seller_id = row[1]
            print('gathered c/o and seller id')
        async with database.execute('SELECT seller_id FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
            seller_role = await cursor.fetchone()
    role = discord.utils.get(ctx.author.roles, id=seller_role[0])
    print('gathered role')
    if role is not None and clear:
        offer = 0 
        async for message in channel.history(limit=30):
            if 'Current Offer' in message.content:
                await message.edit(f"# :bar_chart: Current Offer: ${offer}")
                await ctx.respond('Offers have been cleared!', ephemeral=True)

    if seller_id == ctx.author.id:
        await ctx.respond("Sorry, you're not able to offer on your own account", ephemeral=True)
        return
    
    else:        
        print('reading content')
        async for message in channel.history(limit=30):
            if 'Current Offer' in message.content:
                if not offer % 5 == 0:
                    await ctx.respond('# Sorry, offers need to be a multiple of 5', ephemeral = True)
                    return
                if not offer - value >= 5:
                    await ctx.respond('# Sorry, offers need to be atleast $5 USD more than the last offer', ephemeral = True)
                    return

                print('Editing Content')
                await message.edit(f"# :bar_chart: Current Offer: ${offer}")
                await ctx.respond(f"**You successfully placed an offer of ${offer}.**", ephemeral=True)
                user = await bot.fetch_user(seller_id)
                dm = await user.create_dm()
                
                        
                                
                
                
                await dm.send(f"<@{ctx.author.id}> has offered ${offer} on https://discord.com/channels/{ctx.guild.id}/{channel.id}, with a payment method of {payment_method}")
            elif 'Not taking offers, Price is Non-Negotiable' in message.content:
                await ctx.respond('# Sorry, this account is not currently accepting offers.', ephemeral=True)



    async with aiosqlite.connect("./database/database.db") as database:
        async with database.execute('UPDATE account SET offer = ? WHERE guild_id = ? AND channel_id = ?', (offer, ctx.guild.id, channel.id,)) as cursor:
            await database.commit()  
    return
        
           
            
    
