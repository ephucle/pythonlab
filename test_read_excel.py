import pandas as pd


xl = pd.ExcelFile("ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200316.xlsx")
print (xl.sheet_names)

df = xl.parse("2.BS_DG_DU_Total_Crash")
df.head()
print("Data dimention:", df.shape)

df1 = xl.parse("2.BS_DG_RU_Crash(2020-01-01)")
df1.head()

print("Data dimention:", df1.shape)