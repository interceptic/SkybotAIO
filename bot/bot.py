import discord, requests, asyncio, json, uuid, os, aiosqlite, datetime
from discord.ext import commands
from bot.modals.evalue import Embed
from bot.modals.admin import give_admin, remove_admin
from bot.modals.list import Setup
from bot.modals.calculator import calculate
from bot.build_embed import build
from minecraft.info.tmbk import representTBMK
from database.sqlite import setup_db
from bot.modals.aichat import openai_response
from bot.modals.offer import handle_offers
from bot.modals.buy import create_ticket, create_ticket_coins
from bot.modals.sell import sell_account, sell_coins
from bot.modals.close import close_ticket
from discord import Guild
from bot.modals.statistics import update_embed
from bot.modals.ansi import generate_ansi




intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
bot = commands.Bot(intents=intents, slash_command_prefix='/')  

@bot.event
async def on_ready():
    print('\x1b[32mLogged in!\x1b[0m')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Made by Interceptic"))
    await bot.sync_commands()
    asyncio.create_task(update_embed(bot))
    # guild = bot.get_guild(1227804021142589512)

    # channel = discord.utils.get(guild.channels, name='purchase')
    # await channel.send(embed=(await build('Commands', "Use this channel as a means to use commands.\n**/sell:** This command allows you to sell coins or an account.\n**/buy:** This command allows you to purchase coins and accounts.\n**/offer:** This command allows you to offer on accounts incase you're willing to wait.\n**/coins:** This command will tell you the price to sell or buy coins.", 0xFFFFFF)))

 

@bot.slash_command(name='value', description='Skyblock Account Value')
async def value(ctx, name: str): 
    embed = discord.Embed(
        title="Fetching...",
        description=f"Obtaining data from api, please wait...",
        color=0xFF007B
    )
    embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
    embed.timestamp = datetime.datetime.now()
    await ctx.respond(embed=embed)
    try:
        class_thing = Embed()
        await class_thing.send_embed(ctx, name)
    except Exception as error:
        print('Value:', error)



@bot.slash_command(name='admin', description='Give or remove admin from yourself...')
async def admin(ctx, remove: bool = False):
    with open("config.json") as conf:
        config = json.load(conf)
    if ctx.author.id != config['bot']['owner_discord_id']:
        await ctx.respond("Sorry, you're not allowed to use this command", ephemeral=True)
        return
    if remove: 
        await remove_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
        return 
    await give_admin(ctx, config['bot']['owner_discord_id'], config['bot']['admin_role_id'])
    return

