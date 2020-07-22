#!/usr/bin/env python3
#version 1.1, 24042020
#add function filter_last_crash, to find last crash of an signature


#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
import pandas as pd
from timeit import default_timer as timer
import os, sys
global folder, filename1
folder = '/mnt/c/working/02-Project/16-SKT_5G_Project/06-ProjectTasks/03-DailyReport/'
filename1 = 'ENDC_DU_Crash_Alarm_PKG_Daily_Report_20200424.xlsx'

def parsing_excel_file(filename):
	'''
	input: filename
	output: (du_dataset,ru_dataset)
	'''
	file_path = folder+filename
	print('Parsing', file_path)
	
	start = timer()
	
	
	#du_dataset = pd.read_excel(folder+filename, index_col=0, header=1, sheet_name=5)
	#DU crash la sheet thu 5, vi sheet nam hay bi doi ten, nen dung sheet no
	if os.path.exists(folder+filename):
		print ('>>> Reading DU crash sheet ...')
		du_dataset = pd.read_excel(file_path, header=1, sheet_name=5)
		print ('>>> Reading RU crash sheet ...')
		#ru_table = pd.read_excel(folder+filename, index_col=0, header=1, sheet_name=ru_sheet_name)
	
		#RU crash la sheet thu 6, vi sheet nam hay bi doi ten, nen dung sheet no
		ru_dataset = pd.read_excel(file_path, header=1, sheet_name=6)
	else :
		print (">>> File", file_path, "does not exist" )
		sys.exit()
	#print(">>> Data dimention:", du_table.shape)
	#print ("DU crash")
	#print(du_dataset)
	
	#print ("RU crash")
	#print(ru_dataset)
	
	#Crash Details
	#du_sites_list = du_dataset['Site Name']
	
	#no_of_du_site  = len(du_sites_list)
	#print(no_of_du_site)
	#du_head = du_dataset.columns
	#print(du_head)
	#ru_head = ru_dataset.columns
	#print(ru_head)
	
	
	
	end = timer()
	print (">>> Parsing excel time",end - start)
	
	return (du_dataset,ru_dataset)

def filter_last_crash(sign,dataset):
	'''
	input: sign,dataset
	return (last_crash_time_kst, last_crash_node, last_crash_detail, last_crash_pkg)
	'''
	#filter sign
	#https://stackoverflow.com/questions/27975069/how-to-filter-rows-containing-a-string-pattern-from-a-pandas-dataframe
	#df[df['ids'].str.contains("ball")]
	df = dataset[dataset['Crash Details'].str.contains(sign)]
	
	#sort by KST time
	df = df.sort_values(["Date Time(KST)"], ascending = (False))
	
	#print ("Filtered data frame:")
	#print (df)
	
	#get first row value
	last_crash_time_kst = df['Date Time(KST)'].values[0]
	last_crash_node = df['Site Name'].values[0]
	last_crash_detail = df['Crash Details'].values[0]
	last_crash_pkg = df['UP'].values[0]
	#print (str(last_crash_time_kst), last_crash_node, last_crash_detail, last_crash_pkg)
	return (str(last_crash_time_kst), last_crash_node, last_crash_detail, last_crash_pkg)
	
def main():
	du_dataset,ru_dataset = parsing_excel_file(filename1)
	
	#TEST two signature
	sign = "Extra: BB Restart: Small FSInfo err: cellid="
	last_crash_time_kst, last_crash_node, last_crash_detail, last_crash_pkg = filter_last_crash(sign,du_dataset)
	print (last_crash_time_kst, last_crash_node, last_crash_detail, last_crash_pkg)
	
	sign = '"<!ULL1MDBFUNR.397!> ull1nrmdbfupe_pu rpc/baseband_resource_set/handler/src/eqmhi_baseband_state_machine_impl.cc:1011'
	last_crash_time_kst, last_crash_node, last_crash_detail, last_crash_pkg = filter_last_crash(sign,du_dataset)
	print (last_crash_time_kst, last_crash_node, last_crash_detail, last_crash_pkg)

if __name__ == "__main__":
	main()
