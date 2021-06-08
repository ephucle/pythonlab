#!/usr/bin/env python3
#by Hoang Le P, 08Jun2021
#version2:
#fix scan rule
#fix user input rule
#fix term_menu printout for easier view
#link to download: https://gist.github.com/ephucle/410d9e2a0e36158b2f852b341ca76364/archive/10f12796117d41d2c2bc863b7ca52628ec6b8b9f.zip

from myfunc import ls, get_filename, Timer, call, call_moshell
import re, sys, os, platform
import pandas as pd

current_platform = platform.system()  #'CYGWIN_NT-10.0-17763-WOW64'  | 'Windows' | 'Linux'
if current_platform != 'Windows':
	from simple_term_menu import TerminalMenu

t = Timer()

#root location which store dcgm, add path here
paths = ["/mnt/c/cygwin/home/ephucle/temp", "/mnt/c/cygwin/home/ephucle/moshell_logfiles/logs_moshell/dcg","/mnt/c/working/02-Project"]


print("Start scaning folder")
t.start()
dcgm_paths = []
for path in paths:
	#should use concat two list
	print("scan", path)
	dcgm_paths += ls(path)

#filter
#dcgm_paths = [path for path in dcgm_paths if "dcgm.zip" in path or "modump.zip" in path]
#dcgm_paths = [path for path in dcgm_paths if re.search(r"dcgm.zip$",path) or re.search(r"modump.zip$",path)]
dcgm_paths = [path for path in dcgm_paths if re.search(r"dcgm.zip$",path) or re.search(r"modump.zip$",path)]

#sap xep lai dcgm_path theo thu tu ngay thang modified
dcgm_paths = sorted(dcgm_paths, key=lambda t: os.stat(t).st_mtime, reverse=True)

print("\n".join(dcgm_paths))

print("################################################")
print("no of modump path found:", len(dcgm_paths))
print("################################################")
t.stop()

sys.exit()


def search_by_nodename():
	global df
	nodename = input("nodename:")
	#df_ = df[df['nodename'].str.contains('HNA075|gHI04180B')]
	df_ = df[df['nodename'].str.contains(nodename)]
	print(df_)

def search_by_sw():
	global df
	sw = input("sw:")
	df_ = df[df['sw'].str.contains(sw)]
	print(df_)

def search_by_date():
	global df
	date = input("date:")
	df_ = df[df['date'].str.contains(date)]
	print(df_)


def get_dcgm_path_and_moshell():
	global df
	max_num_of_row = df.shape[0]
	print("\n\n\n")
	try:
		rowid = int(input("row id of dcgm:::"))
		print(rowid)
	except:
		pass
	
	if rowid > max_num_of_row-1:
		print("rowid shoud be lower than", max_num_of_row)
		get_dcgm_path_and_moshell()  #loop back the code
	
	row_data = df.iloc[rowid] # second row of data frame (Evan Zigomalas)
	print("#############################################")
	print(row_data)
	print("#############################################")
	dcgm_path = row_data['path']
	print(dcgm_path)
	
	#ask for confirm before moshell_to_dcgm
	ask_for_confirm = input("Confirm moshell to "+dcgm_path+"\nConfirm [y/Y/n/N]:")
	if ask_for_confirm == "y" or ask_for_confirm == "Y":
		call_moshell(dcgm_path)
	else:
		print("okay, no moshell")



print("extract path, nodename, date, sw")
headers=["path", "nodename", "date", "sw"]
data  = []

count = 0
for path in dcgm_paths:
	nodename = "#"
	date = "#"
	sw = "#"
	count +=1
	filename = get_filename(path)
	
	
	#find node name
	regex = "(\S+)_modump.zip"
	m = re.search(regex, filename)
	if m :
		nodename = m.group(1)
	
	regex = "(\w+)_(\d{6}_\d{6})\S+(CXP\S+)_dcgm.zip"   #"gHI03733T_190417_185011_+07_MSRBS-N_CXP2010045-1_R17B32_dcgm.zip"
	m = re.search(regex, filename)
	if m :
		nodename = m.group(1)
		#date = m.group(2)
		sw = m.group(3)
		
	#tim ngay thang
	#regex = "\S+(\d{6}_\d{6})\S+"   #"gHI03733T_190417_185011_+07_MSRBS-N_CXP2010045-1_R17B32_dcgm.zip"
	#m = re.search(regex, path)
	#if m :
	#	date = m.group(1)
	
	mtime = os.stat(path).st_mtime
	from datetime import datetime, timezone
	modified_utc = datetime.fromtimestamp(mtime, tz=timezone.utc)
	#timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
	
	#convert timezone
	from dateutil import tz
	from_zone = tz.tzutc()
	to_zone = tz.tzlocal()
	# Convert time zone
	modified_utc = modified_utc.replace(tzinfo=from_zone)
	modified_local = modified_utc.astimezone(to_zone)
	#date = modified_local
	date = modified_local.strftime('%Y%m%d_%H%M%S')
	
	
	#print(path,"|", nodename, "|", date, "|", sw)
	data.append([path,nodename,date, sw])





#https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
df= pd.DataFrame(data, columns = headers)

#df['a'] = df['a'].apply(lambda x: x + 1)
#add one more column for easier view
df['filename'] = df['path'].apply(get_filename)

print(df)

print("No of dcgm:", df.shape[0])


nodenames = set(df['nodename'])
print("No of nodename:", len(nodenames))

#print("Total DCGM found in", path1, count)

main_menu_exit = False
terminal_style = ("bg_yellow", "fg_red")
terminal_entry = [
					"0.search_dcgm_by_nodename",
					"1.search_dcgm_by_sw", 
					"2.search_dcgm_by_date", 
					"3.moshell_to_dcgm",
					"4.exit"
					
				]

terminal_menu = TerminalMenu(menu_entries = terminal_entry, menu_highlight_style=terminal_style)

while not main_menu_exit:
	terminal_sel = terminal_menu.show()
	if terminal_sel == 0:
		#os.system('clear')
		print("\n\n\n\n")
		#print("search_dcgm_by_nodename----")
		search_by_nodename()
	if terminal_sel == 1:
		#os.system('clear')
		print("\n\n\n\n")
		#print("1.search_dcgm_by_sw")
		search_by_sw()
	if terminal_sel == 2:
		#os.system('clear')
		print("\n\n\n\n")
		#print("1.search_dcgm_by_date")
		search_by_date()
	if terminal_sel == 3:
		#print("3.moshell_to_dcgm")
		get_dcgm_path_and_moshell()
		#rowid = int(input("input row id of dcgm >>>:"))
		#print(rowid)
		#data.iloc[1] # second row of data frame (Evan Zigomalas)

	if terminal_sel == 4:
		os.system('clear') #sau khi chay xong thi xoa man hinh cho sach se
		sys.exit()


#filter dcgm

## select rows containing 'bbi'
#df.filter(like='bbi', axis=0)
#         one  two  three
#rabbit    4    5      6

df_ = df[df['nodename'].str.contains('HNA075|gHI04180B')]
print(df_)


#filer by name
#sort by latest modify day

print(nodenames)


