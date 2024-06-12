from minecraft.info.shiyu import shiyu_data
statistics = {}


async def user_stats(username):
    statistics[username] = await shiyu_data(username) # calls the function to get data
    statistics[username]['names'] = [statistics[username]['profiles'][f'{profile_id}']['cute_name'] for profile_id in statistics[username]['profiles']] # returns the names of profiles
  # TODO: FIX THIS LINE.  statistics[username]['profile_ids'] = [i for i in statistics[username]['names']]
    return statistics

async def handle_stats(selected_profile, username):
    newDict = {} # will contain cata, skills, only important info
    location = statistics[username]['profile_ids'][selected_profile] # find where in the array is
    newDict['cata']['level'] = statistics['profiles'][location]["data"]["dungeons"]["catacombs"]["level"]["level"] # cata level
    newDict['skills']['skillaverage'] = round(statistics['profiles'][location]["data"]["skills"]["averageSkillLevel"]) # average skill level
    newDict['mining']['hotm_level'] = statistics["profiles"][location]["data"]["mining"]["core"]["level"]["level"]
    newDict['mining']['mithril_powder'] = statistics["profiles"][location]["data"]["mining"]["core"]["powder"]["mithril"]["total"]
    newDict['mining']['gemstone_powder'] = statistics["profiles"][location]["data"]["mining"]["core"]["powder"]["gemstone"]["total"]
    # glacite powder
    s = 'a'
    return newDict, s