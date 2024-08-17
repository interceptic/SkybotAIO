import aiosqlite, random, asyncio

async def calculate(ctx, amount, option):
    if ctx.guild.id == 1227804021142589512:
        if option:
            if amount <= 499:
                amount = False
            amount *= 0.025
            return amount    
        if amount <= 300:
            amount *= 0.08
        if amount <= 599 and amount > 300:
            amount *= 0.06
        if amount >= 600:
            amount *= 0.045
        return amount
    async with aiosqlite.connect('./database/database.db') as database:
        async with database.execute(
            'SELECT coin_price_buy, coin_price_sell FROM info WHERE guild_id = ?', (ctx.guild.id,)
        ) as cursor:
            values = await cursor.fetchone()
            print(values)
    
    coin_price_buy, coin_price_sell = values
    print(coin_price_buy, coin_price_sell)
    if option:
        if amount <= 499:
            amount = False
        amount *= coin_price_buy
        return amount    
    amount *= coin_price_sell
    return amount
            
        
    