import json

with open("config.json") as conf:
    config = json.load(conf)

async def crimson(dict, priced_dict, username):
    mage = round(dict[username]['crimson']['mage'] / 1000)
    barbarian = round(dict[username]['crimson']['barbarian'] / 1000)
    total = abs(round(mage - barbarian))
    total = (total * 0.83) * config['advanced']['crimson']
    priced_dict[username]['total_crimson'] = total
    return priced_dict
