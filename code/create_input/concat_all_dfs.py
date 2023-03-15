# Take all dataframes from player folders and join to one
# Same process for all_match_info.csv and match_info.csv(league-only)

import os
import pandas as pd

# assign directory
directory = '/.../data/players'
all_data_frames, league_data_frames =[], []

# iterate over files in that directory
for foldername in sorted(os.listdir(directory)):
    f = os.path.join(directory, foldername)

    all_data_path = directory+'/'+foldername+'/all_match_info.csv'
    league_data_path = directory+'/'+foldername+'/match_info.csv'

    all_data = pd.read_csv(all_data_path)
    league_data = pd.read_csv(league_data_path)

    all_data_frames.append(all_data)
    league_data_frames.append(league_data)


concat_all_data = pd.concat(all_data_frames)
concat_league_data = pd.concat(league_data_frames)

print(concat_all_data.head())
print(concat_all_data.tail())
print(concat_all_data.shape)

print(concat_league_data.head())
print(concat_league_data.tail())
print(concat_league_data.shape)

concat_all_data.to_csv('data/all_players_all_match_info.csv', index=False)
concat_league_data.to_csv('data/all_players_league_match_info.csv', index=False)

    