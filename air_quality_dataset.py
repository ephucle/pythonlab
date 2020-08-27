#!/usr/bin/env python3
#https://realpython.com/pandas-groupby/
import pandas as pd
from pathlib import Path
import sys

#HERE = Path(__file__).parent
DATA_FOLDER = Path('/mnt/c/cygwin/home/ephucle/tool_script/python/materials/pandas-groupby/groupby-data')
print(DATA_FOLDER)


# Use 3 decimal places in output display
pd.set_option("display.precision", 3)

# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 25)

df = pd.read_csv(
	DATA_FOLDER / "airqual.csv",
	#dtype=dtypes,
	usecols=["CO(GT)", "Date", "Time", "T", "RH", "AH"],
	parse_dates=[["Date", "Time"]],
	na_values=[-200],
).rename(columns= {
		"CO(GT)":"co",  
		"Date_Time": "tstamp",
		"T": "temp_c",
		"RH": "rel_hum",
		"AH": "abs_hum",
		}

	).set_index("tstamp")

print(df.info())
#old
#   Column         Non-Null Count  Dtype
#---  ------         --------------  -----
# 0   Date           9357 non-null   object
# 1   Time           9357 non-null   object
# 2   CO(GT)         9357 non-null   float64
# 3   PT08.S1(CO)    9357 non-null   int64
# 4   NMHC(GT)       9357 non-null   int64
# 5   C6H6(GT)       9357 non-null   float64
# 6   PT08.S2(NMHC)  9357 non-null   int64
# 7   NOx(GT)        9357 non-null   int64
# 8   PT08.S3(NOx)   9357 non-null   int64
# 9   NO2(GT)        9357 non-null   int64
# 10  PT08.S4(NO2)   9357 non-null   int64
# 11  PT08.S5(O3)    9357 non-null   int64
# 12  T              9357 non-null   float64
# 13  RH             9357 non-null   float64
# 14  AH             9357 non-null   float64
#dtypes: float64(5), int64(8), object(2)
#memory usage: 1.1+ MB

#new 
#Data columns (total 5 columns):
# #   Column   Non-Null Count  Dtype
#---  ------   --------------  -----
# 0   tstamp   9357 non-null   datetime64[ns]
# 1   co       9357 non-null   float64
# 2   temp_c   9357 non-null   float64
# 3   rel_hum  9357 non-null   float64
# 4   abs_hum  9357 non-null   float64
#dtypes: datetime64[ns](1), float64(4)
#memory usage: 365.6 KB

print(df)
#         Date      Time   co  temp_c  rel_hum  abs_hum
#0     3/10/04  18:00:00  2.6    13.6     48.9   0.7578
#1     3/10/04  19:00:00  2.0    13.3     47.7   0.7255
#2     3/10/04  20:00:00  2.2    11.9     54.0   0.7502
#3     3/10/04  21:00:00  2.2    11.0     60.0   0.7867
#4     3/10/04  22:00:00  1.6    11.2     59.6   0.7888
#...       ...       ...  ...     ...      ...      ...
#9352   4/4/05  10:00:00  3.1    21.9     29.3   0.7568
#9353   4/4/05  11:00:00  2.4    24.3     23.7   0.7119
#9354   4/4/05  12:00:00  2.4    26.9     18.3   0.6406
#9355   4/4/05  13:00:00  2.1    28.3     13.5   0.5139
#9356   4/4/05  14:00:00  2.2    28.5     13.1   0.5028

#new
#                 tstamp   co  temp_c  rel_hum  abs_hum
#0    2004-03-10 18:00:00  2.6    13.6     48.9   0.7578
#1    2004-03-10 19:00:00  2.0    13.3     47.7   0.7255
#2    2004-03-10 20:00:00  2.2    11.9     54.0   0.7502
#3    2004-03-10 21:00:00  2.2    11.0     60.0   0.7867
#4    2004-03-10 22:00:00  1.6    11.2     59.6   0.7888
#...                  ...  ...     ...      ...      ...
#9352 2005-04-04 10:00:00  3.1    21.9     29.3   0.7568
#9353 2005-04-04 11:00:00  2.4    24.3     23.7   0.7119
#9354 2005-04-04 12:00:00  2.4    26.9     18.3   0.6406
#9355 2005-04-04 13:00:00  2.1    28.3     13.5   0.5139
#9356 2005-04-04 14:00:00  2.2    28.5     13.1   0.5028
#
#[9357 rows x 5 columns]

#after set index
#                      co  temp_c  rel_hum  abs_hum
#tstamp
#2004-03-10 18:00:00  2.6    13.6     48.9   0.7578
#2004-03-10 19:00:00  2.0    13.3     47.7   0.7255
#2004-03-10 20:00:00  2.2    11.9     54.0   0.7502
#2004-03-10 21:00:00  2.2    11.0     60.0   0.7867
#2004-03-10 22:00:00  1.6    11.2     59.6   0.7888
#...                  ...     ...      ...      ...
#2005-04-04 10:00:00  3.1    21.9     29.3   0.7568
#2005-04-04 11:00:00  2.4    24.3     23.7   0.7119
#2005-04-04 12:00:00  2.4    26.9     18.3   0.6406
#2005-04-04 13:00:00  2.1    28.3     13.5   0.5139
#2005-04-04 14:00:00  2.2    28.5     13.1   0.5028
#
#[9357 rows x 4 columns]

