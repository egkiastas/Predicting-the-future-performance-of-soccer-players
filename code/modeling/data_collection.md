# Data Collection-Exploration Process
Enable python environment: `conda activate thesis`

## Scraping Instructions
Two options are provided for getting relevant player data.
1. In the sofascore website: e.g.https://www.sofascore.com/player/cristiano-ronaldo/750

    right click "inspect". Check network, file 0, and XHR Response to see jsons

    Run *get_events.py*. Change url and 'single' flag for each player

2. *get_jsons.py*:

    Download 15 jsons for every player(e.g. https://api.sofascore.com/api/v1/player/78893/events/last/0).   
    Then run the script for all players. Two dfs are created.
    *data/players/**_player/events_all.csv* (all matches, maybe before 2015)
    *data/players/**_player/ratings_all.csv* (all ratings from 2015 approximately)

## Further Data Collection

1. Run *create_input/[number].ipynb* for every player. One df is created for everyone.

2. Manually add season, fifa_rating, fifa_potential to match_info.csv
(https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

3. Manually add injury information to all_match_info.csv
(https://www.transfermarkt.com/lionel-messi/verletzungen/spieler/28003)

4. Add position, birth, height, foot, nationality, market value to all_match_info.csv

6. Run *create_input/create_league_match_info_4all.py* : 
    Automation of last cells of *create_input/number.ipynb*. Take *all_match_info.csv*, add player name to column and hold only league matches.

    *data/players/**_player/all_match_info.csv* (all)

    *data/players/**_player/match_info.csv* (league-only)

7. Run *create_input/change_sth_to_all_dfs.py*:

    - Change 'rating' column name to 'Performance'.
    - Get player age at current timestamp.
    - Capitalize player names.
    - Find result.
    - Rearrange columns.

8. Run *create_input/concat_all_dfs.py*:
    - Take all dataframes from player folders and join to one.
    - Same process for all_match_info.csv(all) and match_info.csv(league-only)
    - New shapes: (8443, 34), (5631, 34)

## Modeling

9. Run *create_input/eda_each_player.py*:
    - Basic plot, analysis and profiling reports for each player.

10. Run *modeling/5_multivariate_models_all-players.ipynb* and *modeling/5_arima_all-players.ipynb*
    - Data proprocessing, feature engineering, model design, training and inference.
