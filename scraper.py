import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

test_url  = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
r = requests.get(url=test_url).json()
table_headers = r['resultSet']['headers']

temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
temp_df2 = pd.DataFrame({'Year':['2012-13' for i in range(len(temp_df1))],
                        'Season_type':['Regular%20Season' for i in range(len(temp_df1))]})
temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
print(temp_df3)