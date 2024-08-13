import aiosqlite
import asyncio

async def setup_db():
    async with aiosqlite.connect('./database/database.db') as sqlite:
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [info] (
                [guild_id] INTEGER,
                [category_id_account] INTEGER,
                [seller_id] INTEGER,
                [category_id_profile] INTEGER,
                [category_id_sell] INTEGER,
                [coin_price_buy] FLOAT,
                [coin_price_sell] FLOAT,
                [ping_role] INTEGER,
                [category_id_buy] INTEGER,
                [vouch_channel_id] INTEGER
            )
        ''')
        await asyncio.sleep(0.3)
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [account] (
                [guild_id] INTEGER,
                [channel_id] INTEGER,
                [ign] STRING,
                [price] INTEGER,
                [seller_id] INTEGER,
                [offer] INTEGER,
                [channel_name] STRING
            )
        ''')
        await asyncio.sleep(0.3)
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [ticket] (
                [guild_id] INTEGER,
                [channel_id] INTEGER,
                [open_ticket_id] INTEGER,
                [coins] INT,
                [price] INTEGER,
                [seller_id] INTEGER
            )
        ''')
        await asyncio.sleep(0.3)
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [vouch] (
                [guild_id] INTEGER,
                [seller_id] INTEGER,
                [voucher_name] STRING,
                [vouch_profile_picture] STRING,
                [vouch_content] INTEGER,
                [uuid] STRING
            )
        ''')
        await asyncio.sleep(0.3)
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [queue] (
            [guild_id] INTEGER,
            [channel_id] INTEGER,
            [coins] INTEGER
            )
        ''')
        await asyncio.sleep(0.3)
        await sqlite.commit()
        print('Commited')
        
async def vouch_db(ctx):
    return
        
        
        

