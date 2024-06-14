import json

with open("config.json") as conf:
    config = json.load(conf)
async def catacombs(dict, priced_dict, username):
    for level in range(1, dict[username]['cata']['level']+1):
        if level <= 10: 
            priced_dict[username]['cata']['level'] += 0.08
        if level <= 23 & level > 10:
            priced_dict[username]['cata']['level'] += 0.12
        if level == 24:
            priced_dict[username]['cata']['level'] += 1.5 * config['advanced']['cata24']
        if level <= 32 and level > 24:
            priced_dict[username]['cata']['level'] += 0.65
        if level <= 40 and level > 32:
            priced_dict[username]['cata']['level'] += 0.90
        if level <= 45 and level > 40:
            priced_dict[username]['cata']['level'] += 1
        if level <= 49 and level > 45:
            priced_dict[username]['cata']['level'] += 2.50
        if level == 50:
            priced_dict[username]['cata']['level'] += 10
        if level >= 51:
            priced_dict[username]['cata']['level'] += 4
    priced_dict[username]["cata"]["level"] = round((priced_dict[username]["cata"]["level"] * config['pricing']['catacombs']), 2)
    return(dict, priced_dict, username)
