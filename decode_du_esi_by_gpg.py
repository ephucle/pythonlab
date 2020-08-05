#!/usr/bin/env python3

######################################################################################################
#support to run from cygwin only due to gpg does not work on WSL 
#(Unable to contact server main-csdp.internal.ericsson.com. Please run while connected to Ericsson Corporate Network.)
#usage:
#./decode_du_esi_by_gpg.py -d -r bs-yeonje-yeonjeb-GX19
#./decode_du_esi_by_gpg.py -d bs-yeonje-yeonjeb-GX19
#./decode_du_esi_by_gpg.py -r bs-yeonje-yeonjeb-GX19
#./decode_du_esi_by_gpg.py bs-yeonje-yeonjeb-GX19
#[~/tool_script/python/pythonlab]$ ./decode_du_esi_by_gpg.py -h
#usage: decode_du_esi_by_gpg.py [-h] [-d] [-r] nodename
#
#ESI decode
#
#positional arguments:
#  nodename    nodename
#
#optional arguments:
#  -h, --help  show this help message and exit
#  -d, --du    Parsing ESI DU
#  -r, --ru    Parsing ESI RU
######################################################################################################
from zipfile import ZipFile
import os,sys, datetime, subprocess
import shutil
import argparse

parser = argparse.ArgumentParser(description='ESI decode')
parser.add_argument(dest='nodename', type=str, help="nodename")

parser.add_argument('-d', '--du', dest='esi_du', action='store_true', help='Parsing ESI DU')
parser.add_argument('-r', '--ru', dest='esi_ru', action='store_true', help='Parsing ESI RU')

nodename = parser.parse_args().nodename
esi_du = parser.parse_args().esi_du
esi_ru = parser.parse_args().esi_ru

print("nodename:", nodename)
print("esi du flag:", esi_du)
print("esi ru flag:", esi_ru)


#root_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"
root_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"
#nodename = "bs-yeonje-yeonjeb-GX19"

#dcgm_file_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/bs-yeonje-yeonjeb-GX19_200804_120521_KST_MSRBS-N_CXP9024418-12_R69B43_dcgm.zip"

#dcgm_file_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/bs-yeonje-yeonjeb-GX19_200804_120521_KST_MSRBS-N_CXP9024418-12_R69B43_dcgm.zip"

dcgm_filepaths = [os.path.join(root_path, file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and nodename in file]
dcgm_filepaths.sort()
#get the latest file
dcgm_file_path = dcgm_filepaths[-1]
print("dcgm_file_path", dcgm_file_path)


date = datetime.date.today().strftime("%Y-%m-%d")

#check if folder exist
target_folder = nodename+"_"+date
target_folder_path = os.path.join(root_path, target_folder)

if not os.path.isdir(target_folder_path):
	os.mkdir(target_folder_path)
	print(f"New folder {target_folder_path} has just been created")
else: 
	print(f"Folder {target_folder_path} existed")
	

if not os.path.isfile(os.path.join(target_folder_path,"modump.zip")):
	source = os.path.join(root_path, "modump.zip")
	target = os.path.join(target_folder_path, "modump.zip")
	shutil.copyfile(source, target)
	print(f"Successful copy {source} to {target}")
else:
	print(f"File modump.zip existed in {target_folder_path}")




with ZipFile(dcgm_file_path) as myzip:
	namelist = myzip.namelist()
	#print(namelist)
	logfiles_name = nodename + "_logfiles.zip"
	myzip.extract(logfiles_name, target_folder_path)
	print (f"Successful extract {logfiles_name} to {target_folder_path}")
	
	logfiles_path = os.path.join(target_folder_path, logfiles_name)
	with ZipFile(logfiles_path) as myzip_logfiles:
		namelist_logfiles = myzip_logfiles.namelist()
		#print(namelist_logfiles)
		ru_esi_path = []
		for item in namelist_logfiles:
			if "esi.du1" in item:
				du_esi_path = item
			if "esi.ru_" in item:
				ru_esi_path.append(item) 
		
		print("du esi path", du_esi_path) #rcslogs/esi.du1.20200804T030752+0000.tar.gz.gpg
		temp , du_esi_filename = os.path.split(du_esi_path)
		
		print("ru esi path", ru_esi_path) #['rcslogs/esi.ru_05-F-AIR3239.20200804T030930+0000.tar.gz.gpg', 'rcslogs/esi.ru_02-C-AIR3239.20200804T031326+0000.tar.gz.gpg', 'rcslogs/esi.ru_01-B-AIR3239.20200804T031439+0000.tar.gz.gpg', 'rcslogs/esi.ru_00-A-AIR3239.20200804T031501+0000.tar.gz.gpg', 'rcslogs/esi.ru_04-E-AIR3239.20200804T031047+0000.tar.gz.gpg', 'rcslogs/esi.ru_03-D-AIR3239.20200804T031213+0000.tar.gz.gpg']
		
		#extract ESI DU
		if esi_du:
			myzip_logfiles.extract(du_esi_path, target_folder_path)
			esi_du_folder = os.path.join(target_folder_path,"rcslogs")
			global esi_du_filepath
			esi_du_filepath = os.path.join(esi_du_folder, du_esi_filename)
			print (f"Successful extract {du_esi_path} to {esi_du_folder}")  
		
		if esi_ru:
			global esi_ru_filepaths
			esi_ru_filepaths = []
			for path in ru_esi_path:
				temp , ru_esi_filename = os.path.split(path)
				myzip_logfiles.extract(path, target_folder_path)
				esi_ru_folder = os.path.join(target_folder_path,"rcslogs")
				global esi_ru_filepath
				esi_ru_filepath = os.path.join(esi_ru_folder, ru_esi_filename)
				esi_ru_filepaths.append(esi_ru_filepath)
				print (f"Successful extract {ru_esi_filename} to {esi_ru_filepath}")  



def create_moshell_script():
	global moshell_script_path
	moshell_script_path =  os.path.join(target_folder_path, nodename + "_script.mos")
	file = open(moshell_script_path,"w+")
	if esi_du:
		file.write("gpg "+ esi_du_filepath+"\n" )
	if esi_ru:
		for path in esi_ru_filepaths:
			file.write("gpg "+ path+"\n" )
	file.close()
	print(f"Successful created amos script {moshell_script_path}")
	
	print("Content of amos script:")
	print("#"*30)
	with open(moshell_script_path) as infile:
		print(infile.read())
	print("#"*30)

create_moshell_script()

def decode_esi_by_gpg():
	
	output_filepath = os.path.join(target_folder_path,nodename + "_script_output.log")
	#find moshell path on WSL or cygwin
	moshell_path = subprocess.getoutput('which moshell')
	modump_path = os.path.join(target_folder_path, "modump.zip")
	print (">>> moshell path:", moshell_path )
	
	full_script = moshell_path + " " + modump_path + " " + moshell_script_path + " | tee " + output_filepath
	
	print("\n")
	print (">>> Full bash script:",full_script)
	print("\n")
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Decoding esi file by gpg...")
	
	#call bash script, to see the progress on terminal
	os.system(full_script)
	

decode_esi_by_gpg()