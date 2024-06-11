from info.shiyu import shiyu_data

async def user_stats(username, selected_profile):
    statistics = await shiyu_data(username)
    names = [] # Will add the uuid of the profile, with the key value of its name, for example 39c3f571-f948-4cbd-b83c-1ee5052a3f05: Peach
    arrary = [] # will contain profile ids
    for profile_id in statistics['profiles']: # number of profile slots
        names.append(statistics['profiles'][f'{profile_id}']['cute_name']) # gives the profile id the key of cute_name
        arrary.append(profile_id) # adds the profile id to an array 
    newDict = {} # will contain cata, skills, only important info
    location = names.index(selected_profile)
    newDict['cata']['level'] = statistics['profiles'][arrary[location]]["data"]["dungeons"]["catacombs"]["level"]["level"]
    newDict['skills']['skillaverage'] = round(statistics['profiles'][arrary[location]]["data"]["skills"]["averageSkillLevel"])