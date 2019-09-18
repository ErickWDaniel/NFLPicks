from nflpicks import db
from nflpicks.models import Picks

from nflpicks.utils.logs import logging


def send_to_db(dt, games_count, games_data, user_data):

    if dt.shape[0] == games_count:
        logging.info(
            f"{user_data['user']} completed round: {games_data['check_round'].iloc[0]}")

        dt = dt.assign(round=lambda x: games_data['check_round'].iloc[0],
                       axis=1)
        dt = dt.assign(picker_id=lambda x: user_data['user'], axis=1)

        dt = dt[['picker_id', 'round', 'winner', 'loser']]

        logging.info('Trying to send data to DB')
        _ = dt.apply(lambda x: db.session.add(
            Picks(x['picker_id'],
                  x['round'],
                  x['winner'],
                  x['loser'])),
            axis=1)

        db.session.commit()
        logging.info('[Success] Data sent to DB')

        return 'complete'

    else:
        logging.info('[Failed]  No complete data to send to DB')

    return 'incomplete'
