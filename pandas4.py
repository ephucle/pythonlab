#!/usr/bin/env python
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
import pandas as pd
import numpy as np
df = pd.DataFrame({'x1': [0,1, 2, 3,4], 'x2': [ 5,6,7,8,9]})
#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ ./pandas4.py
#   x1  x2
#0   0   5
#1   1   6
#2   2   7
#3   3   8
#4   4   9
#df.x2 = df.x2.shift(1)
print(df)
#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ ./pandas4.py
#   x1   x2
#0   0  NaN
#1   1  5.0
#2   2  6.0
#3   3  7.0
#4   4  8.0


df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
				  
print(df)
#     A    B   C  D
#0  NaN  2.0 NaN  0
#1  3.0  4.0 NaN  1
#2  NaN  NaN NaN  5
#3  NaN  3.0 NaN  4