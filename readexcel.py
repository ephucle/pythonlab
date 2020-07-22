#!/usr/bin/python3
import pandas
import time
from tqdm import tqdm

#bo qua hang dau tien, vi dung hang dau tien de dem
print ("Reading exel file ENDC_DU_Crash_Alarm_PKG_Daily_Report_200108.xlsx ...")
df = pandas.read_excel('ENDC_DU_Crash_Alarm_PKG_Daily_Report_200108.xlsx', sheet_name='2.BS_DG_Total_Crash', skiprows=1)
print(df)

print("Column name of the sheet 2.BS_DG_Total_Crash")
print(df.columns.ravel())
print("Size of sheet 2.BS_DG_Total_Crash")
print(df.shape)

print ("pivot table for TRMapping")
df.groupby('TRMapping').size()

#with tqdm(total=100, desc="Adding Users", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
#    for i in range(100):
#        time.sleep(3)
#        pbar.update(1)