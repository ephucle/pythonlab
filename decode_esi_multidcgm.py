#!/usr/bin/env python3
#version 1.1 07Aug2020.
#version 1.2 08Aug2020.
#support import function for gui
#summary result after decode
#2020/08/10 13:43 fix issue on option -r
#V1.3 2020/08/10, 20:33: support moshell to modump 1 time, speed up decode multi dcgm

######################################################################################################
#support CYGWIN and WSL (window subsystem for linux)
#usage:
#./decode_du_esi_by_gpg.py -d -r --nodename bs-yeonje-yeonjeb-GX19
#./decode_du_esi_by_gpg.py -d
#./decode_du_esi_by_gpg.py -r
#./decode_du_esi_by_gpg.py -d --path /path/to/dcgm_folder  # to decode all file in dcgm folder
#./decode_du_esi_by_gpg.py -d --path /path/to/dcgm_folder --nodename node_name  #decode only 1 dcgm
#10/Aug2020: Viet lai de co the import duoc, dung lam GUI
######################################################################################################

from zipfile import ZipFile
import os,sys, datetime, subprocess
import shutil
import argparse
import re
import tarfile
date = datetime.date.today().strftime("%Y-%m-%d")
CRED = '\033[91m'
CEND = '\033[0m'




def create_target_folder(nodename,root_path):
	'''create a target folder to extract log, if folder does not exist'''
	
	#in case script is import importing, root_path =  default dcgm path
	
	target_folder = nodename+"_"+date
	target_folder_path = os.path.join(root_path, target_folder)
	
	if not os.path.isdir(target_folder_path):
		os.mkdir(target_folder_path)
		print(f">>> New folder {target_folder_path} has just been created")
	else: 
		print(f">>> Folder {target_folder_path} existed")
	return target_folder_path

def extract_modump(dcgm_file_path, root_path):
	modump_path = ""
	with ZipFile(dcgm_file_path) as myzip:
		namelist = myzip.namelist()
		for item in namelist:
			if "_modump.zip" in item:
				modump_filename = item
				myzip.extract(modump_filename, root_path)
				print(f">>> Successful extract {modump_filename} to {root_path}")
				modump_path = os.path.join(root_path, modump_filename)
	return modump_path


def extract_logfiles(dcgm_file_path, nodename, target_folder_path, esi_du, esi_ru, selected_sector=(1,1,1,1,1,1)):
	sectorname = ("esi.ru_00" , "esi.ru_01", "esi.ru_02", "esi.ru_03", "esi.ru_04", "esi.ru_05")
	selected_sector_dict = dict(zip (sectorname,selected_sector))
	print("selected_sector_dict", selected_sector_dict)
	
	
	with ZipFile(dcgm_file_path) as myzip:
		namelist = myzip.namelist()
		
		logfiles_name = nodename + "_logfiles.zip"
		
		myzip.extract(logfiles_name, target_folder_path)
		print (f">>> Successful extract {logfiles_name} to {target_folder_path}")
		
		logfiles_path = os.path.join(target_folder_path, logfiles_name)
		with ZipFile(logfiles_path) as myzip_logfiles:
			namelist_logfiles = myzip_logfiles.namelist()
			
			ru_esi_path = []
			#get esi du and ru path
			for item in namelist_logfiles:
				if "esi.du1" in item:
					du_esi_path = item
				if "esi.ru_" in item:
					ru_esi_path.append(item) 
			
			#global esi_du, esi_ru
			if esi_du:
				print(">>> du esi path", du_esi_path) #rcslogs/esi.du1.20200804T030752+0000.tar.gz.gpg
			temp , du_esi_filename = os.path.split(du_esi_path)
			if esi_ru:
				print(">>> ru esi path", ru_esi_path)
			
			#extract ESI DU
			esi_du_filepath = []
			if esi_du:
				myzip_logfiles.extract(du_esi_path, target_folder_path)
				esi_du_folder = os.path.join(target_folder_path,"rcslogs")
				#global esi_du_filepath
				esi_du_filepath = os.path.join(esi_du_folder, du_esi_filename)
				print (f">>> Successful extract {du_esi_path} to {esi_du_folder}")  
			
			esi_ru_filepaths = []
			if esi_ru:
				#global esi_ru_filepaths
				#filter sector, help to save time, no need to decode all ru
				filter_ru_path = []
				for path in ru_esi_path:
					for key in selected_sector_dict:
						if selected_sector_dict[key] > 0 and key in path:
							filter_ru_path.append(path)
				print("filter_ru_path", filter_ru_path)
				ru_esi_path = filter_ru_path
				#sys.exit()
				
				for path in ru_esi_path:
					temp , ru_esi_filename = os.path.split(path)
					myzip_logfiles.extract(path, target_folder_path)
					esi_ru_folder = os.path.join(target_folder_path,"rcslogs")
					global esi_ru_filepath
					esi_ru_filepath = os.path.join(esi_ru_folder, ru_esi_filename)
					esi_ru_filepaths.append(esi_ru_filepath)
					print (f">>> Successful extract {ru_esi_filename} to {esi_ru_filepath}") 
	return logfiles_path, esi_du_filepath, esi_ru_filepaths

