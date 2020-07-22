#!/usr/bin/env python3

#version1.0_20200406_191100
#init version
#version1.1_20200407_102100
#add function read_mhweb_text by like linux less command, and go to line number
#add some hint for search_signature function, help us saving time when brainstorm for search string
#combine file nr and file enb, simplify to reading process

#version1.2_20200408_165100
#add gotoline menu, giup doc file mhweb offline tien loi hon, nhanh hon.
#strip search string in sw and signature, because copy and paste, easy to get additional space character
#fix nho cac path de tool chay duoc tren ca WSL va CYGWIN

#version1.3_20200410_130800
#add get tr content function, to check the TR content, tra cuu offline mot TR

#version = "version1.4_20200411_100300"
#add create_python_regex_string, dung de cat got string, sau do dua vao trong python regex de search
#modify search_mhweb_offline using create_python_regex_string
#update trang thai trong qua trinh search, vi big file, cho lau met lam

#version = "version1.5_20200412_160100"
#update search_mhweb_offline, input crash_string , output set of TR ID
#cai tien thuat toan tim kiem bang cach thay re.search bang re.match, boc tach content moi lan 200 line thay vi 1 line
#update thanh trang thai vao terminal trong qua trinh search. rat chuyen nghiep
#replace all re.search by re.match to speed up big file handle
#in mau do cho ket qua tim kiem trong search_mhweb_offline, de cho de nhin

#version = "version1.6_20200413_090700"
#update search_mhweb_offline function so that it can be reused in new_crash

#version = "version1.7_20200414_152800"
#fix mot so loi lien quan re.match va re.search , da thay lai re.search
#add logo for search offline mhweb

#version = "version1.8_20200422_09400"
#check date of mhweb data, remind update if old than 10 day
#add main logo. beautiful than ugly

#version = "version1.9_20200423_163100"
#update call_new_crash with input = excel crash report  file name, automatically parsing excel file, no need to create DU RU csv file
#auto use default filename for "check new crash" due to it require user input many time

from simple_term_menu import TerminalMenu
import time, os, sys , re,  subprocess, platform
from timeit import default_timer as timer
from datetime import datetime as dt
from datetime import date
import read_big_file
import new_crash
import pyprog
from termcolor import colored
import parsing_excel_by_pandas

version = "version1.9_20200423_163100"
#current_system = platform.system()




#MHWEB file paths
paths = ["/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/2020-04-21.nr.xml" , "/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/2020-04-21.enb.xml", "/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/2020-04-21.4Tbranch15.xml"]
	
mhwebfilepath = '/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt'



#merge two file nr and enb to one file, and then start search

#print ("Start merging two bigfile, nr file and enb file, please wait")
#mhwebfilepath = read_big_file.merge_two_file(paths)

#to save time




