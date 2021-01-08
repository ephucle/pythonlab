#!/usr/bin/env python3
#version 1.0, 31Mar2020, Hoang Le P
#version 1.1, 01Apr2020
#add COLOR for DETAIL crash printout
#add LOGO for crash
#add last 5 row, to check last crash date of the log
#get trmapping version from trmapping.txt and print to console
#version 1.2, 03Apr2020
#remove crash = "Extra: terminated by signal 1", very common
#change logo to "crash du"  or "crash ru" according filename
#add 'CXP9024418/12_R55B26' to filter pkg

#version 1.3, 08Apr2020
#auto convert  PKG Name to PKG ID like MTR20.11, so that no need to manual double check by grep cmd, human readable formar

#version = 'Version1.4, 200411_084000'
#update lai de co the import duoc, tai su dung code

#version = 'Version1.5, 200413_120800'
#matching new crash signature to TR ID
#update find_last_crash_day, replace for in range by for in enumerate, save DU crash 5s

#version = 'Version1.6, 200414_152300'
#print color for tr mapping version

#version = 'Version1.7, 200415_143000'
#update find_last_crash_day
#update extract_crash_signature
#fix duoc loi filter crash sign for "Kernel Crash. Rank: Cold. PMD: /var/log/pmd/pmd-ramoops-pmd"
#them function check_if_crash_in_new_sw, cai thien viec filter new sw crash

#version = 'Version1.8, 200416_125700'
#update extract_crash_signature, add input variable, check_sign_flag for finding crash sign, and for create regex case
#Beautiful is better than ugly.
#fix issue dem sai vai site, root cause: "Board restart. Reason: " and "Board restart.Reason: "

#version = 'Version1.8, 200421_111000'
#update bbUeRef= to extract_crash_signature function

#version = 'Version1.9, 200422_100000'
#update filtered crash, to copy and paste to email quickly, professional report
#beautiful terminal printout for easy read result, simplify everything
#update extract_crash_signature function for better extract crash signature

#version = 'Version2.0, 200423_142700'
#update call_new_crash with input = excel crash report  file name, automatically parsing excel file, no need to create DU RU csv file
#example how to run: ./new_crash.py ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200423.xlsx
#Parsing /mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/03-DailyReport/ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx

version = 'Version2.0, 200423_142700'


import pandas
import sys
import re
import os
from datetime import datetime as dt
from prettytable import PrettyTable
import pyprog
from timeit import default_timer as timer
from termcolor import colored
import skt_5g_cd_tool
import parsing_excel_by_pandas
now = dt.now()

def remove_index_from_signature(crash_signature):
	#truong hop dac biet 1 cua EMCA crash CellIndex variable
	if "cellIndex=" in crash_signature:
		f2 = re.split("cellIndex=",crash_signature)
		crash_signature = f2[0]+ "cellIndex="
	
	if "number:" in crash_signature:
		f2 = re.split("number:",crash_signature)
		crash_signature = f2[0]+ "number:"
	
	if "address:" in crash_signature:
		f2 = re.split("address:",crash_signature)
		crash_signature = f2[0]+ "address:"
	
	if "bbUeRef=" in crash_signature:
		f2 = re.split("bbUeRef=",crash_signature)
		crash_signature = f2[0]+ "bbUeRef="
	
	if "assocId=" in crash_signature:
		f2 = re.split("assocId=",crash_signature)
		crash_signature = f2[0]+ "assocId="
	
	if "by port " in crash_signature:
		f2 = re.split("by port ",crash_signature)
		crash_signature = f2[0]+ "by port "
	
	if "linkId = " in crash_signature:
		f2 = re.split("linkId = ",crash_signature)
		crash_signature = f2[0]+ "linkId = "
	
	if "cellid=" in crash_signature:
		f2 = re.split("cellid=",crash_signature)
		crash_signature = f2[0]+ "cellid="
	
	if "sCellIndex: " in crash_signature:
		f2 = re.split("sCellIndex: ",crash_signature)
		crash_signature = f2[0]+ "sCellIndex: "
	
	return crash_signature


