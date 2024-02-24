import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# IPL Matches Dataset

ipl=pd.read_csv('desktop/matches.csv')

ipl.head()

ipl.shape



# For Any Specific In Data Use Value Count Function

ipl['player_of_match'].value_counts()



# For Top 5 Use At Last

ipl['player_of_match'].value_counts()[0:5]


list(ipl['player_of_match'].value_counts()[0:5].keys())


# Choose The figure Size You Want In (X,Y) Axis

plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]))
plt.show()


ipl['result'].value_counts()


ipl['toss_winner'].value_counts()


# Extracting Records In Which Team Won Batting First

batting_first=ipl[ipl['win_by_runs']!=0]


plt.figure(figsize=(5,5))
plt.hist(batting_first['win_by_runs'])
plt.title('Distribution Of Runs')
plt.xlabel('Runs')
plt.show


batting_first['winner'].value_counts()


# Top 3 Teams Bar Plot

plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=['r','b','g'])
plt.show()



# In PIE Chart We Use labels In Second Parameter Of Data

plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


batting_second=ipl[ipl['win_by_wickets']!=0]


batting_second.head()


plt.figure(figsize=(5,5))
plt.hist(batting_second['win_by_wickets'],bins=20)
plt.show()


batting_second['winner'].value_counts()


# Top 3 Winner Teams Which Bat Second Bar Plot Chart

plt.figure(figsize=(6.5,6.5))
plt.bar(list(batting_second['winner'].value_counts().keys()[0:3]),list(batting_second['winner'].value_counts()[0:3]),color=('r','b','g'))
plt.show()


plt.figure(figsize=(5,5))
plt.pie(batting_second['winner'].value_counts(),labels=(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


ipl['season'].value_counts()


ipl['city'].value_counts()


# Finding Out How Many Teams Won The Match After Winning Toss

np.sum(ipl['toss_winner']==ipl['winner'])

