import json
from minecraft.pricing.values.catacombs import catacombs
from minecraft.pricing.values.networth import networth
from minecraft.pricing.values.hotm import hotm

with open("config.json") as conf:
    config = json.load(conf)


async def pricer(dict, username):
    priced_dict = {}
    priced_dict = {username: {
        "total": 0,
        "cata": {
            "level": 0
        },
        "total_hotm": 0,
        "hotm": {
            "level": 0,
            "mithril_powder": 0,
            "gemstone_powder": 0,
            "glacite_powder": 0
        },
        "total_nw": 0,
        "networth": {
            "unsoulbound": 0,
            "soulbound": 0
        },
        "skills": {
            "average": 0,
            "combat": 0,
            "fishing": 0,
            "foraging": 0,
            "mining": 0,
            "farming": 0
        },
        "slayers": {
            "zombie": 0,
            "spider": 0,
            "wolf": 0,
            "enderman": 0,
            "vampire": 0,
            "blaze": 0
        }
    }}

    dict, priced_dict, username = await catacombs(dict, priced_dict, username)
    dict, priced_dict, username = await networth(dict, priced_dict, username)
    dict, priced_dict, username = await hotm(dict, priced_dict, username)

    a = 's'
    return priced_dict, a