def extract_crash_signature(crash, check_sign_flag):

	'''
	check_sign_flag = True: apply for check new crash signature
	check_sign_flag = False: apply for create regex string for searching MHWEB
	'''
	crash_signature = ""
	
	
	
	if re.match('^No:\s+(\d+,)*\d+. ',crash):
		f1= re.split('^No:\s+(\d+,)*\d+. ', crash)
		
		crash = f1[-1]
	
	#No: 5893. Board restart. Reason: Kernel Crash. Rank: Cold. PMD: /var/log/pmd/pmd-ramoops-pmd-49744-20000101-000115.tgz
	#No: 14836. Program restart. Reason: Program Crash. Program: rhd-bpmd. Extra: CXP2030006%7_R26C62
	#pmd crash thi phai ko co EMCA
	
	
	
	#if (re.search("Program restart. Reason: ",crash) or re.search("Board restart. Reason: ",crash)) and not re.search('Emca \d+:DSP \d+: ', crash) and "PMD:" in crash:
	
	pat = '(Program restart. Reason: |Board restart. Reason: |Board restart.Reason: )'
	if re.search(pat ,  crash) and not re.search('Emca \d+:DSP \d+: ', crash) and "PMD:" in crash:
		if "Extra: " not in crash:
			#Board restart.Reason: Kernel Crash. Rank: Cold. PMD: /var/log/pmd/pmd-ramoops-pmd-46149-20200403-132304.tgz
			#Program restart. Reason: Program Crash. Program: rbsNcLm. Signal: SIGABRT. PMD: pmd-cmd_proc-6664-20200402-000027
			if "Program restart. Reason: " in crash:
				f1 = re.split("Program restart. Reason: ",crash)
			if "Board restart. Reason: " in crash:
				f1 = re.split("Board restart. Reason: ",crash)
			if "Board restart.Reason: " in crash:
				f1 = re.split("Board restart.Reason: ",crash)
				
			f2 = re.split("-\d+-\d{8}-\d{6}",f1[1])
			crash_signature = f2[0]
			crash_signature = remove_index_from_signature(crash_signature)
		
		elif "Extra: " in crash and re.search(r'Extra: CXP\S+_\w+',crash) and not re.search(r'-\d+-\d{8}-\d{6}',crash) and "PMD:" not in crash:
			
			crash_signature = crash
			crash_signature = remove_index_from_signature(crash_signature)
		
		elif "Extra: " in crash and re.search(r'Extra: CXP\S+_\w+',crash) and re.search(r'-\d+-\d{8}-\d{6}',crash) and "PMD:" in crash:
			if "Program restart. Reason: " in crash:
				f1 = re.split("Program restart. Reason: ",crash)
			if "Board restart. Reason: " in crash:
				f1 = re.split("Board restart. Reason: ",crash)
			if "Board restart.Reason: " in crash:
				f1 = re.split("Board restart.Reason: ",crash)
			
			f2 = re.split("-\d+-\d{8}-\d{6}",f1[1])
			crash_signature = f2[0]
			crash_signature = remove_index_from_signature(crash_signature)
		else:
			
			f1 = re.split("Extra: ",crash)
			crash_signature = "Extra: "+ f1[1]
			crash_signature = remove_index_from_signature(crash_signature)
		
			
		
	#filter EMCA crash		
	filter2 = "Emca \d+:DSP \d+: "
	#neu chuoi crash chua "Emca \d+:DSP \d+: ", thi:
	
	if re.search(filter2, crash):
		f1 = re.split(filter2,crash)
		crash_signature = f1[1]
		#remove index for EMCA crash
		crash_signature = remove_index_from_signature(crash_signature)

	
	
	#Cai tien ham nay, de co the reuse o cho khac
	if check_sign_flag == False:
		if crash_signature == "":
			#cac crash ma ko co pmd, nhung co board restart thi ko can quan tam
			#if "Board restart" in crash and 'pmd' not in crash:
			
			pat = '(Program restart. Reason: |Board restart. Reason: |Board restart.Reason: )'
			if re.search( pat , crash) and 'pmd' not in crash:
				return ""
			else:
				return crash
		else:
			return crash_signature
	else: 
		return crash_signature


