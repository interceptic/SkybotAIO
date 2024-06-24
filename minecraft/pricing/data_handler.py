from minecraft.info.shiyu import shiyu_data
statistics = {}


async def user_stats(ctx, username):
    statistics[username] = await shiyu_data(ctx, username) # calls the function to get data
    statistics[username]['names'] = [statistics[username]['profiles'][f'{profile_id}']['cute_name'] for profile_id in statistics[username]['profiles']] # returns the names of profiles
    statistics[username]['profile_ids'] = {name: profile_id for name, profile_id in zip(statistics[username]['names'], statistics[username]['profiles'])}
    return statistics

async def handle_stats(selected_profile, username):
    newDict = {} # will contain cata, skills, only important info
    location = statistics[username]['profile_ids'][selected_profile] # find where in the array is
    

    newDict = {username: {
        "level": 0,
        "cata": {
            "level": 0
        },
        "hotm": {
            "level": 0,
            "mithril_powder": 0,
            "gemstone_powder": 0,
            "glacite_powder": 0
        },
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
        },
        "crimson": {
            "mage": 0,
            "barbarian": 0
        },
        "weight": {
            "senither": 0,
            "lily": 0
        },
        "minions": {
            "total": 0,
            "bonus": 0
        }
    }
}


    try:
        newDict[username]['cata']['level'] = statistics[username]['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
    except KeyError as error:
        newDict[username]['cata']['level'] = 0
    try: 
        newDict[username]['skills']['average'] = round(statistics[username]['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:   
        newDict[username]['hotm']['level'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['hotm']['mithril_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["mithril"]["total"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['hotm']['gemstone_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["gemstone"]["total"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['hotm']['glacite_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["glacite"]["total"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['networth']['unsoulbound'] = round(statistics[username]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"])
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['networth']['soulbound'] = round(statistics[username]["profiles"][location]["data"]["networth"]["networth"]) - round(statistics[username]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"])
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['skills']['combat'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['combat']['level']
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['skills']['fishing'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['fishing']['level']
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['skills']['foraging'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['foraging']['level']
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['skills']['mining'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['mining']['level']
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['skills']['farming'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['farming']['level']
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['zombie'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["zombie"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['spider'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["spider"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['wolf'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["wolf"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['enderman'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["enderman"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['vampire'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["vampire"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['slayers']['blaze'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["blaze"]["level"]["currentLevel"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['crimson']['mage'] = statistics[username]["profiles"][location]["data"]["crimson_isle"]["factions"]["mages_reputation"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['crimson']['barbarian'] = statistics[username]["profiles"][location]["data"]["crimson_isle"]["factions"]["barbarians_reputation"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['level'] = statistics[username]["profiles"][location]["data"]["skyblock_level"]["level"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try:
        newDict[username]['minions']['total'] = statistics[username]["profiles"][location]["data"]["minions"]["minion_slots"]["current"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    try: 
        newDict[username]['minions']['bonus'] = statistics[username]["profiles"][location]["data"]["misc"]["profile_upgrades"]["minion_slots"]
    except KeyError as error:
        print(f"KeyError: {error}, likely irrelevant.")
    if 'MVP' in statistics[username]['profiles'][location]['data']['rank_prefix'] and 'rank-plus' in statistics[username]['profiles'][location]['data']['rank_prefix']:
        rank = 'MVP+'
    elif 'MVP' in statistics[username]['profiles'][location]['data']['rank_prefix'] and 'rank-plus' not in statistics[username]['profiles'][location]['data']['rank_prefix']:
        rank = 'MVP'
    elif 'VIP+' in statistics[username]['profiles'][location]['data']['rank_prefix'] and 'rank-plus' in statistics[username]['profiles'][location]['data']['rank_prefix']:
        rank = 'VIP+'
    elif 'VIP' in statistics[username]['profiles'][location]['data']['rank_prefix'] and 'rank-plus' not in statistics[username]['profiles'][location]['data']['rank_prefix']:
        rank = 'VIP'
    else:
        rank = 'NON'
    return newDict, rank


