#!/usr/bin/env python
import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)

print(df['one'])

#select two column
print(df[['one', 'two']])

print(df.columns[0:2])  #Index(['one', 'two'], dtype='object')

print(df[df.columns[0:2]])

#        one       two
#a -1.289048  0.832361
#b       NaN       NaN
#c -0.763149  1.779659
#d       NaN       NaN
#e  0.299092  0.572636
#f  0.590388 -0.200650
#g       NaN       NaN
#h -0.433992 -1.224091