@bot.slash_command(name='list', description="List an account")
async def list(ctx, username: str, price: int, profile: bool = False, payment_methods: str = '', extra_info: str = '', offers: bool = True):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    
    async with aiosqlite.connect('./database/database.db') as database:
        async with database.execute('SELECT seller_id FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
            value = await cursor.fetchone()
    role = discord.utils.get(ctx.guild.roles, id=value[0])
    if not role in ctx.author.roles:
        await ctx.respond('You need seller role to run this command', ephemeral=True)
        return

    
    
    setup = Setup
    await setup.create_channel(ctx, username, price, profile, payment_methods, extra_info, offers)

@bot.slash_command(name='coins', description="Calculate the price for coins")
async def coins(ctx, type: discord.Option(str, choices=["Buy", "Sell"]), amount: int):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    
    if type == "Sell":
        value = await calculate(ctx, amount, True)
        if value == False:
            embed = await build("Invalid Sell Amount", "Minimum amount to sell is 500 million.", 0xFF0000)
            await ctx.respond(embed=embed)
            return
        amount = representTBMK(amount * 1000000)    
        embed = await build(f"Price for {amount}", f"You can sell {amount} for ${round(value, 2)} USD", 0x00FFDC)
        await ctx.respond(embed=embed)
        return
    elif type == "Buy":
        value = await calculate(ctx, amount, False)
        amount = representTBMK(amount * 1000000)    
        embed = await build(f"Price for {amount}", f"You can buy {amount} for ${round(value, 2)} USD", 0x00FFDC)
        await ctx.respond(embed=embed)
        
# @bot.event
# async def ticket_autocomplete(ctx:discord.AutocompleteContext): 
#     try:
#         async with aiosqlite.connect('./database/database.db') as sqlite:
#             async with sqlite.execute('SELECT channel_id FROM ticket WHERE guild_id = ?', (ctx.interaction.guild.id,)) as cursor:
#                 rows = await cursor.fetchall()
#                 channel_ids = [str(row[0]) for row in rows]
#         if channel_ids == []:
#             return ['No Tickets Created']
#     except Exception as error:
#         print(f"\x1b[34m{error}\x1b[0m")
#         return ['Database Error, Contact Support']
#     names = []
#     for channel_id in channel_ids:
#         try:
#             channel = await bot.fetch_channel(int(channel_id))
#         except:
#             async with aiosqlite.connect('./database/database.db') as database:
#                 await database.execute('UPDATE ticket SET channel_id = NULL WHERE channel_id = ?', (channel_id,))
#                 await database.commit()
#         try:        
#             names.append(str(channel.name))
#         except:
#             pass


#     return names

async def guild_in_db(ctx):
    if not os.path.exists("./database/database.db"):
        await setup_db()
        return False
    async with aiosqlite.connect('./database/database.db') as sqlite:
        async with sqlite.execute('SELECT COUNT(*) FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
            result = await cursor.fetchone()
            exists = result[0] > 0  # This will be True if guild id exists, otherwise False
            return exists
        

@bot.event
async def on_application_command_autocomplete(ctx:discord.AutocompleteContext):
    try:
        async with aiosqlite.connect('./database/database.db') as sqlite:
            async with sqlite.execute('SELECT channel_id FROM account WHERE guild_id = ?', (ctx.interaction.guild.id,)) as cursor:
                rows = await cursor.fetchall()
                channel_ids = [str(row[0]) for row in rows]
        if channel_ids == []:
            return ['No Accounts Listed']
    except Exception as error:
        print(f"\x1b[34m{error}\x1b[0m")
        return ['Database Error, Contact Support']
    names = []
    channels = await ctx.interaction.guild.fetch_channels()

    for channel_id in channel_ids:
        for channel in channels:
            if channel.id == int(channel_id):
                names.append(str(channel.name))
            pass
    if ctx.value == "":
        return names
    current_input = ctx.value.lower()
    suggestions = []
    for i in range(0, len(names)):
        if current_input in names[i]:
            suggestions.append(names[i])
            
        
    if suggestions == []:
        suggestions = ['Could not find the account you are trying to reference']
    return suggestions
            

@bot.event
async def on_member_ban(guild, user):
    try:
        dm = await user.create_dm()
        await dm.send(f'You have been banned from {guild.name}. Were you scammed? - if so, create a support ticket here: https://fluxqol.com/join')
    except Exception as error:
        print('Ban:', error)

@bot.slash_command(name="delete", description="Delete an account")
async def delete(ctx, account: discord.Option(str, "Choose an Account", autocomplete=on_application_command_autocomplete)):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    
    if account == 'No Accounts Listed' or account == 'Database Error, Contact Support':
        await ctx.respond(account, ephemeral=True)
        return
    
    async with aiosqlite.connect("./database/database.db") as database:
        async with database.execute('SELECT seller_id FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
            value = await cursor.fetchone()
    role = discord.utils.get(ctx.guild.roles, id=value[0])
    if not role in ctx.author.roles:
        await ctx.respond('You need seller role to run this command', ephemeral=True)
        return
    channel = discord.utils.get(ctx.guild.channels, name=account)
    embed = await build(f'Deleting channel...', 'Channel will be deleted in 10 seconds', 0xFF0000)
    await ctx.respond(embed=embed)
    await asyncio.sleep(10)
    await channel.delete()
    async with aiosqlite.connect('./database/database.db') as database:
        async with database.execute('DELETE FROM account WHERE channel_id = ?', (channel.id,)) as cursor:
            await database.commit()
                

@bot.slash_command(name='buy', description='Purchase an Account / Profile')
async def buy(ctx, payment_method: discord.Option(str, "Choose a Payment Method", choices=["Cashapp", "Venmo", "Paypal", "LTC", "BTC", "Gift Card", "Other"]), account: discord.Option(str, "Choose what to buy", autocomplete=on_application_command_autocomplete)=None, coins: int=None):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    
    if account == 'No Accounts Listed' or account == 'Database Error, Contact Support':
        await ctx.respond(account, ephemeral=True)
        return
    
    if account is None and coins is None:
        await ctx.respond("Specify if you are buying an account, or if you're buying coins", ephemeral = True)
        return
    if account is not None and coins is not None:
        await ctx.respond("You can only create one ticket at a time, please specify if you're buying coins **or** an account", ephemeral = True)
        return    
    if account is not None:
        data = await ticket_json(ctx)
        if data is None:
            return
        await create_ticket(ctx, account, bot, data, payment_method)
        return
    if coins is not None:
        if coins > 10000:
            await ctx.respond(f'You can not buy more than 10B at once. please note that coins is in millions, so 10 is equal to 10 million', ephemeral=True)
            return
        if coins < 100:
            await ctx.respond(f'You can not buy less than 100M. please note that coins is in millions, so 10 is equal to 10 million', ephemeral=True)
            return
        
        data = await ticket_json(ctx)
        if data is None:
            return
        await create_ticket_coins(ctx, coins, bot, data, payment_method)
        return
    
    


@bot.event
async def on_message(message):
    
    if message.author.id == bot.user.id and message.channel.id != 1259269840066318428:
        return
    if 'add bot' in message.content:
        await message.reply('https://discord.com/oauth2/authorize?client_id=1250030190617165824&permissions=8&integration_type=0&scope=bot')
    if '!tips' in message.content:
        embed = await build('Bot Tips', "I'm built with many useful commands, heres a rundown:```1. /ansi - this will create a message you can use to advertise your accounts```\n\n```2. /coins - this command allows you to calculate the price of coins```\n\n```3. /value - this will generate an estimate value of what your account would sell for```\n\n```4. /offer - this command allows you to offer on accounts/profiles```\n\n```5. /buy and /sell - use these commands to create tickets```", 0x0000FF)
        await message.reply(embed=embed)
    if not os.path.exists("./database/database.db"):
        return

    with open("config.json") as config:
        config = json.load(config)
        
    if message.channel.id == 1259269840066318428:
        await message.delete()
        return
    try:
       async with aiosqlite.connect('./database/database.db') as database:
            async with database.execute('''SELECT vouch_channel_id FROM info WHERE guild_id = ?''', (message.guild.id,)) as cursor:
                cursor = await cursor.fetchone()
                try:
                    vouch_channel = cursor[0]
                except TypeError as error:
                    return
            
            
            
            if message.channel.id == vouch_channel:
                try:
                    user = message.mentions[0]
                except IndexError as error:
                    response = await message.channel.send('Please mention the user you are trying to vouch for')
                    await asyncio.sleep(5)
                    await message.delete()
                    await response.delete()
                    return
            
            
                async with database.execute('''SELECT uuid FROM vouch WHERE guild_id = ?''', (message.guild.id,)) as cursor:
                    cursor = await cursor.fetchone()
                    print(cursor[0])
                    if cursor is None:
                        id = str(uuid.uuid4())
                        dm = await message.guild.owner.create_dm()
                        embed = await build('Vouch Key', f"Your server has been set up in the database, whenever a message is sent inside the vouch channel, it will be saved and backed up. **Please save this key: {id}**\nThis key will allow you to paste the vouches into a new server incase of termination, just use the /vouch command.\n**SAVE THIS KEY SOMEWHERE SAFE, OUTSIDE OF DISCORD**", 0xFFFFFF)
                        await dm.send(embed=embed)

                    else:
                        id = cursor[0]
                        
                    
                
                

                await database.execute(
                    '''
                    INSERT INTO vouch (
                        guild_id, seller_id, voucher_name, vouch_profile_picture, vouch_content, uuid  
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    ''',
                    (message.guild.id, user.id, message.author.name, message.author.avatar.url, message.content, id)
                )
                await database.commit()
                # await message.channel.send(f"Stored data: ```{message.guild.id, user.id, message.author.name, message.author.avatar.url, message.content, id}```")
    except Exception as error:
        pass
        
        
    try:    
        if message.author.id == 1227394151847297148:
            if '1250030190617165824' in message.content:
                with open("ai_history.json") as file:
                    history = json.load(file)
                
                
                author_id = str(message.author.id)
                if author_id not in history['ids']:
                    history['ids'][author_id] = {}
                if 'messages' not in history['ids'][author_id]:
                    history['ids'][author_id]['messages'] = []
                if 'responses' not in history['ids'][author_id]:
                    history['ids'][author_id]['responses'] = []
                    
                history['ids'][author_id]['messages'].append(message.content)
                with open("ai_history.json", "w") as file:
                    json.dump(history, file, indent=4)
                    
                prompt = f"A server admin in flux qol has said: {message.content}"
                response = openai_response(prompt, message)
                await message.reply(response)
                return
    except:
        pass
        
    if message.channel.id != 1254978027369136219:
        return

    # if message.author.id != 1227394151847297148:
    #     return
   
   
    if not config['bot']['ai_chat']:
        await message.reply('**Sorry, the chatbot isnt currently available for member use. D: **')
        return

   
   
    with open("ai_history.json") as file:
        history = json.load(file)
        
    author_id = str(message.author.id)
    if author_id not in history['ids']:
        history['ids'][author_id] = {}
    if 'messages' not in history['ids'][author_id]:
        history['ids'][author_id]['messages'] = []
    if 'responses' not in history['ids'][author_id]:
        history['ids'][author_id]['responses'] = []
    
    
    history['ids'][author_id]['messages'].append(message.content)
    with open("ai_history.json", "w") as file:
        json.dump(history, file, indent=4)
    
    prompt = f"act like a friend but you are also an assistant and do what they say but do not repeat their words: {message.content}"
    response = openai_response(prompt, message)
    with open("ai_history.json") as file:
        history = json.load(file)
    history['ids'][author_id]['responses'].append(response)
    with open("ai_history.json", "w") as file:
        json.dump(history, file, indent=4)
   
   
    if 'role' in response or '@' in response or 'discord.gg' in response or 'discord.com/invite' in response or 'https://' in response:
        await message.reply('**Sorry, this response is restricted - ;)**')
        print(response)
        return
    await message.reply(response)
    return

@bot.slash_command(name='offer', description='Offer what you would pay for an account, false offers will result in punishment')
async def offer(ctx,account: discord.Option(str, "Choose what to buy", autocomplete=on_application_command_autocomplete), offer: int, payment_method: discord.Option(str, "Choose a Payment Method", choices=["Cashapp", "Venmo", "Paypal", "LTC", "BTC", "Gift Card", "Other"]), clear: bool=False):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    
    if account == 'No Accounts Listed' or account == 'Database Error, Contact Support':
        await ctx.respond(account, ephemeral=True)
        return
    await handle_offers(ctx, account, offer, payment_method, clear, bot)
    
@bot.slash_command(name="sell", description="Sell an Account / Profile")
async def sell(ctx, payment_method: discord.Option(str, "Choose a Payment Method", choices=["Cashapp", "Venmo", "Paypal", "LTC", "BTC", "Gift Card", "Other"]), account: str=None, price: int=None, coins: int=None):
    await ctx.defer(ephemeral=True)
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    data = await ticket_json(ctx)
    if data is None:
        return
    
    if coins is not None and account is not None:
        await ctx.respond('Please select which to sell, **coins** or an **account**.')
        return

    if account is not None and price is None:
        await ctx.respond('Please include the price you want to sell for when creating a ticket.')
        return

    if price is not None and account is None:
        await ctx.respond('Please include the username of the account you want to sell')
        return

    if coins is not None and coins < 500:
        await ctx.respond('Sorry, the minimum sell amount is 500 Million Coins')
        return

    if coins and coins <= 10000:
        await sell_coins(ctx, coins, bot, data, payment_method)
        return
    
    if coins is not None and coins >= 10000:
        await ctx.respond('Sorry, the most you can sell at one time is 10 Billion')
        return

    
    
    await sell_account(ctx, account, price, bot, data, payment_method)
    
    
@bot.slash_command(name="vouch", description="Backup and Save your servers vouches")
async def vouch(ctx, key: str, webhook: str):
    await ctx.defer(ephemeral=True)
    try:
        async with aiosqlite.connect('./database/database.db') as database:
            async with database.execute('''SELECT uuid FROM vouch WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                cursor = await cursor.fetchone()
                if cursor is None:
                    embed = await build("Server Not Setup", "Please run another command and initialize the server into the database.", 0xFFFFFF)
                    await ctx.respond(embed=embed)
                    return
                id = cursor[0]  
                
            async with database.execute('''SELECT voucher_name, vouch_profile_picture, vouch_content FROM vouch WHERE uuid = ?''', (key,)) as cursor:
                rows = await cursor.fetchall()
                            
            async with database.execute('''SELECT uuid FROM vouch WHERE guild_id = ?''', (ctx.guild.id,)) as cursor:
                prints = await cursor.fetchall()
                print(prints)
        if rows == []:
            embed = await build('Invalid Key', "The key can be found in the dms of the owner", 0xFFFFFF)
            await ctx.respond(embed=embed)
            return
        for row in rows:
            voucher_name, vouch_profile_picture, vouch_content = row
            data = {"content": vouch_content, "username": voucher_name, "avatar_url": vouch_profile_picture}
            response = requests.post(webhook, json=data)
            await asyncio.sleep(0.8)
        await ctx.respond('Restore process finished!')
    

                    
    except Exception as error:
        embed = await build("Exception Triggered", error, 0xFF0000)
        await ctx.respond(embed=embed)
    
    return

@bot.slash_command(name='close', description='Close a Ticket')
async def close(ctx, sold: discord.Option(str, "Choose an Account", autocomplete=on_application_command_autocomplete)=None, amount: int=None): 
    ticket=None
    async with aiosqlite.connect("./database/database.db") as database:
        async with database.execute('SELECT seller_id FROM info WHERE guild_id = ?', (ctx.guild.id,)) as cursor:
            value = await cursor.fetchone()
    role = discord.utils.get(ctx.guild.roles, id=value[0])
    if not role in ctx.author.roles:
        await ctx.respond('You need seller role to run this command', ephemeral=True)
        return
    if sold is not None and amount is not None:
        await ctx.respond('Both the sold and amount category can not be filled')
        return
    
    await close_ticket(ctx, ticket, bot, sold, amount)

@bot.slash_command(name='reset', description='Reset your server in the database')
async def reset(ctx):
    guild = await guild_in_db(ctx)
    if not guild:
        embed = await build('Server not in Database', "Sorry, please wait 3 seconds and start the setup process", 0xFF0000)
        setup = Setup
        await ctx.respond(embed=embed)
        await asyncio.sleep(3)
        await setup.check(ctx)
        return
    if ctx.author.guild_permissions.administrator:  
        async with aiosqlite.connect('./database/database.db') as db:
            async with db.execute("SELECT name FROM sqlite_master WHERE type='table';") as cursor:
                tables = await cursor.fetchall()
            for table in tables:
                table_name = table[0]
                await db.execute(f"DELETE FROM {table_name} WHERE guild_id = ?", (ctx.guild.id,))
            
            await db.commit()
    else:
        return

@bot.slash_command(name='ansi', description='create an ansi advertising message')
async def ansi(ctx, usernames, prices: str):
    await ctx.defer(ephemeral=True)

    await ctx.respond("Generating ANSI advertising message...", ephemeral=True)
    
    await generate_ansi(ctx, usernames, prices)
    

    
async def ticket_json(ctx):
    with open("ticket_management.json") as ticket:
        data = json.load(ticket)
    if str(ctx.guild.id) not in data['ids']:
        data['ids'][str(ctx.guild.id)] = {}
    if str(ctx.author.id) not in data['ids'][str(ctx.guild.id)]:
        data['ids'][str(ctx.guild.id)][str(ctx.author.id)] = 0
    if data['ids'][str(ctx.guild.id)][str(ctx.author.id)] >= 2:
        await ctx.respond('Sorry, you can only have two open tickets at once.')
        return
    return data

