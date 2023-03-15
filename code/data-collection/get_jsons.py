import json
import pandas as pd
import os
import sys

if len(sys.argv) == 3:
    single = False # whether to get only last json or not
    if single:
        begin = 0
    else:
        begin = int(sys.argv[2])

    responses = []
    directory = '/home/.../data/players/'+str(sys.argv[1])
    
    # iterate over files in that directory
    for pagenum in range(begin,-1,-1):
        filename = str(pagenum)+'.json'
        f = os.path.join(directory, filename)
        file = open(f)
        player_json = json.load(file)
        responses.append(player_json)

    # GET EVENTS
    if not single:
        # CONCAT JSONS
        frames=[]
        for i in range(len(responses)-1,-1,-1):
            frames.append(pd.json_normalize(responses[i]['events']))
        frames.reverse()
        df = pd.concat(frames)
        print(df.tail())
        df.to_csv(directory+'/events_all.csv', index=False)
    else:
        # SINGLE JSON
        df = pd.json_normalize(responses[0]['events'])
        print(df.tail())
        df.to_csv(directory+'/events_single.csv', index=False)

    # GET RATINGS
    if not single:
        # CONCAT JSONS
        frames=[]
        for i in range(len(responses)-1,-1,-1):
            frames.append(pd.DataFrame.from_dict(responses[i]['statisticsMap']).T.reset_index().rename(columns={'index': 'matchid'}))
        frames.reverse()
        df = pd.concat(frames)
        print(df.tail())
        df.to_csv(directory+'/ratings_all.csv', index=False)
    else:
        # SINGLE JSON
        df = pd.DataFrame.from_dict(responses[0]['statisticsMap']).T.reset_index().rename(columns={'index': 'matchid'})
        print(df.tail())
        df.to_csv(directory+'/ratings_single.csv', index=False)
else:
    print('Usage: python get_jsons.py <player dir> <number of latest json>')