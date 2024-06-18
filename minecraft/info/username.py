import aiohttp
import asyncio
from bot.build_embed import build


async def user_data(ctx, username):
    async with aiohttp.ClientSession() as username_info:
        try:
            async with username_info.get(f'https://api.mojang.com/users/profiles/minecraft/{username}') as response:
                if response.status != 200:
                    print(response.status, response.reason)
                    embed = await build(f"Caught Exception: {response.status}", f"**From Mojang API: {response.reason}**", 0xFF0000)
                    await ctx.edit(embed=embed)
                    return
                return await response.json()
        except Exception as error:
            print(f"Exception triggered: {error}")
            return
