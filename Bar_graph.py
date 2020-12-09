# Theodore Dalit, Matthew Williams, Mychael Huynh
# CNA330
# This script reads the different databases and graphs a bar graph comparing the peak viewers from the most
# watched games on Twitch.tv in the past 90, 30, and 7 days.

import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
plt.close('all')

engine = sqlalchemy.create_engine('mysql://root:@127.0.0.1:3306/twitch_data') # Change this according to your own database settings ‘mysql://username:password@databasehost:port/databasename’ https://www.sqlshack.com/introduction-to-sqlalchemy-in-pandas-dataframe/

df = pd.read_sql_table('7d', engine) # Reads the databases
df1 = pd.read_sql_table('30d', engine)
df2 = pd.read_sql_table('90d', engine)

plt.bar(df2['Game'], df2['Peak viewers'], width=0.3, align='edge', label='Peak viewers (90 days)') # Video series that helped with matplotlib https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
plt.bar(df1['Game'], df1['Peak viewers'], width=0.2, align='center', label='Peak viewers (30 days)')
plt.bar(df['Game'], df['Peak viewers'], width=-0.2, align='edge', label='Peak viewers (7 days)')
plt.title('Most watched games on Twitch in the past 90 days')
plt.xlabel('Game')
plt.ylabel('Viewers')
plt.xticks(rotation=-45, ha='left')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()
