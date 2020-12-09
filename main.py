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
df['Watch time'] = df['Watch time'].astype(float)
df['Stream time'] = df['Stream time'].astype(float)
df['Peak viewers'] = df['Peak viewers'].astype(float)
df['Peak channels'] = df['Peak channels'].astype(float)
df['Streamers'] = df['Streamers'].astype(float)
df['Average viewers'] = df['Average viewers'].astype(float)
df['Average channels'] = df['Average channels'].astype(float)
df['Average viewer ratio'] = df['Average viewer ratio'].astype(float)
df['Followers gained'] = df['Followers gained'].astype(float)
df['Views gained'] = df['Views gained'].astype(float)

df1 = pd.read_csv('Wt30.csv', nrows=50, usecols = ['Game', 'Watch time', 'Stream time',
                                               'Peak viewers', 'Peak channels',
                                               'Streamers', 'Average viewers',
                                               'Average channels', 'Average viewer ratio',
                                               'Followers gained', 'Views gained']) # Most watched games on twitch past 30 days.
df1['Watch time'] = df1['Watch time'].astype(float)
df1['Stream time'] = df1['Stream time'].astype(float)
df1['Peak viewers'] = df1['Peak viewers'].astype(float)
df1['Peak channels'] = df1['Peak channels'].astype(float)
df1['Streamers'] = df1['Streamers'].astype(float)
df1['Average viewers'] = df1['Average viewers'].astype(float)
df1['Average channels'] = df1['Average channels'].astype(float)
df1['Average viewer ratio'] = df1['Average viewer ratio'].astype(float)
df1['Followers gained'] = df1['Followers gained'].astype(float)
df1['Views gained'] = df1['Views gained'].astype(float)

df2 = pd.read_csv('Wt90.csv', nrows=50, usecols = ['Game', 'Watch time', 'Stream time',
                                               'Peak viewers', 'Peak channels',
                                               'Streamers', 'Average viewers',
                                               'Average channels', 'Average viewer ratio',
                                               'Followers gained', 'Views gained']) # Most watched games on twitch past 90 days.
df2['Watch time'] = df2['Watch time'].astype(float)
df2['Stream time'] = df2['Stream time'].astype(float)
df2['Peak viewers'] = df2['Peak viewers'].astype(float)
df2['Peak channels'] = df2['Peak channels'].astype(float)
df2['Streamers'] = df2['Streamers'].astype(float)
df2['Average viewers'] = df2['Average viewers'].astype(float)
df2['Average channels'] = df2['Average channels'].astype(float)
df2['Average viewer ratio'] = df2['Average viewer ratio'].astype(float)
df2['Followers gained'] = df2['Followers gained'].astype(float)
df2['Views gained'] = df2['Views gained'].astype(float)

df.to_sql('7d', engine, if_exists = 'replace', index=False) # Writes to the database
df1.to_sql('30d', engine, if_exists = 'replace', index=False)
df2.to_sql('90d', engine, if_exists = 'replace', index=False)