def main():
	print_main_logo()
	print (colored(version, 'red'))
	
	now = dt.now()
	print ("Now: ", now)
	
	mhweb_date = re.split('03-MHWEB/',paths[0]) # => mhweb_date[1] = 2020-04-21.nr.xml
	mhweb_date = re.split('.nr',mhweb_date[1])  # =>  mhweb_date [0] = 2020-04-21
	mhweb_date = mhweb_date[0]
	print ('MHWEB offline day:',  mhweb_date) # '2020-04-21'
	mhweb_date_obj = dt.strptime(mhweb_date,'%Y-%m-%d')
	
	today = dt.now()
	delta = today - mhweb_date_obj
	 
	if delta.days > 10:
		print ("Offline MHWEB data is old than 10 day, please download new data")
	else :
		print(' >>> Offline MHWEB data is up to date', delta.days, 'days (< 10 day)')
	
	
	#show calendar, de biet hom nay la ngay thu may trong tuan
	#lam viec cung can biet ngay thang
	#print (subprocess.getoutput('cal') )

	
	#save time, turn on later
	#tinh total line o day, de tiet kiem thoi gian
	#thefile = open(mhwebfilepath, encoding = "ISO-8859-1")
	#for i, line in enumerate(thefile):
	#	pass
	#print (">>> Total lines:",i + 1)
	#global total_line
	#total_line = i+1
	#thefile.close()
	global total_line
	total_line = 33572723
	

	main_menu_exit = False
	terminal_style = ("bg_yellow", "fg_red")
	terminal_entry = ["1.seach_crash_signature", "2.searh_sw", "3.check_new_crash", "4.search_mhweb_offline", "5.read_mhweb_text" ,"6.go_to_line", "7.get_tr_content", "8.exit"]
	
	#terminal_menu = TerminalMenu(menu_entries = ["1.seach_signature", "2.searh_sw", "3.check_new_crash", "4.search_mhweb_offline", "5.read_mhweb_text" ,"6.go_to_line", "7.exit"], menu_highlight_style=terminal_style)
	
	terminal_menu = TerminalMenu(menu_entries = terminal_entry, menu_highlight_style=terminal_style)
	
	while not main_menu_exit:
		
		terminal_sel = terminal_menu.show()
		if terminal_sel == 0:
			#print("option 1 selected, search sign")
			search_signature()
			#time.sleep(2)
		
		if terminal_sel == 1:
			#print("option 2 selected, search sw")
			search_sw()
			#time.sleep(2)
			
		if terminal_sel == 2:
			#print("option 3 selected, check new crash")
			#print("start check new crash...    ")
			call_new_crash()
			
			#time.sleep(2)
		if terminal_sel == 3:
			
			#print("start check new crash...")
			os.system('clear')
			#tool hay , nen in cai LOGO, ZEN: Beautiful is better than ugly.
			#print("Search MHWEB offline")
			
			print_logo_seach_offline()
			print ("-"*30)
			print ("HINT:")
			print ("INPUT: CRASH SIGNATUTE/CRASH LOG ===> OUTPUT: Match TR ID")
			print('Trying to free a cm ptr that points o rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1114       HY32659 ,Not_in_data')
			print('Extra: UeRef has not been allocated ue/variant/access/handler/context/src/ue_context_handler_impl.cc:201    HY33548 , Not_in_data')
			print('"bbiItc_distrib_16bSigMap.c:72: OSE-signal 0xffff0819 (-63463) cannot be mapped to LPP-signal"      HY34122, Not_in_data')
			print('<!UPCDL.2663!> dlmacce_process_dlsu_thread.c:1235: DBC: dlsr.id     HY34532')
			print('"<!BBMC.542!> bbueme_releaseue_ovl.c:231: DBC: nrOfBearersForUe == req.nrOfRelRadioBearersn"        HY36767')
			print('"<!UPCUL.2045!> ulmacce_catmscheduler.c:1776: DBC: fifoCnt == 1n"   HY36762')
			print('"<!UPCUL.2047!> ulmacce_msg3coord_sched_msg2_cfm_thread.c:297: DBC: successn"  HY36676')
			print ("-"*30)
			search_string = input(">>> Please input [Crash signature/lgg log]: ")
			print ("Input:", search_string)
			#search_string = create_python_regex_string(search_string)
			#print ("Regex:", search_string)
			print ("-"*30)
			
			search_mhweb_offline(search_string)
		
		if terminal_sel == 4:
			
			
			#nr_file_path is define in main procedure
			#mhwebfilepath is merged file of nr and enb MHWEB file
			read_big_file.less_file(mhwebfilepath)
		
		
		if terminal_sel == 5:
			os.system('clear')
			go_to_line()
		
		if terminal_sel == 6:
			os.system('clear')
			get_tr_content()
			
			while(1):
				text = input("Intput TR_ID to get TR content, example: HY29682 or HY13649 | sSqQ: exit ===>:")
				text = text.strip()
				print("Input =",text)
				
				#m = re.search(r'[a-zA-Z]{2}[0-9]{5}', text)
				m = re.match(r'[a-zA-Z]{2}[0-9]{5}', text)
				
				if m:
					#read_big_file.pick_first_tr(text, mhwebfilepath)
					#read_big_file.pick_first_tr('HY29889', mhwebfilepath)
					#print("Correct TR ID")
					print("Reading file", mhwebfilepath,"...")
					read_big_file.pick_first_tr(text, mhwebfilepath)
					
				else:
					print ("Wrong TR ID, input again, :>>>")
				if re.search('^[sSqQ]$', text):
					break
				
			
		if terminal_sel == 7:
			print("option 4 selected, exit")
			main_menu_exit = True
			#time.sleep(1)
			
			#xoa toan bo man hinh
			os.system('clear')


