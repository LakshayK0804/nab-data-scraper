import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

test_url  = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
r = requests.get(url=test_url).json()
table_headers = r['resultSet']['headers']


#print(temp_df3)
df_cols = ['Year', 'Season_type'] + table_headers

df = pd.DataFrame(columns=df_cols)
season_types = ['Regular%20Season', 'Playoffs']
years = ['2010-11','2011-12','2012-13', '2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23','2023-24']
begin_loop = time.time()

for y in years:
    for s in season_types:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
        r = requests.get(url=api_url).json()
        temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year':[y for i in range(len(temp_df1))],
                                'Season_type':[s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
        df=pd.concat([df,temp_df3], axis=0)
        print(f'Finished scraping data for the {y} {s}')
        lag = np.random.uniform(low=5,high=40)
        print(f'...waiting {round(lag, 1)} seconds')
        time.sleep(lag)

print(f'process completed!')
df.to_excel('player_data.xlsx', index=False)