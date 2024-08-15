import json, aiosqlite, discord, datetime, asyncio, os
from discord.ext import commands
from minecraft.info.tmbk import representTBMK

async def update_embed(bot):
    print('Statistics is a bit complicated, only attempt to use statistics if you know what you are doing / a developer')
    # while True:
    #     if not os.path.exists("./database/database.db"):
    #         return
    
    #     with open("config.json") as config:
    #         config = json.load(config)
            
    #     channel = await bot.fetch_channel(int(config['bot']['statistics']))
    #     message = await channel.fetch_message('1258832829824110703')
    #     async with aiosqlite.connect("./database/database.db") as database:
    #         async with database.execute('''SELECT coins FROM ticket WHERE guild_id = ?''', (1227804021142589512,)) as cursor:
    #             coins = await cursor.fetchall()
                
    #         async with database.execute('''SELECT coins FROM queue WHERE guild_id = ?''', (1227804021142589512,)) as cursor:
    #             queue = await cursor.fetchall()
            
    #         async with database.execute('SELECT COUNT(*) FROM vouch WHERE guild_id = ?', (1227804021142589512,)) as cursor:
    #             row_count_result = await cursor.fetchone()

    #         async with database.execute('SELECT * FROM ticket WHERE guild_id = ? AND channel_id IS NOT NULL', (1227804021142589512,))as cursor:
    #             open_tickets = await cursor.fetchall()

    #         async with database.execute('SELECT * FROM account WHERE guild_id = ?', (1227804021142589512,))as cursor:
    #             accounts_profiles = await cursor.fetchall()
                
    #     try:
    #         async with aiosqlite.connect('./database/database.db') as sqlite:
    #             async with sqlite.execute('SELECT channel_id FROM account WHERE guild_id = ?', (1227804021142589512,)) as cursor:
    #                 rows = await cursor.fetchall()
    #                 channel_ids = [str(row[0]) for row in rows]
    #                 number = 0
    #         for channel_id in channel_ids:
    #             try:
    #                 channel = await bot.fetch_channel(int(channel_id))
    #                 number += 1
    #             except Exception as error:
    #                 pass
    #     except Exception as error:
    #         pass
        
            
            
    #     # Extract the count from the result
    #     row_count = row_count_result[0] if row_count_result else 0
    #     total = 0
    #     queues = 0

    #     if coins == [] or coins is None:
    #         print('Empty List Coins = []')
    #     else: 
    #         for coin in coins:
    #             if coin[0] is not None:
    #                 total += coin[0]
    #     if queue == [] or queue is None:
    #         print('Empty List Queue = []')
    #     else:
    #         for que in queue:
    #             if que[0] is not None:
    #                 queues += que[0]
    #     tmbk = representTBMK(total*1000000)
    #     tbmk2 = representTBMK(queues*1000000)
    #     embed = discord.Embed(title='Flux QOL Statistics', description='Tracking Since <t:1720198800>', color=0x1D0FC7)
    #     embed.add_field(name=f'Total Coins Handled: {tmbk}', value=f'', inline=False)
    #     embed.add_field(name=f'Total Vouches: {row_count}', value=f'', inline=False)
    #     embed.add_field(name=f'Lifetime Created Tickets: - {len(open_tickets)}', value='', inline=False)
    #     embed.add_field(name=f'Sell Coin Queue: 0', value='', inline=False)
    #     embed.add_field(name=f'Accounts / Profiles Listed: {number}', value='', inline=False)
    #     embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
    #     embed.timestamp = datetime.datetime.now()
    #     embed.thumbnail = "https://media.discordapp.net/attachments/1227398031112933478/1233568070782554253/fluxbanner.png?ex=6689318a&is=6687e00a&hm=86a40117bdd2b47664ef71679ba0435efd3704fec6f649aa95fff68a1687636d&=&quality=lossless"
    #     await message.edit(content=None, embed=embed)
    #     print('total')
    #     await asyncio.sleep(60*30)
    