def print_logo_seach_offline():

	print ("""
	                          _              __  __ _ _            
	                         | |            / _|/ _| (_)           
	  ___  ___  __ _ _ __ ___| |__     ___ | |_| |_| |_ _ __   ___ 
	 / __|/ _ \/ _` | '__/ __| '_ \\   / _ \|  _|  _| | | '_ \\ / _ \\
	 \__ \\  __/ (_| | | | (__| | | | | (_) | | | | | | | | | |  __/
	 |___/\\___|\\__,_|_|  \\___|_| |_|  \\___/|_| |_| |_|_|_| |_|\\___|
	""")


def print_main_logo():

	print("""
   _____  ____    _____  ____  ____  _    
  /__ __\/  __\  /__ __\/  _ \/  _ \/ \   
    / \  |  \/|    / \  | / \|| / \|| |   
    | |  |    /    | |  | \\_/|| \\_/|| |_/\\
    \_/  \_/\_\    \_/  \____/\____/\____/

    """)
def search_signature():
	result_found = 0
	result_id = 0
	os.system('clear')
	
	print("Search signature, Search TR ID for signature")
	print("HINT, example:")
	print("IGNORECASE")
	print ('. :  show all')
	print ('cc:1114: filter crash with source code posision on line 1114')
	print ('HY\d+: filter HY***** TR crash string')
	print ('HX\d+: filter HX***** TR crash string')
	
	signature = input(">>> Please input signature or TR ID: ")
	
	#bo cac ky tu space o cuoi di, vi copy va paste rat de du ky tu space
	signature = signature.strip()
	
	start = timer()
	lines = [line.rstrip() for line in open("./trmapping.txt")]
	for line in lines:
		m = re.search(signature, line, re.IGNORECASE)
		
		#co truong hop m.match khong co ket qua
		#m = re.match(signature, line, re.IGNORECASE)
		if m:
			#nhom matching
			#print (m.group())
			#ca dong matching
			result_id += 1
			result_found +=1
			print (result_id, line)
			
	print (">>> Number of result found: ", result_found)
	end = timer()
	duration = end - start
	print (">>> Duration",duration)

def search_sw():
	result_found = 0
	os.system('clear')
	
	print("Search sw")
	print ("HINT:")
	print ('. : DOT show all')
	print ('example1: mtr.*05')
	print ('example2, search pkg type: /12')
	print ('example3: search revision: r60c.*')
	
	
	string1 = input(">>> Pls input any key in sw pkg: ")
	#bo cac ky tu space o cuoi di, vi copy va paste rat de du ky tu space
	string1 = string1.strip()
	
	start = timer()
	lines = [line.rstrip() for line in open("./swmapping.txt")]
	for line in lines:
		
		#search khong phan biet chua hoa chu thuong, vi con nguoi rat kho nho
		m = re.search(string1, line, re.IGNORECASE)
		
		if m:
			#nhom matching
			#print (m.group())
			#ca dong matching
			result_found +=1
			print (line)
	print (">>> Number of result found: ", result_found)
	end = timer()
	duration = end - start
	print (">>> Duration",duration)


