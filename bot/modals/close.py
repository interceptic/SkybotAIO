from discord.ext import commands
import discord, json, asyncio, aiosqlite
from bot.build_embed import build

async def close_ticket(ctx, ticket, bot, sold, amount):
    embed = await build("Closing Channel...", "Please wait while data is saved", 0x7A7878)
    response = await ctx.respond(embed=embed)
    try:
        if ticket is not None:
            channel = discord.utils.get(ctx.guild.channels, name=ticket)
        elif ticket is None:
            channel = ctx.channel
        async with aiosqlite.connect("./database/database.db") as database:
            async with database.execute('SELECT open_ticket_id FROM ticket WHERE guild_id = ? AND channel_id = ?', (ctx.guild.id, channel.id,)) as cursor:
                id = await cursor.fetchone()
            if id is None and amount is not None and sold is None:
                embed = await build('Ticket Not Found', f"Sorry, I can't find ``{channel.name}`` in the database, i will delete this channel anyway...", 0xFF0000)
                await response.edit(embed=embed)
                await asyncio.sleep(3.5)
                await channel.delete()
                async with aiosqlite.connect("./database/database.db") as database:
                    async with database.execute('''INSERT INTO ticket (coins, guild_id, channel_id)
                                                VALUES (?, ?, ?)
                                                ''', (amount, ctx.guild.id, channel.id,)) as cursor:
                        await database.commit()  
                        
                
                return
        embed = await build(f'Deleting channel...', 'Channel will be deleted in 10 seconds', 0xFF0000)
        await ctx.respond(embed=embed)
        await asyncio.sleep(10)
        await channel.delete()
        with open("ticket_management.json", 'r+') as ticket:
            the_json = json.load(ticket)
            the_json['ids'][str(ctx.guild.id)][str(id[0])] -= 1
            ticket.seek(0)  # Move the file pointer to the beginning of the file
            ticket.truncate()  # Truncate the file to remove the old content
            json.dump(the_json, ticket, indent=4)  # Dump the updated JSON content
        if sold is None and amount is not None:
            async with aiosqlite.connect("./database/database.db") as database:
                async with database.execute('UPDATE ticket SET coins = ? WHERE guild_id = ? AND channel_id = ?', (amount, ctx.guild.id, channel.id,)) as cursor:
                    await database.commit()  
                await database.execute('''
                UPDATE ticket
                SET channel_id = NULL
                WHERE guild_id = ? AND channel_id = ?
            ''', (ctx.guild.id, channel.id))
                await database.commit()
                    
                try:
                    await database.execute('''
                        DELETE FROM queue WHERE guild_id = ? AND channel_id = ?
                    ''', (ctx.guild.id, channel.id))
                    await database.commit()
                except Exception as error:
                    print('Error with queue', error)
                    return
        elif sold is not None and amount is None:
            channel = discord.utils.get(ctx.guild.channels, name=sold)
            await channel.send('# ACCOUNT SOLD')
            await asyncio.sleep(10)
            await channel.delete()

            
            
            #     CREATE TABLE IF NOT EXISTS [ticket] (
            #     [guild_id] INTEGER,
            #     [channel_id] INTEGER,
            #     [open_ticket_id] INTEGER,
            #     [coins] INT,
            #     [price] INTEGER,
            #     [seller_id] INTEGER
            # )
            
    except Exception as error:
        embed = await build('Exception Triggered', f"{error}", 0xFF0000)
        await response.edit(embed=embed)