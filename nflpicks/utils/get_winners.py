import pandas as pd
from nflpicks.utils import winners
from nflpicks.utils.logs import logging



def get_points():
    
    try:
        win = winners.Winners()
        s = win.data_cleaner.wins()
        points = s.points
    except Exception as k:
        logging.error(f'We ignored {k.__name__}', exc_info=False)
        points = pd.DataFrame(
            {'picker_id':['Johnny','Anne','Rachel'],
            'points': [128, 102, 42]})
    return points.to_dict(orient='records')

    
