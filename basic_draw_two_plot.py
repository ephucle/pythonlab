import sys
import pandas as pd
import matplotlib.pyplot as plt
x = range(5)
y = [2*i for i in x]
z = [i*i for i in x]
df = pd.DataFrame({'x':x, 'y':y, 'z': z})

#df
#   x  y   z
#0  0  0   0
#1  1  2   1
#2  2  4   4
#3  3  6   9
#4  4  8  16

colx_y =df[['x', 'y']]
print(type(colx_y))  #<class 'pandas.core.frame.DataFrame'>
#   x  y
#0  0  0
#1  1  2
#2  2  4
#3  3  6
#4  4  8

colx = df['x']
print(type(colx)) #<class 'pandas.core.series.Series'>

