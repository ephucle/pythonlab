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

dtypes = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}

df = pd.read_csv(
	DATA_FOLDER / "legislators-historical.csv",
	dtype=dtypes,
	usecols=list(dtypes) + ["birthday", "last_name"],
	parse_dates=["birthday"]  #convert from string object to datetime64[ns]
)

#df = pd.read_csv(
#	DATA_FOLDER / "legislators-historical.csv",
#	dtype=dtypes,
#	usecols=list(dtypes) + ["birthday", "last_name"],
#	parse_dates=["birthday"]
#)

print(df)

#      last_name  first_name   birthday gender type state                party
#0       Bassett     Richard 1745-04-02      M  sen    DE  Anti-Administration
#1         Bland  Theodorick 1742-03-21      M  rep    VA                  NaN
#2         Burke     Aedanus 1743-06-16      M  rep    SC                  NaN
#3       Carroll      Daniel 1730-07-22      M  rep    MD                  NaN
#4        Clymer      George 1739-03-16      M  rep    PA                  NaN
#...         ...         ...        ...    ...  ...   ...                  ...
#11970   Garrett      Thomas 1972-03-27      M  rep    VA           Republican
#11971    Handel       Karen 1962-04-18      F  rep    GA           Republican
#11972     Jones      Brenda 1959-10-24      F  rep    MI             Democrat
#11973    Marino         Tom 1952-08-15      M  rep    PA           Republican
#11974     Jones      Walter 1943-02-10      M  rep    NC           Republican
#
#[11975 rows x 7 columns]
#<class 'pandas.core.frame.DataFrame'>

print(df.info())


#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 11975 entries, 0 to 11974
#Data columns (total 34 columns):
# #   Column              Non-Null Count  Dtype
#---  ------              --------------  -----
# 0   last_name           11975 non-null  object
# 1   first_name          11975 non-null  category
# 2   middle_name         8358 non-null   object
# 3   suffix              422 non-null    object
# 4   nickname            227 non-null    object
# 5   full_name           341 non-null    object
# 6   birthday            11422 non-null  object
# 7   gender              11975 non-null  category
# 8   type                11975 non-null  category
# 9   state               11975 non-null  category
# 10  district            10146 non-null  float64
# 11  senate_class        1829 non-null   float64
# 12  party               11741 non-null  category
# 13  url                 646 non-null    object
# 14  address             349 non-null    object
# 15  phone               345 non-null    object
# 16  contact_form        221 non-null    object
# 17  rss_url             203 non-null    object
# 18  twitter             0 non-null      float64
# 19  facebook            0 non-null      float64
# 20  youtube             0 non-null      float64
# 21  youtube_id          0 non-null      float64
# 22  bioguide_id         11975 non-null  object
# 23  thomas_id           1800 non-null   float64
# 24  opensecrets_id      665 non-null    object
# 25  lis_id              191 non-null    object
# 26  fec_ids             538 non-null    object
# 27  cspan_id            415 non-null    float64
# 28  govtrack_id         11975 non-null  int64
# 29  votesmart_id        558 non-null    float64
# 30  ballotpedia_id      191 non-null    object
# 31  washington_post_id  0 non-null      float64
# 32  icpsr_id            11763 non-null  float64
# 33  wikipedia_id        11973 non-null  object
#dtypes: category(5), float64(11), int64(1), object(17)
#memory usage: 2.8+ MB
#None

print(df.dtypes)
#print(df.groupby("state")["last_name"])
df_by_state  = df.groupby("state")
print(type(df_by_state)) #<class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# Summary stats over states

