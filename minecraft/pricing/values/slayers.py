import json

with open("config.json") as conf:
    config = json.load(conf)

async def slayers(dict, priced_dict, username):
    for tier in range(1, dict[username]['slayers']['zombie']+1):
        if tier == 1:
            priced_dict[username]['slayers']['zombie'] += 0.03
        if tier == 2:
            priced_dict[username]['slayers']['zombie'] += 0.03
        if tier == 3:
            priced_dict[username]['slayers']['zombie'] += 0.10
        if tier == 4:
            priced_dict[username]['slayers']['zombie'] += 0.45
        if tier == 5:
            priced_dict[username]['slayers']['zombie'] += 0.75
        if tier == 6:
            priced_dict[username]['slayers']['zombie'] += 1
        if tier == 7:
            priced_dict[username]['slayers']['zombie'] += 1.5 * config['advanced']['slayer_zombie']
        if tier == 8:
            priced_dict[username]['slayers']['zombie'] += 2
        if tier == 9:
            priced_dict[username]['slayers']['zombie'] += 3
        

    for tier in range(1, dict[username]['slayers']['spider']+1):
        if tier == 1:
            priced_dict[username]['slayers']['spider'] += 0.03
        if tier == 2:
            priced_dict[username]['slayers']['spider'] += 0.03
        if tier == 3:
            priced_dict[username]['slayers']['spider'] += 0.10
        if tier == 4:
            priced_dict[username]['slayers']['spider'] += 0.45
        if tier == 5:
            priced_dict[username]['slayers']['spider'] += 0.75
        if tier == 6:
            priced_dict[username]['slayers']['spider'] += 1
        if tier == 7:
            priced_dict[username]['slayers']['spider'] += 1.5 * config['advanced']['slayer_spider']
        if tier == 8:
            priced_dict[username]['slayers']['spider'] += 2
        if tier == 9:
            priced_dict[username]['slayers']['spider'] += 3


    for tier in range(1, dict[username]['slayers']['wolf']+1):
        if tier == 1:
            priced_dict[username]['slayers']['wolf'] += 0.03
        if tier == 2:
            priced_dict[username]['slayers']['wolf'] += 0.13
        if tier == 3:
            priced_dict[username]['slayers']['wolf'] += 0.20
        if tier == 4:
            priced_dict[username]['slayers']['wolf'] += 0.50
        if tier == 5:
            priced_dict[username]['slayers']['wolf'] += 0.75
        if tier == 6:
            priced_dict[username]['slayers']['wolf'] += 1.5
        if tier == 7:
            priced_dict[username]['slayers']['wolf'] += 2 * config['advanced']['slayer_wolf']
        if tier == 8:
            priced_dict[username]['slayers']['wolf'] += 3
        if tier == 9:
            priced_dict[username]['slayers']['wolf'] += 4
   
    for tier in range(1, dict[username]['slayers']['enderman']+1):
        if tier == 1:
            priced_dict[username]['slayers']['enderman'] += 0.33
        if tier == 2:
            priced_dict[username]['slayers']['enderman'] += 0.66
        if tier == 3:
            priced_dict[username]['slayers']['enderman'] += 1
        if tier == 4:
            priced_dict[username]['slayers']['enderman'] += 1.5
        if tier == 5:
            priced_dict[username]['slayers']['enderman'] += 2
        if tier == 6:
            priced_dict[username]['slayers']['enderman'] += 3
        if tier == 7:
            priced_dict[username]['slayers']['enderman'] += 4 * config['advanced']['slayer_enderman']
        if tier == 8:
            priced_dict[username]['slayers']['enderman'] += 4
        if tier == 9:
            priced_dict[username]['slayers']['enderman'] += 5
   
    for tier in range(1, dict[username]['slayers']['vampire']+1):
        if tier == 1:
            priced_dict[username]['slayers']['vampire'] += 0.33
        if tier == 2:
            priced_dict[username]['slayers']['vampire'] += 0.66
        if tier == 3:
            priced_dict[username]['slayers']['vampire'] += 1
        if tier == 4:
            priced_dict[username]['slayers']['vampire'] += 1.5
        if tier == 5:
            priced_dict[username]['slayers']['vampire'] += 2
    

    for tier in range(1, dict[username]['slayers']['blaze']+1):
        if tier == 1:
            priced_dict[username]['slayers']['blaze'] += 0.33
        if tier == 2:
            priced_dict[username]['slayers']['blaze'] += 0.66
        if tier == 3:
            priced_dict[username]['slayers']['blaze'] += 1
        if tier == 4:
            priced_dict[username]['slayers']['blaze'] += 1.5
        if tier == 5:
            priced_dict[username]['slayers']['blaze'] += 2
        if tier == 6:
            priced_dict[username]['slayers']['blaze'] += 3
        if tier == 7:
            priced_dict[username]['slayers']['blaze'] += 4 * config['advanced']['slayer_blaze']
        if tier == 8:
            priced_dict[username]['slayers']['blaze'] += 5
        if tier == 9:
            priced_dict[username]['slayers']['blaze'] += 6
   
   
   
   
    priced_dict[username]['total_slayers'] = round((priced_dict[username]['slayers']['zombie'] + priced_dict[username]['slayers']['vampire'] + priced_dict[username]['slayers']['enderman'] + priced_dict[username]['slayers']['wolf'] + priced_dict[username]['slayers']['spider'] + priced_dict[username]['slayers']['blaze']) * config['pricing']['slayers'], 2)  

    
    
    
    return dict, priced_dict, username