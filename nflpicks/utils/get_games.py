import pandas as pd
from nflpicks.utils import get_data


class GetGames:
    '''pass
    '''

    def __init__(self, round=1, today=None):

        data = get_data.GetData()
        self.games = data.fetch.scrap_fixture()

        if today is None:
            today = pd.datetime.now()
        self.round = round
        self.today = today

    @property
    def round_games(self):
        mask = (self.games.df['check_round'] == self.round
                ) & (self.games.df['game_dt'] > self.today)

        return self.games.df[mask]