def create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths,esi_du, esi_ru, append_flag = False):
	
	#moshell_script_path =  os.path.join(target_folder_path, nodename + "_script.mos")
	moshell_script_path =  os.path.join(root_path,  "gpg_script.mos")
	if not append_flag:
		file = open(moshell_script_path,"w+")  # ghi de tu dau, writing and reading
		#file.write("#change default retry time from 3 to 20 to avoid issue network notstable during decode time"+"\n" )
		#file.write("uv gpg_retry=20"+"\n" )
	if append_flag:
		file = open(moshell_script_path,"a+") # append, writing and reading
	if esi_du:
		file.write("gpg "+ esi_du_filepath+"\n" )
	if esi_ru:
		for path in esi_ru_filepaths:
			file.write("gpg "+ path+"\n" )
	file.close()
	print(f">>> Successful created amos script {moshell_script_path}")

	return moshell_script_path


def decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path, root_path):
	
	#output_filepath = os.path.join(target_folder_path,nodename + "_script_output.log")
	output_filepath = os.path.join(root_path , "moshell_output_log.txt")
	moshell_path = subprocess.getoutput('which moshell')
	full_script = moshell_path + " " + modump_path + " " + moshell_script_path + " | tee " + output_filepath
	
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Start call bash/moshell script")
	
	#call bash script, to see the progress on terminal
	os.system(full_script)
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Decode done")
	return output_filepath