def call_new_crash():
	'''
	parsing DU & RU crash csv file, to find new crash signature
	'''
	#os.system('./check_du_ru_newcrash.sh')
	print ("Example for file name: ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx ")
	userinput = input("Input excel filename or Enter to for default filename: ")
	userinput = userinput.strip()
	
	if userinput == "":
		#default file name = today file name
		#filename = "ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx"
		today= date.today()
		d1 = today.strftime("%Y%m%d") #20200423
		filename = "ENDC_DU_Crash_Alarm_PKG_Daily_Report_" + d1 + ".xlsx"
		print ("default file name:", filename)
	else:
		filename = userinput
	
	
	#du_dataset,ru_dataset = parsing_excel_by_pandas.parsing_excel_file('ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200422.xlsx')
	du_dataset,ru_dataset = parsing_excel_by_pandas.parsing_excel_file(filename)
	
	print (">>> Parsing DU crash")
	new_crash.print_logo("du")
	
	new_crash.new_crash_check(du_dataset)
	print (">>> Parsing RU crash")
	new_crash.print_logo("ru")
	new_crash.new_crash_check(ru_dataset)

def get_line(line_index, filepath):
	'''
	return dict of 100 line before
	{line_index, line_content}
	'''
	dict_line = {}
	thefile = open(filepath, encoding = "ISO-8859-1")
	for lineno, line in enumerate(thefile):
		#luu 100 line phia truoc vao de tim kiem cho nhanh
		#200 thi se boc nham TR ID khac, 100 la vua
		if lineno >= line_index - 100 and lineno < line_index:
			dict_line[lineno] = line
		
		if lineno > line_index:
			thefile.close()
			break
	
	return dict_line
	
	

def search_mhweb_offline(search_string):
	'''
	Function:
	Input crash_string
	Output: set of TR ID
	'''


	search_string = create_python_regex_string(search_string)
	print ("Regex:", search_string)
	#print ("-"*30)
	start = timer()
	

	#search trong 1 file nho, de test cho nhanh
	#mhwebfilepath = 'data.txt'

	
	# dua vao dong nay de biet dang search file nao, vi co 2 file
	print (">>> searching", mhwebfilepath, "...")

	thefile = open(mhwebfilepath, encoding = "ISO-8859-1")
	
	result_found = 0
	#dung cach nay cho ket qua tuc thi, tiet kiem bo nho
	
	#bien nay de luu vi tri line chua ket qua tim
	result_lines = []
	for lineno, line in enumerate(thefile):
		#m = re.search(search_string, line.strip(), re.IGNORECASE)
		
		#print de biet toi line nao
		if lineno%6800000 == 0:
			#cho nay se tim cach fix sau
			total_line = 37463606
			print ('File Searching Progress:', int(100*(lineno/total_line)), '%')
		m = re.match(search_string, line.strip())
		if m:
			result_found +=1
			result_lines.append(lineno)
			#turning log
			if result_found >= 30 :
				thefile.close()
				break

	#find TR_ID
	print (">>> Matching log found, start matching TR number...")
	tr_id_results = set()
	
	if len(result_lines) == 0:
		print (">>> No matching TR found.")
	else:
		#update trang thai cho no dep mat
		prog = pyprog.ProgressBar(" ", "", len(result_lines))
		for i, x in enumerate(result_lines):
			#print ("processing...", x)
			prog.set_stat(i+1)
			prog.update()
			while x > 1:
				#check_line= get_line(x-1, mhwebfilepath)
				
				#mot lan check 100 line, check line from x - 1 to x-101
				check_lines= get_line(x-1, mhwebfilepath)
				
				found_result = False
				for item in check_lines.keys():
					pat = r'<value>([a-zA-Z]{2}[0-9]{5})</value></column>'
					m = re.match(pat, check_lines[item])
					if m:
						
						#no need to print this, only print progress update bar
						#print (x, check_lines[item].strip(), m.group(1))
						tr_id_results.add(m.group(1))
						found_result = True
						#tim co ket qua thi thoat ngay
						break
				
				if found_result:
					break
				x = x-1

		print('-'*30)
		print(">>> TR match found:", tr_id_results)
		print('-'*30)

		
	end = timer()
	duration = end - start
	print (">>> Duration",duration)
	return tr_id_results
	
	
	
