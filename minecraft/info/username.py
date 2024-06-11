import aiohttp
import asyncio

async def user_data(username):
    async with aiohttp.ClientSession() as username_info:
        try:
            async with username_info.get(f'https://api.mojang.com/users/profiles/minecraft/{username}') as response:
                if response.status != 200:
                    print(response.status, response.reason)
                    return
                return await response.json()
        except Exception as error:
            print(f"Exception triggered: {error}")
            pass
