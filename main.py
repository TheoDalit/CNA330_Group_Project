# Theodore Dalit, Matthew Williams, Mychael Huynh
# CNA330
# This script is based off the most watched games on Twitch.tv from the past 90, 30, and 7 days.
# This script uses pandas to pull from CSV files and creates databases from it.
# The CSV files are datasets taken from https://sullygnome.com/games/90/watched

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:@127.0.0.1:3306/twitch_data') # Change this according to your own database settings ‘mysql://username:password@databasehost:port/databasename’ https://www.sqlshack.com/introduction-to-sqlalchemy-in-pandas-dataframe/

df = pd.read_csv('Wt7.csv', nrows=50, usecols = ['Game', 'Watch time', 'Stream time',
                                               'Peak viewers', 'Peak channels',
                                               'Streamers', 'Average viewers',
                                               'Average channels', 'Average viewer ratio',
                                               'Followers gained', 'Views gained']) # Most watched games on twitch past 7 days.

df1 = pd.read_csv('Wt30.csv', nrows=50, usecols = ['Game', 'Watch time', 'Stream time',
                                               'Peak viewers', 'Peak channels',
                                               'Streamers', 'Average viewers',
                                               'Average channels', 'Average viewer ratio',
                                               'Followers gained', 'Views gained']) # Most watched games on twitch past 30 days.

df2 = pd.read_csv('Wt90.csv', nrows=50, usecols = ['Game', 'Watch time', 'Stream time',
                                               'Peak viewers', 'Peak channels',
                                               'Streamers', 'Average viewers',
                                               'Average channels', 'Average viewer ratio',
                                               'Followers gained', 'Views gained']) # Most watched games on twitch past 90 days.

df.to_sql('7d', engine, if_exists = 'replace', index=False) # Writes to the database
df1.to_sql('30d', engine, if_exists = 'replace', index=False)
df2.to_sql('90d', engine, if_exists = 'replace', index=False)