def go_to_line():
	start_position = 0
	while(1):
		user_input = input("Input, 1000: go to line 1000 | nN: next line | s/q: exit >>> :")

		#neu input chi la so nguyen, thi go to line
		m = re.match('^(\d+)$', user_input)
		if m:
			start = timer()
			print (">>> Reading file", mhwebfilepath )
			line_no = int(user_input)
			start_position = line_no + 30
			lines = read_big_file.picklines(mhwebfilepath, line_no, 30)
			
			
			for item  in lines:
				print (item[0],item[1].strip())
			end = timer()
			duration = end - start
			print ("searching duration:", duration)
			
		m1 = re.match('^[sSqQ]$', user_input)
		if m1:
			break
		
		m2 = re.match('^[nN]$', user_input)
		#doc them 30 dong
		if m2:
			start = timer()
			print (">>> Reading file", mhwebfilepath )
			line_no = start_position
			start_position = line_no + 30
			lines = read_big_file.picklines(mhwebfilepath, line_no, 30)
			
			
			for item  in lines:
				print (item[0],item[1].strip())
			end = timer()
			duration = end - start
			print ("searching duration:", duration)


def get_tr_content():
	while(1):
		text = input("Intput TR_ID to get TR content, example: HW82184 or HY13649 | s/q: exit ===>:")
		text = text.strip()
		print("Input =",text)
		
		#m = re.search(r'[a-zA-Z]{2}[0-9]{5}', text)
		m = re.match(r'[a-zA-Z]{2}[0-9]{5}', text)
		
		if m:
			#read_big_file.pick_first_tr(text, mhwebfilepath)
			#read_big_file.pick_first_tr('HY29889', mhwebfilepath)
			#print("Correct TR ID")
			print("Reading file", mhwebfilepath,"...")
			start = timer()
			tr_content = read_big_file.pick_first_tr(text.upper(), mhwebfilepath)
			for line in tr_content:
				print (line)
			end = timer()
			duration = end - start
			print (">>> Duration",duration)
		else:
			print ("Wrong TR ID, input again, :>>>")
		if re.search('^[sSqQ]$', text):
			break
	
	
def create_python_regex_string(crash_string):
	'''
	create regex searching string
	
	'''
	#print (crash_string)
	#bo di ngay thang
	crash_string = re.sub('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '(.*)', crash_string)
	
	#print (crash_string)
	#crash_string = new_crash.extract_crash_signature(crash_string)
	crash_string = new_crash.extract_crash_signature(crash_string, False)
	
	#print(crash_string)
	
	#replace [(] by [(.*)]
	crash_string = crash_string.replace('(', '.')
	
	#replace [)] by [(.*)]
	crash_string = crash_string.replace(')', '.')
	
	#ky tu dac biet xuong hang, "LPP_send to invalid virtual pid\"
	
	crash_string = re.sub(r'[\\]',r'.',crash_string)

	
	#replace ["] by [(.*)]
	#print('replace ["] by [.+]')
	
	crash_string1 = crash_string.replace('"', '(.*)')
	#print(crash_string1)
	
	
	
	#print('replace [<!] by [(.*)]')
	crash_string2 = crash_string1.replace('<!', '(.*)')
	#print(crash_string2)
	
	#print('replace [!> ] by [(.*)]')
	crash_string3 = crash_string2.replace('!> ', '(.*)')
	#print(crash_string3)
	
	#print('replace continue space character by \s+, chi replace neu co 2 continus space lien tuc')
	crash_string4 = re.sub('\s{2,}', '\s+', crash_string3)
	#print(crash_string4)
	
	
	#print('replace (.*)(.*)(.*) ... by (.*)')
	crash_string5 = re.sub('(\(\.\*\)){2,}', '(.*)', crash_string4)
	#print(crash_string5)
	
	return crash_string5
	

if __name__ == "__main__":
	main()