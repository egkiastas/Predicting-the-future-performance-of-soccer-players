import os
import pandas as pd
from pandas_profiling import ProfileReport
import plotly.graph_objects as go
import plotly.express as px

# assign directory
directory = '/.../data/players'

def eda(data, plot_path):
    # Raw data
    fig1 = go.Figure()
    fig1.add_scatter(x=data.index, y=data.Performance, name='Performance')

    rolling_mean5 = pd.Series.rolling(data['Performance'], window=10).mean();
    fig1.add_scatter(x=data.index, y=rolling_mean5, mode='lines', name='Window=10');

    fig1.update_layout(
        title={
            'text': "Raw Perfomance values and Rolling Mean",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    with open(plot_path, 'a') as f:
        f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'));
 
# iterate over files in that directory
for foldername in sorted(os.listdir(directory)):
    f = os.path.join(directory, foldername)
    csv_path = directory+'/'+foldername+'/match_info.csv'
    plot_path = directory+'/'+foldername+'/plots.html'
    profiling_path = directory+'/'+foldername+'/profiling.html'

    # if os.path.exists(plot_path):
    #     os.remove(plot_path)
    # else:
    #     print("The file does not exist to be removed")
    if os.path.exists(profiling_path):
        os.remove(profiling_path)
    else:
        print("The file does not exist to be removed")

    print(csv_path, plot_path)

    # Generate pandas profiling reports
    league_data = pd.read_csv(csv_path, index_col=['startTimestamp'], parse_dates=['startTimestamp'])
    league_data = league_data[['after_injury','Performance']]
    print(league_data.columns)
    
    profile = ProfileReport(league_data)
    profile
    profile.to_file(profiling_path)
    # eda(league_data, plot_path)

    