print(df_by_state.describe().head())
#      last_name                                      first_name                                 birthday                                              gender                             type                             party
#          count unique           top freq first last      count unique      top freq first last    count unique        top freq      first       last  count unique top freq first last count unique  top freq first last count unique       top freq first last
#state
#
#AK           16     15        Begich    2   NaN  NaN         16     15    Frank    2   NaN  NaN       16     16 1857-08-24    1 1848-09-17 1962-03-30     16      1   M   16   NaN  NaN
# 16      2  rep   10   NaN  NaN    14      3  Democrat    8   NaN  NaN
#AL          206    178      Bankhead    4   NaN  NaN        206     97  William   24   NaN  NaN      197    197 1883-09-25    1 1780-01-30 1967-10-09    206      2   M  203   NaN  NaN
#206      2  rep  167   NaN  NaN   206      8  Democrat  145   NaN  NaN
#AR          117    102       Cravens    3   NaN  NaN        117     64  William   16   NaN  NaN      114    114 1852-05-25    1 1788-08-25 1968-08-21    117      2   M  112   NaN  NaN
#117      2  rep   84   NaN  NaN   115      5  Democrat   94   NaN  NaN
#AS            2      2  Faleomavaega    1   NaN  NaN          2      2     Fofó    1   NaN  NaN        2      2 1937-03-13    1 1937-03-13 1943-08-15      2      1   M    2   NaN  NaN
#  2      1  rep    2   NaN  NaN     2      1  Democrat    2   NaN  NaN
#AZ           48     46        Rhodes    2   NaN  NaN         48     38     John   10   NaN  NaN       48     48 1907-01-29    1 1816-01-24 1976-11-03     48      2   M   45   NaN  NaN
# 48      2  rep   37   NaN  NaN    48      3  Democrat   24   NaN  NaN

n_by_state = df.groupby("state")["last_name"].count()
print(n_by_state)

#state
#AK     16
#AL    206
#AR    117
#AS      2
#AZ     48
#     ...
#VT    115
#WA     95
#WI    196
#WV    120
#WY     40
#Name: last_name, Length: 58, dtype: int64

print(df.groupby(["state", "gender"])["last_name"].count())
#state  gender
#AK     F           0
#       M          16
#AL     F           3
#       M         203
#AR     F           5
#                ...
#WI     M         196
#WV     F           1
#       M         119
#WY     F           2
#       M          38
#Name: last_name, Length: 116, dtype: int64

n_by_state_gender = df.groupby(["state", "gender"])["last_name"].count()
print(type(n_by_state_gender))  #<class 'pandas.core.series.Series'>
print(n_by_state_gender)

#state  gender
#AK     F           0
#       M          16
#AL     F           3
#       M         203
#AR     F           5
#                ...
#WI     M         196
#WV     F           1
#       M         119
#WY     F           2
#       M          38
#Name: last_name, Length: 116, dtype: int64

print(n_by_state_gender.index)
#MultiIndex([('AK', 'F'),
#            ('AK', 'M'),
#            ('AL', 'F'),
#            ('AL', 'M'),
#            ('AR', 'F'),
#            ('AR', 'M'),
#            ('AS', 'F'),
#            ('AS', 'M'),
#            ('AZ', 'F'),
#            ('AZ', 'M'),
#            ...
#            ('VT', 'F'),
#            ('VT', 'M'),
#            ('WA', 'F'),
#            ('WA', 'M'),
#            ('WI', 'F'),
#            ('WI', 'M'),
#            ('WV', 'F'),
#            ('WV', 'M'),
#            ('WY', 'F'),
#            ('WY', 'M')],
#           names=['state', 'gender'], length=116)

#as_index=False ==> convert df.groupby to pandas dataframe
print(df.groupby(["state", "gender"], as_index=False)["last_name"].count())

#           names=['state', 'gender'], length=116)
#    state gender  last_name
#0      AK      F        NaN
#1      AK      M       16.0
#2      AL      F        3.0
#3      AL      M      203.0
#4      AR      F        5.0
#..    ...    ...        ...
#111    WI      M      196.0
#112    WV      F        1.0
#113    WV      M      119.0
#114    WY      F        2.0
#115    WY      M       38.0
#
#[116 rows x 3 columns]
print(type(df.groupby(["state", "gender"], as_index=False)["last_name"].count()))  #<class 'pandas.core.frame.DataFrame'>



