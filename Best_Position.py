import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



'''
Categorizing players by Goalkeepers, Defenders, Midfielders and Forwards, my hypothesis is that Forwards are the best football players and I hope to prove this using FIFA 18's data.

Wingers will be regarded as Forwards and wing backs will be regarded as defenders
'''

'''
FIFA 2018 data set taken from kaggle
https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset/version/5
'''

df = pd.read_csv('CompleteDataset.csv', low_memory = False)

'''
Some explaratory data analyses
'''

print(df.head())
print(df.tail())
print(df.columns)

'''

getting rid of unneeded columns

'''

df = df[['Name', 'Age', 'Overall', 'Preferred Positions']]
print(df.columns)

'''

I regard the top players as those that have an overall rating better than 1.25 times better than the average
This happens to be 83

'''

df_top_overall = df[df['Overall'] > 1.25*df.Overall.mean()].sort_values(by=['Overall'], ascending=False)
print(df_top_overall.head())
print(df_top_overall.tail())


top_position_numbers = {'GK' : 0, 'DF' : 0, 'MF' : 0, 'FW' : 0}
for position in df_top_overall['Preferred Positions']:
    if position.startswith('GK'):
        top_position_numbers['GK'] += 1
    elif position.startswith('CB')or position.startswith('LB') or position.startswith('RB'):
        top_position_numbers['DF'] += 1
    elif position.startswith('CDM') or position.startswith('CM') or position.startswith('RM') or position.startswith('LM') or position.startswith('CAM'):
        top_position_numbers['MF'] += 1
    elif position.startswith('LW') or position.startswith('RW') or position.startswith('ST') or position.startswith('CF'):
        top_position_numbers['FW'] += 1

'''
Kyle Walker's position is listed as "RWB RB "
this means he would've been added to the forwards
'''
df_RWB = df_top_overall[df['Preferred Positions'] == 'RWB RB ']
print(df_RWB)

print(top_position_numbers)

'''
ammending the kyle walker error
'''

top_position_numbers['FW'] -= 1
top_position_numbers['DF'] += 1


print(top_position_numbers)


'''

let's visualise these results

'''

plt.bar(*zip(*sorted(top_position_numbers.items())))
plt.show()


'''

From these result according to FIFA 2018 overall stats the Midfielders are the best players

These results need to be taken with a pinch of salt as many players who are midfielders are also Forwards as their secondary position and are often utilised in other positions.
These results could also be due to the fact that a team has more midfielders than any position.
A method for further exploration would be to take a sample of the top 50 players in each position and then compare their averages.

Final Results:
{'GK': 27, 'DF': 49, 'MF': 73, 'FW': 49}

'''
