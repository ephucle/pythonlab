#!/usr/bin/env python3
#Example 3: News Aggregator Dataset
#https://realpython.com/pandas-groupby/
import pandas as pd
from pathlib import Path
import datetime as dt
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
def parse_millisecond_timestamp(ts: int) -> dt.datetime:
	"""Convert ms since Unix epoch to UTC datetime instance."""
	return dt.datetime.fromtimestamp(ts / 1000, tz=dt.timezone.utc)
#test
print(parse_millisecond_timestamp(1394470370698))  #2014-03-10 16:52:50.698000+00:00
print(parse_millisecond_timestamp(1409229190251))  #2014-08-28 12:33:10.251000+00:00



df = pd.read_csv(
	DATA_FOLDER / "news.csv",
	#dtype=dtypes,
	#usecols=["CO(GT)", "Date", "Time", "T", "RH", "AH"],
	#parse_dates=[["Date", "Time"]],
	#na_values=[-200],
	sep="\t",
	names=["title", "url", "outlet", "category", "cluster", "host", "tstamp"],
	dtype={  # help to save memory, from 25MB to 16MB
			"outlet": "category",
			"category": "category",
			"cluster": "category",
			"host": "category",
	},
	parse_dates=["tstamp"],
	date_parser=parse_millisecond_timestamp
	)
print(df)
print(df.info())

#Data columns (total 7 columns):
# #   Column    Non-Null Count   Dtype
#---  ------    --------------   -----
# 0   title     422419 non-null  object
# 1   url       422419 non-null  object
# 2   outlet    422417 non-null  category
# 3   category  422419 non-null  category
# 4   cluster   422419 non-null  category
# 5   host      422419 non-null  category
# 6   tstamp    422419 non-null  int64
#dtypes: category(4), int64(1), object(2)
#memory usage: 16.9+ MB
#None

print(df['tstamp'])
#1         1394470370698
#2         1394470371207
#3         1394470371550
#4         1394470371793
#5         1394470372027
#              ...
#422933    1409229190251
#422934    1409229190508
#422935    1409229190771
#422936    1409229191071
#422937    1409229191565