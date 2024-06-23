import aiosqlite

async def setup_db():
    async with aiosqlite.connect('./database/database.db') as sqlite:
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [info] (
                [guild_id] INTEGER,
                [category_id_account] INTEGER,
                [seller_id] INTEGER,
                [category_id_profile] INTEGER,
                [category_id_tickets] INTEGER,
                [coin_price_buy] FLOAT,
                [coin_price_sell] FLOAT
            )
        ''')
        await sqlite.execute('''
            CREATE TABLE IF NOT EXISTS [account] (
                [guild_id] INTEGER,
                [channel_id] INTEGER,
                [ign] STRING,
                [price] INTEGER,
                [seller_id] INTEGER
            )
        ''')
        await sqlite.commit()
        print('Commited')


