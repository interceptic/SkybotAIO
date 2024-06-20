import os
import aiosqlite
from discord.ext import commands

# IDK HOW TO DO SQLITE 

async def setup():
    async with aiosqlite.connect('./database/database.db') as sqlite:
        await database.execute('''
            CREATE TABLE IF NOT EXISTS [info] (
                [guild_id] INTEGER,
                [ign] TEXT,
                [channel_id] INTEGER,
                [message_id] INTEGER,
                [price] FLOAT,
                [payment_methods] TEXT,
                [seller_discord_id] INTEGER,
                [buyer_discord_id] INTEGER
            )
        ''')