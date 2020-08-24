#!/usr/bin/env python3
import pandas as pd
import sys
import matplotlib.pyplot as plt #plt.rcdefaults() 
filepath = 'datasets_316056_639173_amazon.csv'
df = pd.read_csv(filepath, encoding = "ISO-8859-1", thousands = '.')
print(df)
print(df.info())
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 6454 entries, 0 to 6453
#Data columns (total 5 columns):
# #   Column  Non-Null Count  Dtype
#---  ------  --------------  -----
# 0   year    6454 non-null   int64
# 1   state   6454 non-null   object
# 2   month   6454 non-null   object
# 3   number  6454 non-null   float64
# 4   date    6454 non-null   object
#dtypes: float64(1), int64(1), object(3)
#memory usage: 252.2+ KB
month_name = set(list(df['month']))
print(month_name)  #{'Abril', 'Maio', 'Outubro', 'Dezembro', 'Julho', 'Novembro', 'Junho', 'Janeiro', 'Fevereiro', 'Agosto', 'Setembro', 'Março'}

dict_month = {"Janeiro":"January",
"Fevereiro":"February",
"Março":"March",
"Abril":"April",
"Maio":"May",
"Junho":"June",
"Julho":"July",
"Agosto":"August",
"Setembro":"September",
"Outubro":"October",
"Novembro":"November",
"Dezembro":"December"
}
print(dict_month)

#https://stackoverflow.com/questions/34962104/pandas-how-can-i-use-the-apply-function-for-a-single-column
df['month'] = df['month'].map(lambda x: dict_month[x])
print(df)

print(df.describe(include= "all"))

#Check for any missing values:

print(df.isna().sum())

#year      0
#state     0
#month     0
#number    0
#date      0
#dtype: int64


forest_fire_per_month = df.groupby('month')['number'].sum()

print(forest_fire_per_month)


#April          28364
#August        740841
#December      152596
#February       30952
#January        52587
#July          217620
#June          111405
#March          35118
#May            46083
#November      312326
#October       629665
#September    1015925
#Name: number, dtype: int64


print(forest_fire_per_month.index)

#Index(['April', 'August', 'December', 'February', 'January', 'July', 'June',
#       'March', 'May', 'November', 'October', 'September'],
#      dtype='object', name='month')

#convert from Series to DataFrame
print("type of forest_fire_per_month before convert", type(forest_fire_per_month))  ##<class 'pandas.core.series.Series'>
forest_fire_per_month = forest_fire_per_month.to_frame()
print("type of forest_fire_per_month after convert", type(forest_fire_per_month))


#forest_fire_per_month['month'] = forest_fire_per_month.index

print(forest_fire_per_month.info())
#Data columns (total 2 columns):
# #   Column  Non-Null Count  Dtype
#---  ------  --------------  -----
# 0   number  12 non-null     int64
# 1   month   12 non-null     object

print(forest_fire_per_month)
#
#            number      month
#month
#April        28364      April
#August      740841     August
#December    152596   December
#February     30952   February
#January      52587    January
#July        217620       July
#June        111405       June
#March        35118      March
#May          46083        May
#November    312326   November
#October     629665    October
#September  1015925  September




print(forest_fire_per_month.index)
forest_fire_per_month.reset_index(level=0, inplace=True)
print(forest_fire_per_month.index)
print(forest_fire_per_month)

plt.figure(figsize=(25, 15)) 
#plt.bar(x-values, y-values) 

plt.bar(
forest_fire_per_month['month'],
forest_fire_per_month['number'], 
color = (0.5,0.1,0.5,0.6)) 
plt.suptitle('Amazon Forest Fires Over the Months', fontsize=20)

plt.title('Using Data from Years 1998 - 2017', fontsize=20)
plt.xlabel('Month', fontsize=20) 
plt.ylabel('Number of Forest Fires', fontsize=20)

plt.show()