#How Pandas GroupBy Works
by_state = df.groupby("state")
print(by_state) #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f75c1adf9b0>


for state, dataframe in by_state:
	print(f"first 2 row of {state} --------")
	print(dataframe.head(2))

#first 2 row of WA --------
#      last_name first_name   birthday gender type state     party
#2979  Lancaster   Columbia 1803-08-26      M  rep    WA  Democrat
#3052   Anderson      James 1822-02-16      M  rep    WA  Democrat
#first 2 row of WI --------
#     last_name first_name   birthday gender type state     party
#2410    Martin     Morgan 1805-03-31      M  rep    WI  Democrat
#2503   Darling      Mason 1801-05-18      M  rep    WI  Democrat
#first 2 row of WV --------
#       last_name first_name   birthday gender type state                   party
#3615       Blair      Jacob 1821-04-11      M  rep    WV  Unconditional Unionist
#3690  Van Winkle      Peter 1808-09-07      M  sen    WV              Republican
#first 2 row of WY --------
#     last_name first_name   birthday gender type state       party
#4009  Nuckolls    Stephen 1825-08-16      M  rep    WY    Democrat
#4138     Jones    William 1842-02-20      M  rep    WY  Republican

#Each value is a sequence of the index locations for the rows belonging to that particular group. In the output above, 4009, 4138, and 4511 are the first indices in df at which the state equals “WY.”
print(by_state.groups["WY"])  #return row index
#Int64Index([ 4009,  4138,  4511,  4572,  4718,  5054,  5533,  5726,  6128,
#             6895,  7620,  7831,  7925,  7988,  8038,  8052,  8280,  8545,
#             8604,  8674,  8801,  8931,  9242,  9394,  9468,  9470,  9685,
#             9722,  9783,  9998, 10098, 10159, 10235, 10449, 10811, 10860,
#            10978, 11464, 11518, 11835],
#           dtype='int64')


print(by_state.get_group("WY"))

#      last_name first_name   birthday gender type state       party
#4009   Nuckolls    Stephen 1825-08-16      M  rep    WY    Democrat
#4138      Jones    William 1842-02-20      M  rep    WY  Republican
#4511     Steele    William 1842-07-24      M  rep    WY    Democrat
#4572    Corlett    William 1842-04-10      M  rep    WY  Republican
#4718     Downey    Stephen 1839-07-25      M  rep    WY  Republican
#...         ...        ...        ...    ...  ...   ...         ...
#10860    Wallop    Malcolm 1933-02-27      M  sen    WY  Republican
#10978   Simpson       Alan 1931-09-02      M  sen    WY  Republican
#11464     Cubin    Barbara 1946-11-30      F  rep    WY  Republican
#11518    Thomas      Craig 1933-02-17      M  sen    WY  Republican
#11835    Lummis    Cynthia 1954-09-10      F  rep    WY  Republican
#
#[40 rows x 7 columns]

print(df.loc[df["state"] == "WY"])  #~ by_state.get_group("WY")

#[40 rows x 7 columns]
#      last_name first_name   birthday gender type state       party
#4009   Nuckolls    Stephen 1825-08-16      M  rep    WY    Democrat
#4138      Jones    William 1842-02-20      M  rep    WY  Republican
#4511     Steele    William 1842-07-24      M  rep    WY    Democrat
#4572    Corlett    William 1842-04-10      M  rep    WY  Republican
#4718     Downey    Stephen 1839-07-25      M  rep    WY  Republican
#...         ...        ...        ...    ...  ...   ...         ...
#10860    Wallop    Malcolm 1933-02-27      M  sen    WY  Republican
#10978   Simpson       Alan 1931-09-02      M  sen    WY  Republican
#11464     Cubin    Barbara 1946-11-30      F  rep    WY  Republican
#11518    Thomas      Craig 1933-02-17      M  sen    WY  Republican
#11835    Lummis    Cynthia 1954-09-10      F  rep    WY  Republican
#
#[40 rows x 7 columns]