def removeduplicatedandcount(gnb):
	'''
	input : list
	return: list of tube, ex: [('HY10307', 1), ('HY12920', 1), ('HX95174', 1), ('HX97383', 1), ('HY11574', 1)]
	'''
	#gnb = ['HX85427', 'HY13193', 'HX95786', 'HX95255', 'HX97721', 'New Crash', 'New Crash', 'New Crash', 'HX95786', 'HX95786', 'New Crash', 'HX95786', 'HX85427', 'HY13193', 'HX95786', 'New Crash', 'HX95786', 'New Crash', 'HX95786', 'New Crash', 'New Crash', 'New Crash', 'HY12920', 'HX97721', 'HX95786', 'New Crash', 'New Crash', 'New Crash', 'HX95786', 'HX95786']
	x ={}
	gnbuniq = list(set(gnb))
	#reset
	for item in gnbuniq:
		x[item]=0
	#bat dau dem
	for i in  x:
		for tr in gnb:
			if i == tr:
				x[i]+=1
	
	y = sorted(x.items(), key=lambda x: x[1], reverse=True)
	#y = [('New Crash', 38), ('HX95786', 34), ('HX96268', 12), ('HX82707', 9), ('HX85427', 6), ('HX97721', 5), ('HY17824', 4), ('HY13193', 3), ('HX95255', 2), ('HX96299', 2), ('HX82729', 2), ('HY10892', 1), ('HY19547', 1), ('HX99090', 1), ('HY10307', 1), ('HY12920', 1), ('HX95174', 1), ('HX97383', 1), ('HY11574', 1)]

	return y

def get_tr_mapping_dict():
	'''
	#parse trmapping.txt and get trmapping dict
	'''
	tr_dict = {}
	lines = [line.rstrip() for line in open("./trmapping.txt")]
	for line in lines:	
		#note for regular expression
		#(.*?): match any string
		#\s+: match one or more continuous space for tab
		#(\w\w\d\d\d\d\d): match an TR ID (HX12345/HW45678/HY12345)
		#m = re.match(r"(.*?)	(\w\w\d\d\d\d\d)", line)
		m = re.match(r"(.*?)\s+(\w\w\d\d\d\d\d)", line)
		
		#rat quan trong, neu ko se fail
		if m:
			crashsignature = m.group(1)
			tr = m.group(2)
			tr_dict[crashsignature] = tr
		
		#check version of tool
		#Version9.8.92
		m1 = re.match(r"Version(\S+)", line)
		if m1:
			trmappingversion = m1.group(1)
	return [tr_dict,trmappingversion]



def get_sw_mapping_dict():
	'''
	#parse trmapping.txt and get trmapping dict
	'''
	
	sw_dict = {}
	lines = [line.rstrip() for line in open("./swmapping.txt")]
	for line in lines:	
		
		#88	CXP9024418/12_R50B37	MTR19.41_AD1	gNB_NR(Mergit)	
		#89	CXP9024418/12_R51B20	MTR19.43	gNB_NR(Mergit)	
		#print (line)
		m = re.match(r'\d+\s+(\S+)\s+(\S+)\s+\S+', line)
		
		
		#rat quan trong, neu ko se fail
		if m:
			#print (line)
			pkg_rev = m.group(1)
			pkg_id = m.group(2)
			sw_dict[pkg_rev] = pkg_id

	return sw_dict


def check_new_crash(crash):
	result = True
	tr_dict = get_tr_mapping_dict()[0]
	list_known_sig = tr_dict.keys()
	for sig in list_known_sig:
		if sig in crash:
		#if crash.endswith(sig):
			return False
			break
	return result
			



def find_last_crash_day(signature1, crash_details1, crash_daytimes,sites_list,tr_mappings1):
	'''
	return (last_crash_day, last_crash_node)
	
	'''
	last_crash_date = dt.strptime("1/1/1970",'%m/%d/%Y')
	last_crash_node = ""
	
	for i, crash in enumerate(crash_details1):
		crash_day = crash_daytimes[i]
		
		crash_day = str(crash_day)
		#print (crash_day)
		try:
			crash_day_obj = dt.strptime(crash_day,'%Y/%m/%d %H:%M:%S')
			
		except:
			crash_day_obj = dt.strptime(crash_day,'%Y-%m-%d %H:%M:%S')
		
		
		

		
		if tr_mappings1[i] == "New Crash" and signature1 in crash:
			if last_crash_date < crash_day_obj:
				last_crash_date = crash_day_obj
				last_crash_node = sites_list[i]
	return (last_crash_date, last_crash_node)
	
