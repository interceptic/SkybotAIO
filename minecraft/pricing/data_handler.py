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
    print(statistics[username]['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"])
    print(location)
    
    # TODO: 

    newDict = {username: {
        "cata": {
            "level": 0
        }
    }}


    try:
        newDict[username]['cata']['level'] = statistics[username]['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
    except KeyError:
        newDict[username]['cata']['level'] = "API disabled or no cata levels"
    # newDict[username]['skills']['skillaverage'] = round(statistics[username]['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
    # newDict[username]['mining']['hotm_level'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
    # newDict[username]['mining']['mithril_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["mithril"]["total"]
    # newDict[username]['mining']['gemstone_powder'] = statistics[username]["profiles"][location]["data"]["mining"]["core"]["powder"]["gemstone"]["total"]
    # # glacite powder
    s = 'a'
    return newDict, s


