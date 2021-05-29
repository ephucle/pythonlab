import re, sys, os
#later we can replace pattern here
saperate_pattern = "\*\*"
import pandas as pd
from string import Template

template_filepath = "./template/5G_relation/4_4_gNB_NRCellRelation"




#find all variable in template
with open(template_filepath) as infile:
	lines = infile.readlines()
	
	#find all variable string
	var_set = set()
	for index, line in enumerate(lines):
		line = line.strip()
		regex = '\$' + "(\w+)"
		variables = re.findall(regex, line)
		print(variables)
		for item in variables:
			var_set.add(item)
		
		#####
		regex2 = '\$\{' + "(\w+)"+'\}'
		variables2 = re.findall(regex2, line)
		print(variables2)
		for item in variables2:
			var_set.add(item)
		#####
	print("----------------all variable string--------------")
	print(var_set)
	

#sys.exit()

#try to lookup variable from excel
df = pd.read_excel("1.CDD_5G mmWave 8CC_HNI_B7_v07.xlsx", header=0, sheet_name="4.4.gNB.NRCellRelation")

column_headers = list(df.columns.values)

#print(df)
#print(column_headers)
#sys.exit()

f = open(template_filepath, "r")
input_file_content = f.read()



#scan each row
for index, row in df.iterrows():
	#rowname = row["nRFrequencyId"]
	#print(rowname)
	data = {}
	for column_name in var_set:
		if column_name in column_headers:
			#print(index,column_name,row[column_name])
			data[column_name] = row[column_name]
	print(data)
	rowname = index #using row index for filename tag
	src = Template(input_file_content)
	result = src.substitute(data)
	home_path = os.path.dirname(os.path.realpath(__file__))
	output_filepath=os.path.join(home_path, "output_script", str(rowname))
	output_text_file = open(output_filepath, "w")
	output_text_file.write(result)
	output_text_file.close()
	print("Successful create script", output_filepath)