import json

import pandas as pd
import plotly
import plotly.graph_objs as go

def get_results(data):
    df = pd.DataFrame.from_records(data)
    df = df[df['points'] > 0]
    df = df.sort_values(by='round')

    data_ = [
        go.Scatter(
            x=df[df['picker_id'] == user_id]['round'],
            y=df[df['picker_id'] == user_id]['points'],
            name=user_id,
        ) for user_id in df['picker_id'].unique()
    ]

    bar = json.dumps(data_, cls=plotly.utils.PlotlyJSONEncoder)

    points = df.groupby(
        'picker_id')['points'].sum(
    ).reset_index(
    ).sort_values('points',ascending=False
                  ).to_dict(orient='records')

    return bar, points
