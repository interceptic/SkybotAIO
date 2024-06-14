import json

with open("config.json") as conf:
    config = json.load(conf)

async def hotm(dict, priced_dict, username):
    for tier in range(1, dict[username]['hotm']['level']+1):
        if tier == 1:
            priced_dict[username]['hotm']['level'] += 0.33
        if tier == 2:
            priced_dict[username]['hotm']['level'] += 0.66
        if tier == 3:
            priced_dict[username]['hotm']['level'] += 1
        if tier == 4:
            priced_dict[username]['hotm']['level'] += 1.5
        if tier == 5:
            priced_dict[username]['hotm']['level'] += 2
        if tier == 6:
            priced_dict[username]['hotm']['level'] += 3
        if tier == 7:
            priced_dict[username]['hotm']['level'] += 7 * config['advanced']['hotm7']
        if tier == 8:
            priced_dict[username]['hotm']['level'] += 5
        if tier == 9:
            priced_dict[username]['hotm']['level'] += 5
        if tier == 10:
            priced_dict[username]['hotm']['level'] += 5 * config['advanced']['hotm10']
    priced_dict[username]['hotm']['level'] = round(priced_dict[username]['hotm']['level'])  
    priced_dict[username]['hotm']['mithril_powder'] = round(dict[username]['hotm']['mithril_powder'] / 100000) * config['pricing']['mithril_powder']
    priced_dict[username]['hotm']['gemstone_powder'] = round(dict[username]['hotm']['gemstone_powder'] / 100000) * config['pricing']['gemstone_powder']
    priced_dict[username]['hotm']['glacite_powder'] = round(dict[username]['hotm']['glacite_powder'] / 100000) * config['pricing']['glacite_powder']
    priced_dict[username]['total_hotm'] =  priced_dict[username]['hotm']['level'] + priced_dict[username]['hotm']['mithril_powder'] + priced_dict[username]['hotm']['gemstone_powder'] + priced_dict[username]['hotm']['glacite_powder']
    
    
    
    return dict, priced_dict, username