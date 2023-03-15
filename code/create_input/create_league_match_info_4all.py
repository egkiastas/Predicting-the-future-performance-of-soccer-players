# Automation of last cells of create_input/number.ipynb. 
# Take all_match_info.csv, add player name to column and hold only league matches

import os
import pandas as pd

# assign directory
directory = '/.../data/players'
 
league_names = ['premier-league', 'laliga','ligue-1','serie-a','bundesliga','eliteserien','eredivisie','liga-profesional-de-futbol','brasileiro-serie-a','primeira-liga','super-league', 'Süper Lig', 'LaLiga 2']

# iterate over files in that directory
for foldername in sorted(os.listdir(directory)):
    f = os.path.join(directory, foldername)
    csv_path = directory+'/'+foldername+'/all_match_info.csv'


    # Read csv and hold only rows of league games
    all_data = pd.read_csv(csv_path)

    # RUN ONLY ONE TIME
    # player = foldername.split("_")[1] # get player name from folder.
    # all_data.insert(loc=0, column='player_name', value=player)
    # all_data.insert(loc=1, column='player_position', value='')
    # all_data.insert(loc=2, column='player_nationality', value='')
    # all_data.insert(loc=3, column='player_birth', value='')
    # all_data.insert(loc=4, column='player_foot', value='')
    # all_data.insert(loc=5, column='player_height', value='')

    print(all_data.head())

    # all_data.to_csv(csv_path, index=False)

    league_data = all_data[all_data['tournament.uniqueTournament.slug'].isin(league_names)]
    league_data.to_csv(directory+'/'+foldername+'/match_info.csv', index=False)
    