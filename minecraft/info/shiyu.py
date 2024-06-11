import asyncio
import aiohttp
from username import user_data


async def shiyu_data(username):
    async with aiohttp.ClientSession() as shiyu_session:
        user = await(user_data(username))
        try:    
            async with shiyu_session.get(f"https://sky.shiiyu.moe/api/v2/profile/{user['id']}") as response:
                if response.status != 200:
                    print(response.status, response.reason)
                    return
                return await response.json()
        except Exception as error:
            print(f'Exception triggered: {error}')      
            return error 