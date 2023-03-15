# Apply some changes to all dfs.
# E.g. column names

import os
from turtle import home
import pandas as pd

# assign directory
directory = '/.../data/players'

def find_age(current_date, player_birth):
    age = round(pd.Timedelta(current_date.date()-player_birth.date()).days/365, 2)
    return age

def find_result(hometeam, homescore, awayscore, current_team):
    result = 0
    if current_team==hometeam:
        if homescore>awayscore:
            result=1 # win
        elif homescore<awayscore:
            result=0 # lose
        else:
            result=2 # draw
    else:
        if homescore<awayscore:
            result=1
        elif homescore>awayscore:
            result=0
        else:
            result=2
    return result

def change_name(player_name):
    if player_name != 'Lewa':
        pass
    else:
        player_name = 'Lewandowski'
    return player_name


# iterate over files in that directory
for foldername in sorted(os.listdir(directory)):
    f = os.path.join(directory, foldername)

    all_data_path = directory+'/'+foldername+'/all_match_info.csv'
    league_data_path = directory+'/'+foldername+'/match_info.csv'

    all_data = pd.read_csv(all_data_path, parse_dates=['startTimestamp', 'player_birth'])
    # all_data.rename(columns={'rating': 'Performance'}, inplace=True)
    # all_data.insert(loc=12, column='age', value=0)
    # all_data['age'] = all_data.apply(lambda row: find_age(row['startTimestamp'], row['player_birth']), axis=1) # get player age at current timestamp
    # all_data['player_name'] = all_data['player_name'].apply(lambda x: x.title()) # Capitalize player names
    # all_data['result'] = all_data.apply(lambda row: find_result(row['homeTeam.name'], row['homeScore.normaltime'], row['awayScore.normaltime'], row['current_team']), axis=1)
    # all_data = all_data[['player_name','player_position','player_nationality','player_birth','player_foot','player_height','age',\
    #     'fifa_rating','fifa_potential','after_injury','injury_days','injury_type','rest_days','form_last1','form_last3','form_last5','form_last10','form_last20','form_last30',\
    #     'season','matchid','startTimestamp','previous_date','tournament.name','tournament.uniqueTournament.slug','tournament.uniqueTournament.id',\
    #     'roundInfo.round','homeTeam.name','homeTeam.id','awayTeam.name','awayTeam.id','current_team','current_team_category','opponent','opponent_category','home_fixture',\
    #     'homeScore.normaltime','awayScore.normaltime','result','Performance']] # rearrange columns
    # all_data['rest_days'] =  all_data['rest_days'].fillna(30) # fill nan rest days for first games of Aug 2015
    # all_data['form_last5'] = all_data['Performance'].rolling(6).mean() # get mean form for last N games
    # all_data['form_last10'] = all_data['Performance'].rolling(11).mean()
    # all_data['form_last20'] = all_data['Performance'].rolling(21).mean()
    # all_data['form_last30'] = all_data['Performance'].rolling(31).mean()
    # all_data['form_last3'] = all_data['Performance'].rolling(4).mean()
    # all_data['form_last1'] = all_data['Performance'].rolling(2).mean()
    # all_data['player_name'] = all_data.apply(lambda row: change_name( row['player_name']), axis=1) # get player name


    league_data = pd.read_csv(league_data_path, parse_dates=['startTimestamp', 'player_birth'])
    # league_data.rename(columns={'rating': 'Performance'}, inplace=True)
    # league_data.insert(loc=12, column='age', value=0)
    # league_data['age'] = league_data.apply(lambda row: find_age(row['startTimestamp'], row['player_birth']), axis=1)
    # league_data['player_name'] = league_data['player_name'].apply(lambda x: x.title())
    # league_data['result'] = league_data.apply(lambda row: find_result(row['homeTeam.name'], row['homeScore.normaltime'], row['awayScore.normaltime'], row['current_team']), axis=1)
    # league_data = league_data[['player_name','player_position','player_nationality','player_birth','player_foot','player_height','age',\
    #     'fifa_rating','fifa_potential','after_injury','injury_days','injury_type','rest_days','form_last1','form_last3','form_last5','form_last10','form_last20','form_last30',\
    #     'season','matchid','startTimestamp','previous_date','tournament.name','tournament.uniqueTournament.slug','tournament.uniqueTournament.id',\
    #     'roundInfo.round','homeTeam.name','homeTeam.id','awayTeam.name','awayTeam.id','current_team','current_team_category','opponent','opponent_category','home_fixture',\
    #     'homeScore.normaltime','awayScore.normaltime','result','Performance']]
    # league_data['rest_days'] =  league_data['rest_days'].fillna(30)
    # league_data['form_last5'] = league_data['Performance'].rolling(6).mean()
    # league_data['form_last10'] = league_data['Performance'].rolling(11).mean()
    # league_data['form_last20'] = league_data['Performance'].rolling(21).mean()
    # league_data['form_last30'] = league_data['Performance'].rolling(31).mean()
    # league_data['form_last3'] = league_data['Performance'].rolling(4).mean()
    # league_data['form_last1'] = league_data['Performance'].rolling(2).mean()
    # league_data['player_name'] = league_data.apply(lambda row: change_name( row['player_name']), axis=1) # get player name



    all_data.to_csv(all_data_path, index=False)
    league_data.to_csv(league_data_path, index=False)
