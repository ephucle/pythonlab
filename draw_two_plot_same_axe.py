import sys
import pandas as pd
import matplotlib.pyplot as plt

left_2013 = pd.DataFrame(
    {'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
               'oct', 'nov', 'dec'],
     '2013_val': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 6]})

#print(left_2013)
#sys.exit()

right_2014 = pd.DataFrame({'month': ['jan', 'feb'], '2014_val': [4, 5]})

print(right_2014)
#sys.exit()

right_2014_target = pd.DataFrame(
    {'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep',
               'oct', 'nov', 'dec'],
     '2014_target_val': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]})

print(right_2014_target)


df_13_14 = pd.merge(left_2013, right_2014, how='outer')
print(df_13_14)

#sys.exit()

df_13_14_target = pd.merge(df_13_14, right_2014_target, how='outer')
print(df_13_14_target)

#ax = df_13_14_target[['month', '2014_target_val']].plot(x='month', linestyle='-', marker='o')
ax = df_13_14_target[['month', '2014_target_val']].plot(x='month', kind = "line" ,linestyle='-', marker='o')

df_13_14_target[['month', '2013_val', '2014_val']].plot(x='month', kind='bar',ax=ax)

plt.show()