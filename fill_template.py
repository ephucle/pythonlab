#!/usr/bin/env python3
from string import Template
import pandas as pd
d = {
    'gnbname': 'gHA00037',
    'subtitle': 'And this is the subtitle',
    'vlanid_oam':'2639',
    'oam_ipaddress':'10.188.132.145',
    'vlanid_traffic':'2638',
    'traffic_ipaddress':'10.178.132.145',
    'next_hop_oam':'10.188.132.150',
    'next_hop_traffic':'10.178.132.150'
}
#template = "sitebasic.xml"
template_filename = "./BB6502_LTE_template/02_SiteBasic_eSG08949_Viettel.xml"

##FILL DATA
#with open(template, 'r') as f:
#    input_file_content = f.read()
#    src = Template(input_file_content)
#    result = src.substitute(d)
#    
#    print("---------template before fill-----------------------------------------")
#    print(input_file_content)
#    output_filename = template+ ".fill.xml"
#    text_file = open(output_filename, "w")
#    n = text_file.write(result)
#    text_file.close()
#
#with open(output_filename, 'r') as f:
#    print("---------template after fill------------------------------------------------------------------------------------")
#    print(f.read())

#df = pd.read_excel(file_path, header=1, sheet_name='2.BS_DG_DU_Crash(2020-04-01이후)', usecols=["Site Name", "KST Time","KST Dalry", "Crash HW", "UP" , "Crash Details", "TRMapping"])
input_file_path = 'input_cdd.xlsx'
#df = pd.read_excel(input_file_path, header=0, sheet_name='Sheet1')
df2 = pd.read_excel(input_file_path, header=0, sheet_name='Sheet2')
#print(df)
print(df2)
#  Tỉnh    eNBname  eNBId  OSS  ServiceVLAN     ServiceIP ServiceSubnetMask ServiceDefaultGateway  OAMVLAN         OAMIP    OAMSubnetMask OAMDefaultGateway
#0  HCM   eSG08949    NaN  NaN         2636  10.170.66.33   255.255.255.248          10.170.66.38     2637  10.171.66.33  255.255.255.248      10.171.66.38
#1  HCM  eSG08949B    NaN  NaN         2636  10.170.66.41   255.255.255.248          10.170.66.46     2637  10.171.66.41  255.255.255.248      10.171.66.46
###iterate


f = open(template_filename, "r")
input_file_content = f.read()
for index, row in df2.iterrows():
	#rule: moi row se ghi ket qua ra 1 file
	#tam thoi lay tagname la column eNBname
	rowname = row["eNBname"]
	
	print (row["eNBname"], row["ServiceIP"], row["ServiceVLAN"], row["ServiceDefaultGateway"])
	data = {
	'eNBname': row["eNBname"],
	'ServiceIP' : row["ServiceIP"],
	'ServiceVLAN' : row["ServiceVLAN"],
	'ServiceDefaultGateway' : row["ServiceDefaultGateway"],
	'OAMVLAN' : row["OAMVLAN"],
	'OAMIP' : row["OAMIP"],
	'OAMDefaultGateway' : row["OAMDefaultGateway"],
	}
	src = Template(input_file_content)
	result = src.substitute(data)
	
	output_filename = rowname
	output_text_file = open(output_filename, "w")
	output_text_file.write(result)
	output_text_file.close()
f.close()

