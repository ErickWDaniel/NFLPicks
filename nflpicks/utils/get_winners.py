import pandas as pd
from nflpicks.utils import winners
from nflpicks.utils.logs import logging



def get_points():

    try:
        # 'mysite/nflpicks/data/data.sqlite'
        win = winners.Winners('nflpicks/data/data.sqlite')
        s = win.data_cleaner.wins()
        points = s.points.sort_values('points', ascending=False)

    except Exception as k:
        logging.error(f'We ignored', exc_info=True)
        points = pd.DataFrame(
            {'picker_id':['Johnny','Anne','Rachel'],
            'points': [128, 102, 42]})
    return points.to_dict(orient='records')


def get_points_per_round():

    try:
        win = winners.Winners('nflpicks/data/data.sqlite')
        s = win.data_cleaner.wins()
        points_per_round = s.points_per_round.sort_values('points', ascending=False)
        
    except Exception as k:
        logging.error(f'We ignored', exc_info=True)
        points_per_round = pd.DataFrame(
            {'picker_id':['Johnny','Anne','Rachel'],
            'points': [128, 102, 42],
            'round': [1,1,1]})

    return points_per_round.to_dict(orient='records')