def find_newest_pkg(sw_set):
	result = []
	sw6 = []
	for item in sw_set:
		if "/6" in item and "gNB" not in item:
			sw6.append(item)
	sw6 = sorted(sw6)
	
	sw12 = []
	for item in sw_set:
		if "/12" in item:
			sw12.append(item)
	sw12 = sorted(sw12)
	
	sw5 = []
	for item in sw_set:
		if "/5" in item:
			sw5.append(item)
	sw5 = sorted(sw5)
	
	sw4t = []
	for item in sw_set:
		if "gNB" in item:
			sw4t.append(item)
	sw4t = sorted(sw4t)
	
	if len(sw5) > 0: result.append(sw5[-1])
	if len(sw6) > 0: result.append(sw6[-1])
	if len(sw12) > 0: result.append(sw12[-1])
	if len(sw4t) > 0: result.append(sw4t[-1])
	
	return set(result)


def print_logo(filename):
	if "du" in filename:
		print("                     _           _       ")
		print("                    | |         | |      ")
		print("   ___ _ __ __ _ ___| |__     __| |_   _ ")
		print("  / __| '__/ _` / __| '_ \   / _` | | | |")
		print(" | (__| | | (_| \__ \ | | | | (_| | |_| |")
		print("  \___|_|  \__,_|___/_| |_|  \__,_|\__,_|")

	elif "ru" in filename:
		print("                     _                  ")
		print("                    | |                 ")
		print("   ___ _ __ __ _ ___| |__    _ __ _   _ ")
		print("  / __| '__/ _` / __| '_ \  | '__| | | |")
		print(" | (__| | | (_| \__ \ | | | | |  | |_| |")
		print("  \___|_|  \__,_|___/_| |_| |_|   \__,_|")
	else:
		print ("")


def lookup_pkg_id(pkg, sw_dict):
	if pkg in sw_dict.keys():
		return sw_dict[pkg]
	else :
		return pkg
	
def check_if_crash_in_new_sw(last_sw_list1, sw_filter_list1):
	'''
	return True if new SW
	return False if old SW
	'''
	result = False
	for item in last_sw_list1:
		if item in sw_filter_list1:
			result = True
			break
	
	return result
	
	
	
