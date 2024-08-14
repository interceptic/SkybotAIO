from minecraft.info.tmbk import representTBMK
from minecraft.info.shiyu import shiyu_data
from minecraft.info.username import user_data
from bot.build_embed import build


ansi = """``````ansi
[2;31mSelling:
"""

async def generate_ansi(ctx, usernames, prices):
    try: 
        message = []
        prices = prices.split()
        usernames = usernames.split()
        
        
        if len(usernames) != len(prices):
            await ctx.respond('You must have the same amount of usernames as prices.', ephemeral=True)
            return
        if len(usernames) > 5:
            await ctx.respond('You can only generate an ansi message for 5 accounts.', ephemeral=True)
            return
        
        for i in range(len(usernames)):
            shiyu_stats = await shiyu_data(ctx, usernames[i])
        
            for s in shiyu_stats['profiles']:
                if shiyu_stats['profiles'][s]['current'] == True:
                    location = s

            try:
                cata = shiyu_stats['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
            except KeyError as error:
                cata = 0
            try:   
                hotm = shiyu_stats["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
            except KeyError as error:
                hotm = 0
            try: 
                sa = round(shiyu_stats['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
            except KeyError as error:
                sa = 0
            try:
                level = shiyu_stats["profiles"][location]["data"]["skyblock_level"]["level"]
            except KeyError as error:
                level = 0
            try:
                unsnw = representTBMK(round(shiyu_stats["profiles"][location]["data"]["networth"]["unsoulboundNetworth"]))
            except KeyError as error:
                unsnw = 0
            try:
                sbnw = representTBMK(round(shiyu_stats["profiles"][location]["data"]["networth"]["networth"]) - round(shiyu_stats["profiles"][location]["data"]["networth"]["unsoulboundNetworth"]))
            except KeyError as error:
                sbnw = 0
                print(error)
            try:
                zombie = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["zombie"]["level"]["currentLevel"]
            except KeyError as error:
                zombie = 0
            try:
                spider = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["spider"]["level"]["currentLevel"]
            except KeyError as error:
                spider = 0
            try:
                wolf = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["wolf"]["level"]["currentLevel"]
            except KeyError as error:
                wolf = 0 
            try:
                enderman = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["enderman"]["level"]["currentLevel"]
            except KeyError as error:
                enderman = 0
            try:
                vamp = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["vampire"]["level"]["currentLevel"]
            except KeyError as error:
                vamp = 0
            try:
                blaze = shiyu_stats["profiles"][location]["data"]["slayer"]["slayers"]["blaze"]["level"]["currentLevel"]
            except KeyError as error:
                blaze = 0
            message.append(f"""
[2;31m[2;35m[2;30m[2;37mIGN:     [0m[2;30m[0m[2;35m[0m[2;31m[2;36m{usernames[i]}: ${prices[i]}[0m[2;31m[0m
[2;30m[2;37mLevel[0m[2;30m[0m:   [2;32m[2;33m{level}[0m[2;32m[0m
[2;30m[2;37mSA[0m[2;30m[0m:      [2;33m{sa}[0m
[2;37m[0m[2;37mUns NW[0m:  [2;33m{unsnw}[0m
[2;30m[2;37mSb NW[0m[2;30m[0m:   [2;33m{sbnw}[0m
[2;30m[2;37mCata[0m[2;30m[0m:    [2;33m{cata}[0m[2;33m
[0m[2;30m[2;37mHOTM[0m[2;30m[0m:    [2;33m{hotm}[0m
[2;37mSlayers[0m:[2;33m ({zombie}/{spider}/{wolf}/{enderman}/{vamp}/{blaze})""")

        final = ansi + """

[0m""".join(message)
        final = final + """
Generated using ANSIgen -> https://github.com/interceptic/ANSIgen``````"""
        await ctx.respond(final, ephemeral=True)
    except Exception as error:
        embed = await build('ANSI Error:', f'```{error}``` Please contact <@1227394151847297148> for support', 0xFF0000)
        await ctx.respond(embed=embed)
        
    