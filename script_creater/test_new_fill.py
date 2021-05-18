import re
#later we can replace pattern here
saperate_pattern = "\*\*"
import pandas as pd


with open("./template/relation/4.2.gNB.NRFrequency") as infile:
	lines = infile.readlines()
	
	#find all variable string
	var_set = set()
	for index, line in enumerate(lines):
		line = line.strip()
		#print (index, line)
		
		#regex = '\*\*(\S+)\*\*'
		regex = saperate_pattern + "(\S+)" + saperate_pattern
		
		
		m = re.search(regex, line)
		if m:
			variable_string = m.group(1)
			print(variable_string)
			var_set.add(variable_string)
	print("all variable string---")
	print(var_set)  #{'smtcOffset', 'smtcPeriodicity', 'smtcDuration', 'smtcScs', 'arfcnValueNRDl', 'nRFrequencyId'}



#try to lookup variable from excel
df = pd.read_excel("1.CDD_5G mmWave 8CC_HNI_B7_v07.xlsx", header=0, sheet_name="4.2.gNB.NRFrequency")
column_headers = list(df.columns.values)


for index, row in df.iterrows():
	#rowname = row["nRFrequencyId"]
	#print(rowname)
	for column_name in var_set:
		if column_name in column_headers:
			print(index,column_name,row[column_name])