from wsgiref import headers
import requests
import json
import pandas as pd

single = True # whether to get only last json or not

if single:
    begin = 0
else:
    begin = 12

responses = []
for pagenum in range(begin,-1,-1):
    url = "https://api.sofascore.com/api/v1/player/750/events/last/"+str(pagenum)
    print(url)

    payload={}
    headers={}
    proxy = {
    'https': 'https://103.73.194.2:80',
    'http': 'https://103.73.194.2:80' 
    }
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    # 'Accept': '*/*',
    # 'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Referer': 'https://www.sofascore.com/',
    # 'Origin': 'https://www.sofascore.com',
    # 'Connection': 'keep-alive',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    # 'TE': 'trailers'
    # }


    r = requests.get(url, headers=headers, data=payload, proxies=proxy)
    print(r)
    cristiano = r.json()
    responses.append(cristiano)

# GET EVENTS
if not single:
    # CONCAT JSONS
    frames=[]
    for i in range(len(responses)-1,-1,-1):
        frames.append(pd.json_normalize(responses[i]['events']))
    frames.reverse()
    df = pd.concat(frames)
    print(df.head())
    df.to_csv('data/events_all.csv', index=False)
else:
    # SINGLE JSON
    df = pd.json_normalize(responses[0]['events'])
    print(df.head())
    df.to_csv('data/events_single.csv', index=False)

# GET RATINGS
if not single:
    # CONCAT JSONS
    frames=[]
    for i in range(len(responses)-1,-1,-1):
        frames.append(pd.DataFrame.from_dict(responses[i]['statisticsMap']).T.reset_index().rename(columns={'index': 'matchid'}))
    frames.reverse()
    df = pd.concat(frames)
    print(df.head())
    df.to_csv('data/ratings_all.csv', index=False)
else:
    # SINGLE JSON
    df = pd.DataFrame.from_dict(responses[0]['statisticsMap']).T.reset_index().rename(columns={'index': 'matchid'})
    print(df.head())
    df.to_csv('data/ratings_single.csv', index=False)