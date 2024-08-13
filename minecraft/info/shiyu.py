import asyncio
import aiohttp
from minecraft.info.username import user_data
from bot.build_embed import build



async def shiyu_data(ctx, username):
    async with aiohttp.ClientSession() as shiyu_session:
        user = await user_data(ctx, username)
        
        try:
            async with shiyu_session.get(f'https://sky.shiiyu.moe/stats/{username}/') as abcd:
                await asyncio.sleep(3)
        except:
            pass
        
        try:    
            async with shiyu_session.get(f"https://sky.shiiyu.moe/api/v2/profile/{user['id']}") as response:
                if response.status != 200:
                    embed = await build(f"Caught Exception: {response.status}", f"**From Shiyu API: {response.reason}**", 0xFF0000)
                    await ctx.edit(embed=embed)
                    return
                username = await response.json()
                return username
        except Exception as error:
            print(f'Exception triggered: {error}')      
            return error 