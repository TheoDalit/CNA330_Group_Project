import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib

engine = sqlalchemy.create_engine('mysql://root:@127.0.0.1:3306/twitch_data') # https://www.sqlshack.com/introduction-to-sqlalchemy-in-pandas-dataframe/

df = pd.read_sql_table('7d', engine) # Reads the databases
df1 = pd.read_sql_table('30d', engine)
df2 = pd.read_sql_table('90d', engine)

df2 = df2.sort_values(by='Stream time', ascending=False)

plt.bar(df2['Game'], df2['Stream time'], width=0.3, align='edge', label='Stream time (90 days)') # Video series that helped with matplotlib https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_
plt.bar(df2['Game'], df1['Stream time'], width=0.2, align='center', label='Stream time (30 days)')
plt.bar(df2['Game'], df['Stream time'], width=-0.2, align='edge', label='Stream time (7 days)')

plt.title('Stream time on Twitch in the past 90 days') # Title, labels, and axis formatting
plt.xlabel('Game')
plt.ylabel('Time (Hours)')
plt.xticks(rotation=-45, ha='left')
plt.yscale('log')
plt.grid(axis='y')
plt.legend()
plt.tight_layout()

formatter = matplotlib.ticker.ScalarFormatter() # Format for the y-axis so it isn't in scientific notation https://stackoverflow.com/questions/61449706/change-y-axis-tick-scale-with-log-bar-graph-python
formatter.set_powerlimits((0,15))
plt.gca().yaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_minor_locator(matplotlib.ticker.NullLocator())

plt.show()
