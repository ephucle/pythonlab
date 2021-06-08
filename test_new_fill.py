#!/usr/bin/env python3
##https://www.python.org/dev/peps/pep-0292/
##A Simpler Proposal
##We propose the addition of a new class, called Template, which will live in the string module. The Template class supports new rules for string substitution; its value contains placeholders, introduced with the $ character. The following rules for $-placeholders apply:
##
##$$ is an escape; it is replaced with a single $
##$identifier names a substitution placeholder matching a mapping key of "identifier". By default, "identifier" must spell a Python identifier as defined in [2]. The first non-identifier character after the $ character terminates this placeholder specification.
##${identifier} is equivalent to $identifier. It is required when valid identifier characters follow the placeholder but are not part of the placeholder, e.g. "${noun}ification".

#https://docs.python.org/3/library/string.html
#delimiter – This is the literal string describing a placeholder introducing delimiter. The default value is $. Note that this should not be a regular expression, as the implementation will call re.escape() on this string as needed. Note further that you cannot change the delimiter after class creation (i.e. a different delimiter must be set in the subclass’s class namespace).

#idpattern – This is the regular expression describing the pattern for non-braced placeholders. The default value is the regular expression (?a:[_a-z][_a-z0-9]*). If this is given and braceidpattern is None this pattern will also apply to braced placeholders

import re, sys, os
#later we can replace pattern here
saperate_pattern = "\*\*"
import pandas as pd
from string import Template

#template_filepath = "./template/5G_relation/4_4_gNB_NRCellRelation"
template_filepath = "./template/4G_FDD/Template Files/SiteBasic.xml"


with open(template_filepath) as infile:
	input_file_content = infile.read()
	#print(template_content)


#find all variable in template
with open(template_filepath) as infile:
	lines = infile.readlines()
	
	#find all variable string
	var_set = set()
	for index, line in enumerate(lines):
		line = line.strip()
		regex = '\$' + "(\w+)"
		variables = re.findall(regex, line)
		#print(variables)
		for item in variables:
			var_set.add(item)
		
		#####
		regex2 = '\$\{' + "(\w+)"+'\}'
		variables2 = re.findall(regex2, line)
		#print(variables2)
		for item in variables2:
			var_set.add(item)
		#####
		
		#####
		#regex3 = '%' + "(\w+)"+'%'
		#cai tien co dau : ben trong variable
		regex3 = '%' + "([\w:]+)"+'%'
		
		variables3 = re.findall(regex3, line)
		#print(variables3)
		for item in variables3:
			var_set.add(item)
		#####
		
	print("----------------all variable string--------------")
	print(var_set)
	

#regex = '%' + "(\w+)"+'%'
regex = '%' + "([\w:]+)"+'%'  #update to support : inside variablename
variables_percent = re.findall(regex, input_file_content)
print(variables_percent)

for var in variables_percent:
	print (var)
	new_var = var.replace(":","_")  #phai thay ":" bang "_" vi substitudte ko duoc
	#new_s = re.sub('%'+var+'%','${'+var+'}',input_file_content)
	new_s = re.sub('%'+var+'%','${'+new_var+'}',input_file_content)
	input_file_content = new_s


#print(input_file_content)
with open('./output_script/temp_template.xml','w') as outfile:
	outfile.write(input_file_content)
#sys.exit()

#try to lookup variable from excel
#df = pd.read_excel("1.CDD_5G mmWave 8CC_HNI_B7_v07.xlsx", header=0, sheet_name="4.4.gNB.NRCellRelation")
df = pd.read_excel("./template/4G_FDD/CIQ-template.xlsx", header=0, sheet_name="CIQ-template")


column_headers = list(df.columns.values)


print(column_headers)
print("------------------------------------------------------")
i = df[((df.Parameter == 'Area'))].index
df= df.drop(i)
print(df)
#thay doi ":" bang dau ":"
df.columns = df.columns.str.replace(r"[:]", "_")

print(df)

print(df.columns)
#sys.exit()



#scan each row
for index, row in df.iterrows():
	data = {}
	for column_name in var_set:
		if column_name in column_headers:
			column_name = column_name.replace(":","_")
			data[column_name] = row[column_name]
	print(data)
	filename = str(index)+".xml" #using row index for filename tag
	src = Template(input_file_content)
	
	result = src.substitute(data)
	home_path = os.path.dirname(os.path.realpath(__file__))
	output_filepath=os.path.join(home_path, "output_script", filename)
	output_text_file = open(output_filepath, "w")
	output_text_file.write(result)
	output_text_file.close()
	print("Successful create script", output_filepath)