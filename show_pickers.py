# Show User and Max Round Picked

import sqlite3
import pandas as pd


query = ('SELECT DISTINCT picker_id, MAX(round) AS round FROM picks '
         'GROUP BY picker_id ORDER BY round DESC')
con = sqlite3.connect('nflpicks/data/data.sqlite')

df = pd.read_sql(query, con)

df['notify'] = df['round'] < df['round'].max()
df = df.rename({'picker_id': 'pickers'}, axis=1)

print('Notify True Users\n')
print(df)
