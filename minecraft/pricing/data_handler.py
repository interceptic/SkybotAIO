from info.shiyu import shiyu_data
statistics = {}


async def user_stats(username):
    statistics[username] = await shiyu_data(username)
    names = [] # add the name, for example Peach
    arrary = [] # will contain profile ids
    for profile_id in statistics['profiles']: # number of profile slots
        names.append(statistics['profiles'][f'{profile_id}']['cute_name']) # gives the profile id the key of cute_name
        arrary.append(profile_id) # adds the profile id to an array 
    return names

async def handle_stats(selected_profile):
    newDict = {} # will contain cata, skills, only important info
    location = names.index(selected_profile)
    newDict['cata']['level'] = statistics['profiles'][arrary[location]]["data"]["dungeons"]["catacombs"]["level"]["level"]
    newDict['skills']['skillaverage'] = round(statistics['profiles'][arrary[location]]["data"]["skills"]["averageSkillLevel"])
    