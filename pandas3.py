#!/usr/bin/env python
#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

#https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)
print(dates)
print(type(dates))

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
#                   A         B         C         D
#2000-01-01  1.602868  0.350132 -1.585676  1.746061
#2000-01-02 -0.116802  0.073141  0.069216 -0.322130
#2000-01-03  0.513310 -1.082456  1.727792 -0.254612
#2000-01-04  1.662068 -1.866598 -0.204887 -1.126883
#2000-01-05 -0.957771 -0.004574  1.747949  1.474672
#2000-01-06  1.938112 -0.306607 -1.288822  1.309355
#2000-01-07 -2.812086  1.669614 -0.449197  0.153111
#2000-01-08  0.685334  0.356475  0.828709  0.103675

s = df['A']
print(s, s.shape)
print(s[dates[5]])

#DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
#               '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08'],
#              dtype='datetime64[ns]', freq='D')
#<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
#                   A         B         C         D
#2000-01-01 -0.661460 -0.153772 -1.060624 -0.051188
#2000-01-02 -0.660511 -0.762316  0.188735 -1.386994
#2000-01-03  0.485998  0.075377  1.297933  0.778210
#2000-01-04  0.671885 -1.219082 -0.385959  1.122694
#2000-01-05  1.481818 -0.667114  0.487491  2.252396
#2000-01-06  1.570612  0.518857 -0.594049  0.131551
#2000-01-07  0.470750  0.287938  1.605534  1.327092
#2000-01-08  0.561448  0.414237 -0.766321 -0.769881
#2000-01-01   -0.661460
#2000-01-02   -0.660511
#2000-01-03    0.485998
#2000-01-04    0.671885
#2000-01-05    1.481818
#2000-01-06    1.570612<====
#2000-01-07    0.470750
#2000-01-08    0.561448
#Freq: D, Name: A, dtype: float64 (8,)
#1.5706121383110034  ===> s[dates[5]]   (dates[5] = '2000-01-06')

print(df[['A', 'B']])
df[['B', 'A']] = df[['A', 'B']]
print(df[['A', 'B']])


#                   A         B
#2000-01-01  1.722978 -0.384697
#2000-01-02 -1.751995  0.904858
#2000-01-03  0.003871  1.100479
#2000-01-04 -0.147601  0.808737
#2000-01-05 -0.690789 -1.613931
#2000-01-06 -0.054220 -1.299334
#2000-01-07 -1.341368 -0.942909
#2000-01-08 -1.433051  1.355884
#                   A         B
#2000-01-01 -0.384697  1.722978
#2000-01-02  0.904858 -1.751995
#2000-01-03  1.100479  0.003871
#2000-01-04  0.808737 -0.147601
#2000-01-05 -1.613931 -0.690789
#2000-01-06 -1.299334 -0.054220
#2000-01-07 -0.942909 -1.341368
#2000-01-08  1.355884 -1.433051

sa = pd.Series([1, 2, 3], index=list('abc')) 
dfa = df.copy()

print(sa, type(sa))  
#a    1
#b    2
#c    3
#dtype: int64 <class 'pandas.core.series.Series'>


print(sa.b, sa.a, sa.c)  #2 1 3
print (dfa.A, "\n",type(dfa.A))

#2000-01-01   -1.814482
#2000-01-02    0.202293
#2000-01-03    1.122820
#2000-01-04   -0.307967
#2000-01-05    0.095379
#2000-01-06    0.883080
#2000-01-07    0.908124
#2000-01-08   -0.160006
#Freq: D, Name: A, dtype: float64

#<class 'pandas.core.series.Series'>

sa.a = 10
print(sa)

#a    10  <===
#b     2
#c     3
#dtype: int64

dfa.A = list(range(len(dfa.index)))  # ok if A already exists
print(dfa)
#            A         B         C         D
#2000-01-01  0 -2.226635  0.123095 -0.160513
#2000-01-02  1  0.677840 -0.063026 -0.245209
#2000-01-03  2 -0.526444 -1.547377  0.267135
#2000-01-04  3 -2.064781 -0.499199 -1.709043
#2000-01-05  4 -1.605205 -0.317207  0.012128
#2000-01-06  5  0.259763  0.955246 -1.128148
#2000-01-07  6 -1.300691 -0.403016 -1.013060
#2000-01-08  7  2.090782 -2.049009 -0.544172

