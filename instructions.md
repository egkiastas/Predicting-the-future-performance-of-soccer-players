# Data Collection-Exploration-Modeling Process
Here, the step-by-step reproduction instructions are provided.

**Note** that [Scraping](#scraping) and [Further Data Collection](#further-data-collection) parts can be skipped and begin from the [Modeling](#modeling), since the dataset 
is available.

## Usage
To use this code, you need to have Python 3 installed on your system. You can install the required packages by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

Enable python environment: 

```bash
conda activate thesis
```

## Scraping
Two options are provided for getting relevant player data.
1. On the sofascore website: e.g.https://www.sofascore.com/player/cristiano-ronaldo/750

    Right-click "inspect". Check network, file 0, and XHR Response to see jsons

    Run *data_collection/get_events.py*. Change url and 'single' flag for each player

2. *data_collection/get_jsons.py*:

    Download 15 jsons for every player(e.g. https://api.sofascore.com/api/v1/player/78893/events/last/0).   
    Then run the script for all players. Two dfs are created.
    - *data/players/**_player/events_all.csv* (all matches, maybe before 2015)
    - *data/players/**_player/ratings_all.csv* (all ratings from 2015 approximately)

## Further Data Collection

1. Run *create_input/[number].ipynb* for every player. One dataframe is created for everyone. Only one notebook is provided, here.

2. Manually add season, fifa_rating, fifa_potential to match_info.csv
(https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)

3. Manually add injury information to all_match_info.csv
(https://www.transfermarkt.com/lionel-messi/verletzungen/spieler/28003)

4. Add position, birth, height, foot, nationality, market value to all_match_info.csv

6. Run *create_input/create_league_match_info_4all.py* : 
    - Automation of last cells of *create_input/number.ipynb*. 
    - Take *all_match_info.csv*, add player name to column and hold only league matches.

    - *data/players/**_player/all_match_info.csv* (all)

    - *data/players/**_player/match_info.csv* (league-only)

7. Run *create_input/change_sth_to_all_dfs.py*:

    - Change 'rating' column name to 'Performance'.
    - Get player age at current timestamp.
    - Capitalize player names.
    - Find result.
    - Rearrange columns.

8. Run *create_input/concat_all_dfs.py*:
    - Take all dataframes from player folders and join to one.
    - Perform the same process for all_match_info.csv(all) and match_info.csv(league-only)
    - New shapes: (8443, 34), (5631, 34)

9. *create_input/eda_each_player.py*:
    - Automated the basic plots, analysis and profiling reports for each player.

## Modeling
At this stage, all data have been collected and joined. We can now explore and develop models. Each notebook is named with a number indicating its order.

10. *modeling/1_eda_all_players.ipynb* and *modeling/2_eda_injuries.ipynb*
    - Basic plot, analysis and profiling reports for each player and their injuries.

11. *modeling/3_feature_selection.ipynb*
    - Feature exploration and importance

10. *modeling/4_regression.ipynb*
    - Handle the problem as a time-agnostic regression one.

10. *modeling/5_multivariate_models_all-players.ipynb* and *modeling/5_arima_all-players.ipynb*
    - Data proprocessing, feature engineering, model design, training and inference.
    - Multivariate and univariate time-series forecasting of future player performance.
