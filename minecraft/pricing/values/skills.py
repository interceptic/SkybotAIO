import json

with open("config.json") as conf:
    config = json.load(conf)

async def skills(dict, priced_dict, username):
    combat = dict[username]["skills"]["combat"]
    fishing = dict[username]["skills"]["fishing"]
    foraging = dict[username]["skills"]["foraging"]
    mining = dict[username]["skills"]["mining"]
    farming = dict[username]["skills"]["farming"]
    average = dict[username]["skills"]["average"]
    
    
    for i in range(1, combat+1):
        if i <= 20:
            priced_dict[username]['skills']['combat'] += 0.04
        if i <= 40 and i > 20:
            priced_dict[username]['skills']['combat'] += 0.08
        if i <= 50 and i > 40:
            priced_dict[username]['skills']['combat'] += 0.20
        if i <= 60 and i > 50:
            priced_dict[username]['skills']['combat'] += 0.25

    for i in range(1, fishing+1):
        if i <= 20:
            priced_dict[username]['skills']['fishing'] += 0.04
        if i <= 40 and i > 20:
            priced_dict[username]['skills']['fishing'] += 0.15
        if i <= 50 and i > 40:
            priced_dict[username]['skills']['fishing'] += 0.20
        if i <= 60 and i > 50:
            priced_dict[username]['skills']['fishing'] += 0.25
    
    for i in range(1, foraging+1):
        if i <= 20:
            priced_dict[username]['skills']['foraging'] += 0.10
        if i <= 40 and i > 20:
            priced_dict[username]['skills']['foraging'] += 0.25
        if i <= 50 and i > 40:
            priced_dict[username]['skills']['foraging'] += 0.40
        if i <= 60 and i > 50:
            priced_dict[username]['skills']['foraging'] += 0.50

    for i in range(1, mining+1):
        if i <= 20:
            priced_dict[username]['skills']['mining'] += 0.04
        if i <= 40 and i > 20:
            priced_dict[username]['skills']['mining'] += 0.07
        if i <= 50 and i > 40:
            priced_dict[username]['skills']['mining'] += 0.11
        if i <= 60 and i > 50:
            priced_dict[username]['skills']['mining'] += 0.17
    
    for i in range(1, farming+1):
        if i <= 20:
            priced_dict[username]['skills']['farming'] += 0.04
        if i <= 40 and i > 20:
            priced_dict[username]['skills']['farming'] += 0.08
        if i <= 50 and i > 40:
            priced_dict[username]['skills']['farming'] += 0.20
        if i <= 60 and i > 50:
            priced_dict[username]['skills']['farming'] += 0.25
    priced_dict[username]['skills']['combat'] *= config['advanced']['combat']
    priced_dict[username]['skills']['fishing'] *= config['advanced']['fishing']
    priced_dict[username]['skills']['foraging'] *= config['advanced']['foraging']
    priced_dict[username]['skills']['mining'] *= config['advanced']['mining']
    priced_dict[username]['skills']['farming'] *= config['advanced']['farming']


    priced_dict[username]['total_skills'] = round(priced_dict[username]['skills']['farming'] + priced_dict[username]['skills']['mining'] + priced_dict[username]['skills']['foraging'] + priced_dict[username]['skills']['fishing'] + priced_dict[username]['skills']['combat'], 2)
    return dict, priced_dict, username



