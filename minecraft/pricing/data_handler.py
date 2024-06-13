from minecraft.info.shiyu import shiyu_data
statistics = {}


async def user_stats(username):
    statistics[username] = await shiyu_data(username) # calls the function to get data
    statistics[username]['names'] = [statistics[username]['profiles'][f'{profile_id}']['cute_name'] for profile_id in statistics[username]['profiles']] # returns the names of profiles
    statistics[username]['profile_ids'] = {name: profile_id for name, profile_id in zip(statistics[username]['names'], statistics[username]['profiles'])}
    return statistics

async def handle_stats(selected_profile, username):
    newDict = {} # will contain cata, skills, only important info
    location = statistics[username]['profile_ids'][selected_profile] # find where in the array is
    
    # TODO: 

    newDict = {username: {
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
        }
    }
}


    try:
        newDict[username]['cata']['level'] = statistics[username]['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
    except Exception as error:
        newDict[username]['cata']['level'] = 0
    try: 
        newDict[username]['skills']['average'] = round(statistics[username]['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
    except Exception as error:
        print(error)
    try:   
        newDict[username]['hotm']['level'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['hotm']['mithril_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["mithril"]["total"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['hotm']['gemstone_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["gemstone"]["total"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['hotm']['glacite_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["glacite"]["total"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['networth']['unsoulbound'] = round(statistics[username]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"])
    except Exception as error:
        print(error)
    try:
        newDict[username]['networth']['soulbound'] = round(statistics[username]["profiles"][location]["data"]["networth"]["networth"]) - round(statistics[username]["profiles"][location]["data"]["networth"]["unsoulboundNetworth"])
    except Exception as error:
        print(error)
    try:
        newDict[username]['skills']['combat'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['combat']['level']
    except Exception as error:
        print(error)
    try:
        newDict[username]['skills']['fishing'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['fishing']['level']
    except Exception as error:
        print(error)
    try:
        newDict[username]['skills']['foraging'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['foraging']['level']
    except Exception as error:
        print(error)
    try:
        newDict[username]['skills']['mining'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['mining']['level']
    except Exception as error:
        print(error)
    try:
        newDict[username]['skills']['farming'] = statistics[username]["profiles"][location]["data"]['skills']['skills']['farming']['level']
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['zombie'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["zombie"]["level"]["currentLevel"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['spider'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["spider"]["level"]["currentLevel"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['wolf'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["wolf"]["level"]["currentLevel"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['enderman'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["enderman"]["level"]["currentLevel"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['vampire'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["vampire"]["level"]["currentLevel"]
    except Exception as error:
        print(error)
    try:
        newDict[username]['slayers']['blaze'] = statistics[username]["profiles"][location]["data"]["slayer"]["slayers"]["blaze"]["level"]["currentLevel"]
    except Exception as error:
        print(error)

    s = 'a'
    return newDict, s


