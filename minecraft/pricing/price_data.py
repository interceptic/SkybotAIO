import json

with open("config.json") as conf:
    config = json.load(conf)


async def pricer(dict, username):
    priced_dict = {}
    