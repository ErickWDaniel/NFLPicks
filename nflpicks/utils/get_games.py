import pandas as pd
from nflpicks.utils import get_data


class GetGames:
    '''pass
    '''

    def __init__(self, today=None):

        data = get_data.GetData()
        self.games = data.fetch.scrap_fixture()

        if today is None:
            today = pd.datetime.now()

        round_dates = self.games.df.groupby('check_round')[
            'game_dt'].agg(['min', 'max'])

        print(f'Assuming future: actual today {today}')
        today += pd.Timedelta(days=3)  # Assuming future( Remove later)
        week_later = today + pd.Timedelta(days=7)
        print(f'Assuming future: fake today {today}')

        self.round = round_dates[round_dates['min']
                                 <= week_later].index.values[0]

        self.today = today

        self.all_games = self.games.df


    @property
    def round_games(self):
        mask = (self.games.df['check_round'] == self.round
                ) & (self.games.df['game_dt'] > self.today)

        return self.games.df[mask]
