import sqlite3
import pandas as pd
from nflpicks.utils import get_games, get_data
from nflpicks.utils.logs import logging


class Winners:
    '''pass
    '''

    def __init__(self, database=None):

        if database is None:
            database = 'nflpicks/data/data.sqlite'

        self.database = database

        con = sqlite3.connect(database)

        self.picks = pd.read_sql('SELECT * FROM picks', con)
        self.picks.loc[:, 'winner'] = self.picks['winner'].str.replace(
            '-', ' ').str.title()
        self.picks.loc[:, 'date'] = pd.to_datetime(self.picks['date'])

        games_rounds = get_games.GetGames().all_games
        self.games_rounds = games_rounds.groupby(
            'check_round').count()[['games']]

        data = get_data.GetData(end_point='results')

        self.results = data.fetch.scrap_result().df
        self.results.loc[:, 'game_date'] = pd.to_datetime(
            self.results['game_date'])

        self.results = self.results[self.results['game_date']
                                    > self.picks['date'].min()]

    @property
    def data_cleaner(self):

        con = sqlite3.connect(self.database)
        cursor = con.cursor()

        check_picks = self.picks.groupby(
            ['picker_id', 'round']).count().reset_index()
        correct_picks = check_picks[check_picks['winner'] > 16].rename(
            {'winner': 'n_count'}, axis=1)

        correct_pickers = ((picker, rounds, wrong) for _, picker,
                           rounds, wrong in correct_picks[['picker_id', 'round', 'n_count']].to_records())
        try:
            for picker, rounds, wrong in correct_pickers:
                actual_games_rounds = self.games_rounds.loc[rounds].iloc[0]
                to_delete = wrong - actual_games_rounds
                delete_query = (
                    f'''DELETE FROM picks WHERE picks.picker_id = "{picker}" AND picks.round = {rounds} AND picks.id IN (SELECT id FROM picks ORDER BY id DESC LIMIT {to_delete})''')

                logging.info(delete_query)
                logging.info(f'{picker} had {to_delete} rows removed')

                cursor.execute(delete_query)
                con.commit()

        except KeyError as k:
             logging.error(f'We ignored KeyError', exc_info=False)
             pass

        self.picks = pd.read_sql('SELECT * FROM picks', con)
        self.picks.loc[:, 'winner'] = self.picks['winner'].str.replace(
            '-', ' ').str.title()
        self.picks.loc[:, 'date'] = pd.to_datetime(self.picks['date'])

        return self

    def wins(self, point=1):
        results = self.results[['game_date', 'game_round', 'winner']]
        results.loc[:, 'game_round'] = results['game_round'].apply(
            lambda x: x.split(' ')[-1])
        results.loc[:, 'round_winner'] = results['game_round'] + \
            results['winner']

        results_poll = results['round_winner'].tolist()

        pickers = self.picks[['picker_id', 'round', 'winner']]
        pickers.loc[:, 'round_winner'] = pickers['round'].astype(
            str) + pickers['winner']

        pickers.loc[:, 'points'] = pickers['round_winner'].apply(
            lambda x: point if x in results_poll else 0)
        pickers = pickers.drop(columns='round_winner', axis=1)

        self.get_result = pickers
        self.points = pickers.groupby(
            'picker_id')['points'].sum().reset_index()

        return self