def main():

	
	#default default_dcgm_path  is home folder
	default_dcgm_path = os.path.expanduser('~')
	parser = argparse.ArgumentParser(description='ESI decode')

	#parser.add_argument("--path", dest="dcgm_path", action="store", type=str, help="path of dcgm folder", default=default_dcgm_path)
	parser.add_argument('dcgm_path', type=str, help='Input dcgm folder path', default=default_dcgm_path )
	
	parser.add_argument('-d', '--du', dest='esi_du', action='store_true', help='Parsing ESI DU')
	parser.add_argument('-r', '--ru', dest='esi_ru', action='store_true', help='Parsing ESI RU')
	parser.add_argument("--nodename",dest='nodename', type=str, help="nodename")

	nodename = parser.parse_args().nodename
	global root_path
	root_path = parser.parse_args().dcgm_path
	global esi_du, esi_ru
	
	esi_du = parser.parse_args().esi_du
	esi_ru = parser.parse_args().esi_ru

	#toi thieu phai co 1 thang duoc decode, neu user ghi ro action -d or -r
	decode_all_dcgm_flag = False
	
	
	if esi_du == False and esi_ru == False:
		esi_du = True
	if nodename == None:
		decode_all_dcgm_flag = True


	print(">>> nodename:", nodename)
	print(f">>> root path: {root_path}")
	print("esi du flag:", esi_du)
	print("esi ru flag:", esi_ru)
	print("decode_all_dcgm_flag:", decode_all_dcgm_flag)
	
	

	if decode_all_dcgm_flag == False:
		dcgm_filepaths = [os.path.join(root_path, file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and nodename in file]
		dcgm_filepaths.sort()
		#get the latest file
		dcgm_file_path = dcgm_filepaths[-1]
		print(">>> dcgm_file_path", dcgm_file_path)
		
	else:
		dcgm_filepaths = [os.path.join(root_path, file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "_dcgm.zip" in file]
		print(CRED + f">>> No of dcgm found: {len(dcgm_filepaths)}" + CEND)
		if len(dcgm_filepaths) == 0:
			print("Please select correct dcgm_folder_path")
			sys.exit()
		print(">>> dcgm_filepaths:")
		print(CRED+ "\n".join(dcgm_filepaths)+CEND)


	if decode_all_dcgm_flag == False:
		#decode 1 DCGM dua vao nodename
		target_folder_path = create_target_folder(nodename, root_path)
		modump_path = extract_modump(dcgm_file_path, root_path)
		#modump_path, logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_modump_logfiles(dcgm_file_path,nodename, target_folder_path)
		logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_logfiles(dcgm_file_path,nodename, target_folder_path,esi_du, esi_ru)
		moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths, esi_du, esi_ru, append_flag=False)
		
		#print amos script
		print(">>> Content of amos script:")
		print("*"*30)
		with open(moshell_script_path) as infile:
			print(infile.read())
		print("*"*30)
		output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path, root_path)
		
		#clear log after finish decrypted
		os.remove(modump_path)
		
		#remove temp moshell script
		os.remove(moshell_script_path)
		
		#remove logfilepath
		os.remove(logfiles_path)
		
		#remove esi gpg file
		if esi_du:
			os.remove(esi_du_filepath)
		
		if esi_ru:
			for esi_ru_filepath in esi_ru_filepaths:
				os.remove(esi_ru_filepath)
		
		#summary output
		count = 0
		success_output_list = []
		with open (output_filepath) as infile:
			lines = (line.strip() for line in infile.readlines())
			for line in lines:
				m = re.match("GPG File has been successfully decrypted and saved to (\S+)", line) 
				if m:
				#GPG File has been successfully decrypted and saved to /cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/dg-dalseo-skb-10-45_2020-08-07/rcslogs/esi.du1.20200807T032628+0000.tar.gz
					success_output_file = m.group(1)
					#print(success_output_file)
					success_output_list.append(success_output_file)
					count += 1
		if count == 0 :
			print(f">>> Fail to decoded all dcgm")
		else:
			print(">>> Successful decode to below files")
			print("\n".join(success_output_list))
		
	else:
		#truong hop nay xu ly nhieu file dcgm cung 1 luc
		output_filepaths = []
		input_nodenames = set()
		
		count = 0
		success_output_list = []
		success_nodenames = set()
		
		#lay 1 dcgm va extract modump, de dung chung cho tat ca
		modump_path = extract_modump(dcgm_filepaths[0], root_path)
		
		count_dcgm = 1
		for dcgm_file_path in dcgm_filepaths:
			#print(path)
			temp_path, dcgm_filename = os.path.split(dcgm_file_path)
			print(temp_path, dcgm_filename, sep = "|")
			#extract nodename from dcgm filename
			nodename =  re.match("(\S+)_\d{6}_\d{6}_\S+_dcgm.zip", dcgm_filename).group(1)
			print(nodename)
			input_nodenames.add(nodename)
			
			target_folder_path = create_target_folder(nodename, root_path)
			
			logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_logfiles(dcgm_file_path, nodename, target_folder_path,esi_du, esi_ru)
			if count_dcgm == 1:
				moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths ,esi_du, esi_ru, append_flag=False)
			else:
				moshell_script_path = create_moshell_script(root_path, nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths ,esi_du, esi_ru, append_flag=True)
			count_dcgm +=1
		
		#start decode ESI
		print(">>> Content of amos script:")
		print("*"*30)
		with open(moshell_script_path) as infile:
			print(infile.read())
		print("*"*30)
		output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path, modump_path, root_path)
		output_filepaths.append(output_filepath)
			
		
		
		
		#remove common modump
		os.remove(modump_path)
		print(f"{modump_path} has just been removed" )
		
		#remove logfiles.zip
		os.remove(logfiles_path)
		
		#remove amos script
		os.remove(moshell_script_path)
		
		#remove esi log
		if esi_du:
			os.remove(esi_du_filepath)
		if esi_ru:
			for path in esi_ru_filepaths:
				os.remove(path)
		
		#summary decode result
		for path in output_filepaths:
			with open (path) as infile:
				lines = (line.strip() for line in infile.readlines())
				for line in lines:
					#line = GPG File has been successfully decrypted and saved to /cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/dg-dalseo-skb-10-45_2020-08-07/rcslogs/esi.du1.20200807T032628+0000.tar.gz
					m = re.match("GPG File has been successfully decrypted and saved to (\S+)", line) 
					if m:
						success_output_file = m.group(1) #/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/dg-dalseo-skb-10-45_2020-08-07/rcslogs/esi.du1.20200807T032628+0000.tar.gz
						
						temp_path = success_output_file.partition("/rcslogs/")[0]
						temp_path2 , nodename_date = os.path.split(temp_path)
						nodename = nodename_date.partition("_")[0]
						success_nodenames.add(nodename)
						#print(success_output_file)
						success_output_list.append(success_output_file)
						count += 1
		#print("success nodename", success_nodenames)
		if count == 0 :
			print(f">>> Failed to decoded ALL dcgm:")
			print(CRED + "\n".join(dcgm_filepaths) + CEND)
			
		else:
			print(">>> Successful decode to below du, ru ESI files")
			print(CRED + "\n".join(success_output_list) + CEND)
			if len(success_nodenames) < len(input_nodenames):  #truong hop nay chi decode thanh cong vai esi, fail vai esi
				print("Detail:")
				print("#"*20)
				print("Failure nodes:")
				fail_nodes = input_nodenames.difference(success_nodenames)
				fail_nodes = list(fail_nodes)
				
				print(CRED + "\n".join(fail_nodes) + CEND)
				
				print("Success nodes:")
				success_nodenames = list(success_nodenames)
				print(CRED + "\n".join(success_nodenames) + CEND)
				print("#"*20)
			

def get_pmd_path_from_tgz(tgz_file_path):
	esi_path, name = os.path.split(tgz_file_path)
	print(esi_path, name)  #/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/metro2dg-dalseo-hosan-10-B4_2020-09-01/rcslogs esi.du1.20200901T025304+0000.tar.gz
	
	with tarfile.open(tgz_file_path, "r:gz") as tar:
		all_files = tar.getnames()
		pmd_paths = [path for path in all_files if "pmd" in path and path.endswith(".tgz")]
		
		#try to extract all
		#for pmd_path in pmd_paths:
		#	print("extracting ", pmd_path)
		#	tar.extract(pmd_path, esi_path)
			
		
	return pmd_paths

def extract_pmd_from_du_dump(tgz_file_path, pmdfiles):
	esi_path, name = os.path.split(tgz_file_path)
	with tarfile.open(tgz_file_path, "r:gz") as tar:
		for pmd_path in pmdfiles:
			tar.extract(pmd_path, esi_path)
			print("successful extracting", pmd_path)
	print("check again unzip output")
	print("all file below", esi_path)
	print("\n".join(myfunc.ls(esi_path)))

if __name__ == "__main__":
	main()