#def main():
def new_crash_check(pandas_dataset):
	'''
	crash_type = 'du' or 'ru'
	'''
	
	#filename = 'ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx'
	print ("-"*40)
	print (version)
	#print_logo(filename)
	
	#parse trmapping.txt and get trmapping dict
	tr_dict = get_tr_mapping_dict()[0]
	tr_mapping_version = get_tr_mapping_dict()[1]
	
	#in version mau do cho de nhin, bien nay thay doi hang ngay, can remark cho ro
	print("TR Mapping Version: ", colored(tr_mapping_version,'red'))
	
	list_known_sig = tr_dict.keys()
	
	sw_filter_list = set([
	 'CXP9024418/12_R55B26', 'CXP9024418/12_R57C74', 'CXP9024418/12_R60B28' , 'CXP9024418/12_R62B21', 'CXP9024418/12_R62B41' ,'CXP9024418/12_R62B45' ,
	 'CXP9024418/6_R80F30' , 'CXP9024418/6_R80F51',
	 'CXP9024418/6_R85C59(gNB)' , 'CXP9024418/6_R85C103(gNB)' , 'CXP9024418/15_R4B28' , 'CXP9024418/15_R5B21'
	])
	 
	#parsing swmapping.txt to get sw_dict
	sw_dict = get_sw_mapping_dict()
	#print (sw_dict)
	
	
	
	#will remove later
	#dataset = pandas.read_csv(filename,encoding = "ISO-8859-1",low_memory=False)
	dataset = pandas_dataset
	
	#data = pandas.read_csv(myfile, encoding='utf-8', quotechar='"', delimiter=',') 
	
	
	print("Data dimention:", dataset.shape)
	
	
	
	print("First 5 row and Last 5 ROW:")
	print(dataset)
	

	#parsing csv sheet
	crash_details = dataset['Crash Details']
	
	#because header of DU sheet and RU sheet if different, so that have to use this if to check
	if "TRMapping" in dataset.columns:
		tr_mappings = dataset['TRMapping']
	if "TR Mapping" in dataset.columns:
		tr_mappings = dataset['TR Mapping']
		
	upgrade_pkg = dataset['UP']
	sites_list = dataset['Site Name']
	if 'Date Time(KST)' in dataset.columns
		crash_daytimes = dataset['Date Time(KST)']
	else 
		crash_daytimes = dataset['KST Time']

	len1 = len(crash_details)
	
	#chi tap trung xu ly new crash
	crash_detail = ""
	signatures = []
	
	count_new = 0
	for i in range(len1):
		crash_detail = crash_details[i]
		#dung check_new_crash(crash_details[i]) de check crash theo file trmapping.txt
		if  "New Crash" in tr_mappings[i] and check_new_crash(crash_detail):
			count_new += 1
				
			##check lai thang ong noi nay
			#signature = extract_crash_signature(crash_detail)
			signature = extract_crash_signature(crash_detail, True)
			signatures.append(signature)

	dict_signatures = removeduplicatedandcount(signatures)
	
	#20 la toi uu, can tim cac ket qua thap hon 10 nua
	max_sign_check = 20
	
	#chi xu ly top 30 new crash
	print ('*'*20)
	#print ("TOP 30 CRASH:")	
	j = 0
	
	#https://stackoverflow.com/questions/10865483/print-results-in-mysql-format-with-python
	x = PrettyTable(["No.", "Crash signature", "Count","Site", "Latest Crash PKG" , "Last crash time", "Last Crash Node" ])	
	x.align["Crash signature"] = "l"
	x.align["Latest Crash PKG"] = "l"
	x.align["SW"] = "l"
	
	#filtered table
	x2 = PrettyTable(["No.", "Crash signature", "Crash", "Site","Latest Crash PKG" , "Last crash time KST", "Last Crash Node", "Match TR" ])		
	x2.align["Crash signature"] = "l"
	x2.align["Latest Crash PKG"] = "l"
	x2.align["SW"] = "l"
	
	#filtered table, 2
	x3 = PrettyTable(["No.", "Crash signature", "Crash", "Site","Latest Crash PKG" , "Last crash time KST", "Last Crash Node", "Match TR" ])		
	x3.align["Crash signature"] = "l"
	x3.align["Latest Crash PKG"] = "l"
	x3.align["SW"] = "l"
	
	filtered_crashs = []
	# Create Object
	prog = pyprog.ProgressBar(" ", "", max_sign_check)
	#print ("Parsing data ...[No of Site/Crash, SW PKG, Matching TR...]")
	
	#start to count time
	start = timer()

	parsing_result_list = []
	print ("Total signature found:", len(dict_signatures) )
	print ("Parsing data ...[No of Site/Crash, SW PKG, Matching TR...]")
	prog.update()
	
	
	for i in range(max_sign_check):
		
		sign = dict_signatures[i][0]
		count_sign = dict_signatures[i][1]
		sw_list = set()
		temp_site_list = []
		last_crash_node_day = find_last_crash_day(sign, crash_details, crash_daytimes, sites_list,tr_mappings)
		last_crash_day = last_crash_node_day[0]
		last_crash_node = last_crash_node_day[1]
		delta_day = now - last_crash_day
		delta_day = delta_day.days
		
		#find sw list of sign
		for i1 in range(len1):
			if sign in crash_details[i1]:
				if upgrade_pkg[i1] not in sw_list and "New Crash" in tr_mappings[i1] and check_new_crash(crash_details[i1]) and not isinstance(upgrade_pkg[i1], float) :
					sw_list.add(upgrade_pkg[i1])
				if(sites_list[i1] not in temp_site_list) and "New Crash" in tr_mappings[i1]:
					temp_site_list.append(sites_list[i1])
		
		count_sites = len(temp_site_list)
		
		
		#tim tap hop sw moi mat
		last_sw_list = find_newest_pkg(sw_list)
		
		#chuyen doi package string to COMMON PKG ID like MTR20.05
		last_sw_list_ID = []
		for item in last_sw_list:
			last_sw_list_ID.append(lookup_pkg_id(item,sw_dict))
		
		
		if sign != "" and sign != "Extra: terminated by signal 1":
			parsing_result_list.append((i, sign, count_sign,count_sites, sw_list, last_crash_day, last_crash_node))
			
			x.add_row([i, sign[:40], count_sign, count_sites , last_sw_list_ID,last_crash_day,last_crash_node])
			
			# Set current status
			prog.set_stat(i + 1)
			# Update Progress Bar
			prog.update()

			
		#filter crash
		
		if sign != "" and sign != "Extra: terminated by signal 1" and  'CMC supervision.nIllegal access by port' not in sign and count_sign >= 10 and count_sites >= 2 and delta_day <= 3  and check_if_crash_in_new_sw(last_sw_list, sw_filter_list):
			
			#find matching TR ID
			print ("\n>>> Matching TR ID for new crash signature:", colored(sign, 'red'))
			#chay cham qua, tam thoi turn off
			match_tr = skt_5g_cd_tool.search_mhweb_offline(sign)
			#de print cho dep, khong phai print set()
			if len(match_tr) == 0 : match_tr = ""
			
			##test filter crash with pandas
			#last_crash_time_kst_pd, last_crash_node_pd, last_crash_detail_pd, last_crash_pkg_pd = parsing_excel_by_pandas.filter_last_crash(sign,pandas_dataset)
			#x3.add_row([i, sign[:30],count_sign,count_sites, last_crash_pkg_pd,last_crash_time_kst_pd,last_crash_node_pd, match_tr])
			
			#dung PKG ID trong filter table, cho no ngan gon
			x2.add_row([i, sign[:30],count_sign,count_sites, last_sw_list_ID,last_crash_day,last_crash_node, match_tr])
			
			#doi voi detail crash, thi chi can sign full, sw full, con lai ko can, cho don gian
			filtered_crashs.append([i, sign, "No. Crash: "+str(count_sign), "No. Site: "+str(count_sites), last_sw_list])
	
	print ("\n")
	print ("TOP 30 CRASH:")
	for item in parsing_result_list:
		#(i, sign, count_sign,count_sites, sw_list, last_crash_day, last_crash_node)
		
		#color print
		print (item[0],"|", colored(item[1], 'green'),"|", item[2],"|", colored(item[3], 'red'), "|",  colored(item[4], 'cyan'), "|", colored(item[5], 'yellow'), "|", item[6])
		#colored(item[1], 'cyan')
	
	print ("SUMMARY TABLE:")
	print(x)

	
	print ("FILTER CRITERIA:")
	print ('1.', "CRASH COUNT >= 10, COUNT SITE >= 2, LAST CRASH DAY <= 3 DAYS AGO")
	print('2.', 'Filter PKG')
	
	
	for pkg in sw_filter_list:
		pkg_id = lookup_pkg_id(pkg,sw_dict)
		print(f'{pkg:<25}  {pkg_id:<20}  ')
	
	print("\n\n")
	print('*'*15, "FILTERD CRASH", '*'*15)
	
	#print ("Now: ", now)
	
	print(x2)
	
	print ("\n>>> Detail of crash signature:\n")
	for item in filtered_crashs:
		print (item)
		
	end = timer()
	print("\n>>> Duration ", end - start)
	
	
	
def main():
	#print ("TU DONG HOA CHO INPUT DU & RU")
	#dataset = pandas.read_csv(filename)
	
	#filename: excel crash report file name in folder /mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/03-DailyReport/
	#filename: only file name need, no need full path
	filename = sys.argv[1]
	
	du_dataset,ru_dataset = parsing_excel_by_pandas.parsing_excel_file('ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx')
	du_dataset,ru_dataset = parsing_excel_by_pandas.parsing_excel_file(filename)
	
	print (">>> Parsing DU crash")
	new_crash_check(du_dataset)
	print (">>> Parsing RU crash")
	new_crash_check(ru_dataset)
	#print ("END TU DONG HOA CHO INPUT DU & RU")
	

if __name__ == '__main__':
	main()
