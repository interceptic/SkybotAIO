import json

with open("config.json") as conf:
    config = json.load(conf)

async def networth(dict, priced_dict, username):
    unsoulbound = dict[username]['networth']['unsoulbound']
    soulbound = dict[username]['networth']['soulbound']
    unsoulbound = round(unsoulbound / 1000000)
    priced_dict[username]['networth']['unsoulbound'] = round(unsoulbound * config['pricing']['networth_unsb'],2)
    soulbound = round(soulbound/1000000)
    priced_dict[username]['networth']['soulbound'] = round(soulbound * config['pricing']['networth_sb'],2)
    priced_dict[username]['total_nw'] = priced_dict[username]['networth']['unsoulbound'] + priced_dict[username]['total_nw']
    return dict, priced_dict, username