dfa['E'] = list(range(len(dfa.index)))  # use this form to create a new column
print(dfa)
#            A         B         C         D  E
#2000-01-01  0  0.261927  0.726791 -0.060020  0
#2000-01-02  1 -0.242354  0.570750  0.174102  1
#2000-01-03  2 -0.088569  0.648275 -0.600566  2
#2000-01-04  3  0.146246  0.756152  0.805622  3
#2000-01-05  4  0.669240  0.038790 -1.387015  4
#2000-01-06  5 -2.316866  1.110778  1.128867  5
#2000-01-07  6 -0.659295 -1.186056  2.023476  6
#2000-01-08  7  0.705169 -0.716454 -1.052348  7


x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
print(x)
#   x  y
#0  1  3
#1  2  4
#2  3  5

#You can also assign a dict to a row of a DataFrame:
x.iloc[1] = {'x': 20, 'y': 40}  #modify row 1 by iloc
print(x)
#    x   y
#0   1   3
#1  20  40
#2   3   5

dfx = pd.DataFrame({'one': [1., 2., 3.]})
#df.two = [4, 5, 6]  
#warning pandas3.py:149: UserWarning: Pandas doesn't allow columns to be created via a new attribute name - see https://pandas.pydata.org/pandas-docs/stable/indexing.html#attribute-access
# df.two = [4, 5, 6]

#fix this
dfx['two'] = [4,5,6]
print(df)
#   one  two
#0  1.0    4
#1  2.0    5
#2  3.0    6

#Slicing ranges¶
print(s)
#2000-01-01   -0.147010
#2000-01-02    0.713779
#2000-01-03   -0.247310
#2000-01-04    0.333229
#2000-01-05    1.725655
#2000-01-06    0.807154
#2000-01-07   -0.295523
#2000-01-08   -0.068787
#Freq: D, Name: A, dtype: float64
print(s[:5])
#2000-01-01   -0.147010
#2000-01-02    0.713779
#2000-01-03   -0.247310
#2000-01-04    0.333229
#2000-01-05    1.725655
#Freq: D, Name: A, dtype: float64

print(s[::2])
#2000-01-01   -0.432090
#2000-01-03   -0.999437
#2000-01-05    0.525866
#2000-01-07   -0.019130
#Freq: 2D, Name: A, dtype: float64

print(s[::-1])
#2000-01-08   -0.905545
#2000-01-07   -1.793023
#2000-01-06   -0.043694
#2000-01-05    1.660516
#2000-01-04    0.234835
#2000-01-03    0.606784
#2000-01-02   -0.354328
#2000-01-01   -0.671984
#Freq: -1D, Name: A, dtype: float64

s2 = s.copy()
s2[:5] = 0
print(s2)
#2000-01-01    0.000000
#2000-01-02    0.000000
#2000-01-03    0.000000
#2000-01-04    0.000000
#2000-01-05    0.000000
#2000-01-06    0.594348
#2000-01-07   -1.109338
#2000-01-08   -0.259261
#Freq: D, Name: A, dtype: float64

#With DataFrame, slicing inside of [] slices the rows. This is provided largely as a convenience since it is such a common operation.
print(df)

#                   A         B         C         D
#2000-01-01 -0.079323 -1.215530  0.031367 -0.686720
#2000-01-02  0.372868 -0.053056 -0.846434  1.459085
#2000-01-03 -0.775991  0.921461 -0.752750  0.441469
#2000-01-04  0.441639  0.575536  0.390241  0.842933
#2000-01-05  1.198024  0.652070  1.737948 -0.057456
#2000-01-06 -1.080374  0.834225 -1.258854 -0.312607
#2000-01-07  2.162759  0.625425  0.144485  1.405122
#2000-01-08  1.828783 -0.857140  1.328280  0.028883
print(df[:3])
#                   A         B         C         D
#2000-01-01 -0.054167 -0.474083  1.389365  0.750958
#2000-01-02  0.818501  0.547317  1.390717  1.006611
#2000-01-03  0.552822 -1.081187  0.580804  0.477570
print(df[::-1])
#                   A         B         C         D
#2000-01-08 -1.620555 -0.485163  0.512095  2.015384
#2000-01-07 -1.451583  0.528065 -0.494810  2.957511
#2000-01-06  0.766385  2.393887 -1.571419 -1.607854
#2000-01-05 -0.572316  1.417072 -0.609748 -0.352637
#2000-01-04  0.138585  0.936458  1.266479  1.516948
#2000-01-03  0.688926  0.914088 -1.416465 -1.275302
#2000-01-02  1.269053  0.446309  0.882227 -0.324024
#2000-01-01  1.181708  0.300565 -0.006371  2.495646