print(df.index.min(),  type(df.index.min())) #2004-03-10 18:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(df.index.max(), type(df.index.max())) #2005-04-04 14:00:00 <class 'pandas._libs.tslibs.timestamps.Timestamp'>

day_names = df.index.day_name()
print(type(day_names)) #<class 'pandas.core.indexes.base.Index'>
print(day_names)
#Index(['Wednesday', 'Wednesday', 'Wednesday', 'Wednesday', 'Wednesday',
#       'Wednesday', 'Thursday', 'Thursday', 'Thursday', 'Thursday',
#       ...
#       'Monday', 'Monday', 'Monday', 'Monday', 'Monday', 'Monday', 'Monday',
#       'Monday', 'Monday', 'Monday'],
#      dtype='object', name='tstamp', length=9357)
print(df.groupby(day_names)["co"].mean())

#tstamp
#Friday       2.543
#Monday       2.017
#Saturday     1.861
#Sunday       1.438
#Thursday     2.456
#Tuesday      2.382
#Wednesday    2.401
#Name: co, dtype: float64

#check data
#print(df [df ['co'] == -200])
#old
#                        co  temp_c  rel_hum  abs_hum
#tstamp
#2004-03-11 04:00:00 -200.0    10.1     60.5   0.7465
#2004-03-12 04:00:00 -200.0     6.1     65.9   0.6248
#2004-03-12 09:00:00 -200.0     9.2     56.2   0.6561
#2004-03-13 04:00:00 -200.0     7.0     71.1   0.7158
#2004-03-14 04:00:00 -200.0    12.1     61.1   0.8603
#...                    ...     ...      ...      ...
#2005-03-23 04:00:00 -200.0    14.5     66.4   1.0919
#2005-03-26 04:00:00 -200.0    16.2     71.2   1.3013
#2005-03-29 04:00:00 -200.0    13.7     68.2   1.0611
#2005-04-01 04:00:00 -200.0    13.7     48.8   0.7606
#2005-04-04 04:00:00 -200.0    11.8     56.0   0.7743
#
#[1683 rows x 4 columns]

#after add na_values=[-200] to pd.read_csv
#Empty DataFrame
#Columns: [co, temp_c, rel_hum, abs_hum]
#Index: []


hr = df.index.hour
print(df.groupby(hr)["co"].mean())
#tstamp
#0     1.786
#1     1.468
#2     1.099
#3     0.888
#4     0.759
#5     0.713
#6     0.922
#7     1.811
#8     2.824
#9     2.972
#10    2.566
#11    2.261
#12    2.170
#13    2.201
#14    2.126
#15    2.049
#16    2.267
#17    2.816
#18    3.436
#19    3.733
#20    3.469
#21    2.601
#22    1.977
#23    1.878
#Name: co, dtype: float64

print(df.groupby([day_names,hr])["co"].mean())
#tstamp     tstamp
#Friday     0         1.936
#           1         1.609
#           2         1.172
#           3         0.887
#           4         0.823
#                     ...
#Wednesday  19        4.147
#           20        3.845
#           21        2.898
#           22        2.102
#           23        1.938
#Name: co, Length: 168, dtype: float64

#Here’s one more similar case that uses .cut() to bin the temperature values into discrete intervals:

#bins : int, sequence of scalars, or IntervalIndex
#
#If bins is an int, it defines the number of equal-width bins in the range of x. However, in this case, the range of x is extended by .1% on each side to include the min or max values of x. If bins is a sequence it defines the bin edges allowing for non-uniform bin width. No extension of the range of x is done in this case.
bins = pd.cut(df["temp_c"], bins=3, labels=("cool", "warm", "hot"))

print(bins)
#2004-03-10 18:00:00    cool
#2004-03-10 19:00:00    cool
#2004-03-10 20:00:00    cool
#2004-03-10 21:00:00    cool
#2004-03-10 22:00:00    cool
#                       ...
#2005-04-04 10:00:00    warm
#2005-04-04 11:00:00    warm
#2005-04-04 12:00:00    warm
#2005-04-04 13:00:00    warm
#2005-04-04 14:00:00    warm
#Name: temp_c, Length: 9357, dtype: category
#Categories (3, object): [cool < warm < hot]

#Resampling
#What if you wanted to group by an observation’s year and quarter? Here’s one way to accomplish that:
print(df.groupby([df.index.year, df.index.quarter])["co"].agg(
	["max", "min"]
	).rename_axis(["year", "quarter"]))
	
#               max  min
#year quarter
#2004 1         8.1  0.3
#     2         7.3  0.1
#     3         7.5  0.1
#     4        11.9  0.1
#2005 1         8.7  0.1
#     2         5.0  0.3

#same function, such as "Q" for "quarterly"
print(df.resample("Q")["co"].agg(["max", "min"]))
#             max  min
#tstamp
#2004-03-31   8.1  0.3
#2004-06-30   7.3  0.1
#2004-09-30   7.5  0.1
#2004-12-31  11.9  0.1
#2005-03-31   8.7  0.1
#2005-06-30   5.0  0.3
