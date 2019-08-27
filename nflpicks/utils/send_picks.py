from nflpicks import db
from nflpicks.models import Picks


def send_to_db(dt, games_count, games_data, user_data):

    if dt.shape[0] == games_count:
        print('True match completed')

        dt = dt.assign(round=lambda x: games_data['check_round'][0],
                       axis=1)
        dt = dt.assign(picker_id=lambda x: user_data['user'], axis=1)

        dt = dt[['picker_id', 'round', 'winner', 'loser']]

        print('Trying to send data to DB')
        _ = dt.apply(lambda x: db.session.add(
                                    Picks(x['picker_id'],
                                          x['round'],
                                          x['winner'],
                                          x['loser'])),
                     axis=1)

        db.session.commit()
        print('[Success] Data in DB')

    else:
        print('[Failed]  Not Data to Send DB')