dfl = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'),index=pd.date_range('20130101', periods=5))
print(dfl)
#                   A         B         C         D
#2013-01-01 -0.887254  1.020647  0.675561 -0.792749
#2013-01-02 -0.487367  0.893489  0.592571  0.795277
#2013-01-03  2.112594  0.907859 -0.509239 -0.968670
#2013-01-04  0.308868 -0.983970  2.314069 -1.369000
#2013-01-05  1.763875 -1.271379 -1.499814 -0.845821
#print(dfl.loc[2:3])  #TypeError: cannot do slice indexing on <class 'pandas.core.indexes.datetimes.DatetimeIndex'> with these indexers [2] of <class 'int'>

print(dfl.loc['20130102':'20130104'])
#                   A         B         C         D
#2013-01-02  1.106674 -0.060431 -0.831519  0.308548
#2013-01-03 -0.250762  0.535067 -0.751850  1.120964
#2013-01-04  1.524178 -1.290070  0.353586  1.537178



s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
print(s1)
#a    0.920785
#b    0.617624
#c    0.186792
#d   -0.341279
#e    0.248373
#f   -0.361739
#dtype: float64
print(s1.loc['c':])
#c    0.768770
#d   -0.769576
#e   -0.972409
#f    0.516055
#dtype: float64

print(s1.loc['b'])  #==>0.768770
s1.loc['c':] = 0
print(s1)
#a   -1.005843
#b    1.506321
#c    0.000000
#d    0.000000
#e    0.000000
#f    0.000000
#dtype: float64


df1 = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
print(df1)
#          A         B         C         D
#a -0.702435  1.177559  0.780932  1.108739
#b -1.405549 -1.348540 -2.430458 -0.211017
#c  1.040244  1.094935  0.976991  1.638355
#d  0.688495 -1.087876 -0.326134  0.498374
#e -0.260185  0.106972 -1.177852 -0.240825
#f -0.093155 -1.636237 -0.742823 -1.219361

print(df1.loc[['a', 'b', 'd'], :])
#          A         B         C         D
#a -0.596418  0.549593  0.845238  0.022001
#b -1.430475 -1.188122  1.009530  2.098821
#d  0.477519  0.488646  0.719775 -0.941347
print(df1.loc[['a', 'b', 'd'], ['A', 'D']])

#          A         D
#a -0.201463  0.361931
#b  0.672303  0.790099
#d  0.428271 -0.595896
print(df1.loc['d':, 'A':'C'])
#          A         B         C
#d  0.566874 -1.148012 -0.152846
#e  1.519347  1.073838 -0.756132
#f  1.339995 -1.990319  0.601080

print(df1.loc['a'])
#A    1.435635
#B   -0.919258
#C   -0.890521
#D   -0.054632
#Name: a, dtype: float64
print(df1.loc['a'] > 0)
#A   -0.280483
#B    0.066091
#C    2.338203
#D   -0.793658
#Name: a, dtype: float64
#A    False
#B     True
#C     True
#D    False
#Name: a, dtype: bool

#For getting a value explicitly:
print(df1.loc['a', 'A']) #-1.2764078472360987

print(df1.iloc[[1, 3, 5], [1, 3]])
#          B         D
#b -1.025628 -0.037002
#d -2.221235  0.617687
#f  1.163686  0.668555
print(df1.iloc[[0], [0]])
#          A
#a -0.107308

print(df1.iloc[1:3, :])
#          A         B         C         D
#b -0.334897 -0.063722 -1.960813  1.410355
#c  0.399673 -0.233062 -1.034042 -0.123945

print(df1.iloc[1])
#A   -0.112937
#B    0.657887
#C   -0.341545
#D    0.890924
#Name: b, dtype: float64

df1 = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'),columns=list('ABCD'))
print(df1)