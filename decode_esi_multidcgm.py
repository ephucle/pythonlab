#!/usr/bin/env python3
#version 1.1 07Aug2020.
#version 1.2 08Aug2020.
#support import function for gui
#summary result after decode
#2020/08/10 13:43 fix issue on option -r

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

#note: you can set your default dcgm path here, or using option --path to set dcgm folder path

date = datetime.date.today().strftime("%Y-%m-%d")
if sys.platform == "linux":
	default_dcgm_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"
if sys.platform == "cygwin":
	default_dcgm_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"


def create_target_folder(nodename,root_path):
	'''create a target folder to extract log, if folder does not exist'''
	
	#in case script is import importing, root_path =  default dcgm path
	#root_path = default_dcgm_path
	target_folder = nodename+"_"+date
	target_folder_path = os.path.join(root_path, target_folder)
	
	if not os.path.isdir(target_folder_path):
		os.mkdir(target_folder_path)
		print(f">>> New folder {target_folder_path} has just been created")
	else: 
		print(f">>> Folder {target_folder_path} existed")
	return target_folder_path

def extract_modump_logfiles(dcgm_file_path, nodename, target_folder_path):
	with ZipFile(dcgm_file_path) as myzip:
		namelist = myzip.namelist()
		
		#extract modump
		modump_filename = nodename + "_modump.zip"
		myzip.extract(modump_filename, target_folder_path)
		print(f">>> Successful extract {modump_filename} to {target_folder_path}")
		#global modump_path
		global modump_path
		modump_path = os.path.join(target_folder_path, modump_filename)
		
		
		
		logfiles_name = nodename + "_logfiles.zip"
		myzip.extract(logfiles_name, target_folder_path)
		print (f">>> Successful extract {logfiles_name} to {target_folder_path}")
		#global logfiles_path
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
			
			global esi_du, esi_ru
			if esi_du:
				print(">>> du esi path", du_esi_path) #rcslogs/esi.du1.20200804T030752+0000.tar.gz.gpg
			temp , du_esi_filename = os.path.split(du_esi_path)
			if esi_ru:
				print(">>> ru esi path", ru_esi_path) #['rcslogs/esi.ru_05-F-AIR3239.20200804T030930+0000.tar.gz.gpg', 'rcslogs/esi.ru_02-C-AIR3239.20200804T031326+0000.tar.gz.gpg', 'rcslogs/esi.ru_01-B-AIR3239.20200804T031439+0000.tar.gz.gpg', 'rcslogs/esi.ru_00-A-AIR3239.20200804T031501+0000.tar.gz.gpg', 'rcslogs/esi.ru_04-E-AIR3239.20200804T031047+0000.tar.gz.gpg', 'rcslogs/esi.ru_03-D-AIR3239.20200804T031213+0000.tar.gz.gpg']
			
			#extract ESI DU
			if esi_du:
				myzip_logfiles.extract(du_esi_path, target_folder_path)
				esi_du_folder = os.path.join(target_folder_path,"rcslogs")
				global esi_du_filepath
				esi_du_filepath = os.path.join(esi_du_folder, du_esi_filename)
				print (f">>> Successful extract {du_esi_path} to {esi_du_folder}")  
			
			esi_ru_filepaths = []
			if esi_ru:
				#global esi_ru_filepaths
				for path in ru_esi_path:
					temp , ru_esi_filename = os.path.split(path)
					myzip_logfiles.extract(path, target_folder_path)
					esi_ru_folder = os.path.join(target_folder_path,"rcslogs")
					global esi_ru_filepath
					esi_ru_filepath = os.path.join(esi_ru_folder, ru_esi_filename)
					esi_ru_filepaths.append(esi_ru_filepath)
					print (f">>> Successful extract {ru_esi_filename} to {esi_ru_filepath}") 
	return modump_path, logfiles_path, esi_du_filepath, esi_ru_filepaths

def create_moshell_script(nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths):
	#global moshell_script_path
	moshell_script_path =  os.path.join(target_folder_path, nodename + "_script.mos")
	file = open(moshell_script_path,"w+")
	#change default retry time to avoid issue network notstable during decode time
	#file.write("#change default retry time from 3 to 100 to avoid issue network notstable during decode time"+"\n" )
	#file.write("uv gpg_retry=100"+"\n" )
	
	if esi_du:
		file.write("gpg "+ esi_du_filepath+"\n" )
	if esi_ru:
		for path in esi_ru_filepaths:
			file.write("gpg "+ path+"\n" )
	file.close()
	print(f">>> Successful created amos script {moshell_script_path}")
	
	print(">>> Content of amos script:")
	print("*"*30)
	with open(moshell_script_path) as infile:
		print(infile.read())
	print("*"*30)
	return moshell_script_path


def decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path):
	#global output_filepath
	output_filepath = os.path.join(target_folder_path,nodename + "_script_output.log")
	#find moshell path on WSL or cygwin
	moshell_path = subprocess.getoutput('which moshell')
	#print (">>> moshell path:", moshell_path )
	global modump_path
	full_script = moshell_path + " " + modump_path + " " + moshell_script_path + " | tee " + output_filepath
	
	#print("\n")
	#print (">>> Full bash script:",full_script)
	#print("\n")
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Decoding esi file by gpg...")
	
	#call bash script, to see the progress on terminal
	os.system(full_script)
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Decode done")
	return output_filepath

def main():
	parser = argparse.ArgumentParser(description='ESI decode')

	parser.add_argument("--path", dest="dcgm_path", action="store", type=str, help="path of dcgm folder", default=default_dcgm_path)
	parser.add_argument("--nodename",dest='nodename', type=str, help="nodename")
	parser.add_argument('-d', '--du', dest='esi_du', action='store_true', help='Parsing ESI DU')
	parser.add_argument('-r', '--ru', dest='esi_ru', action='store_true', help='Parsing ESI RU')
	

	nodename = parser.parse_args().nodename
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
		print(">>> dcgm_filepaths:",dcgm_filepaths)
		print(f">>> No of dcgm found: {len(dcgm_filepaths)}")
		

	if decode_all_dcgm_flag == False:
		#decode 1 DCGM dua vao nodename
		target_folder_path = create_target_folder(nodename, root_path)
		modump_path, logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_modump_logfiles(dcgm_file_path,nodename, target_folder_path)
		moshell_script_path = create_moshell_script(nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths)
		output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path)
		
		#clear log after finish decrypted
		os.remove(modump_path)
		#print(f"{modump_path} has just been removed" )
		
		
		#remove temp moshell script
		os.remove(moshell_script_path)
		#print(f"{moshell_script_path} has just been removed" )
		
		#remove logfilepath
		os.remove(logfiles_path)
		#print(f"{logfiles_path} has just been removed" )
		
		#remove esi gpg file
		if esi_du:
			os.remove(esi_du_filepath)
			#print(f"{esi_du_filepath} has just been removed" )
		
		if esi_ru:
			for esi_ru_filepath in esi_ru_filepaths:
				os.remove(esi_ru_filepath)
				#print(f"{esi_ru_filepath} has just been removed" )
		
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
		for dcgm_file_path in dcgm_filepaths:
			#print(path)
			temp_path, dcgm_filename = os.path.split(dcgm_file_path)
			print(temp_path, dcgm_filename, sep = "|")
			#extract nodename from dcgm filename
			nodename =  re.match("(\S+)_\d{6}_\d{6}_\S+_dcgm.zip", dcgm_filename).group(1)
			print(nodename)
			input_nodenames.add(nodename)
			
			target_folder_path = create_target_folder(nodename, root_path)
			modump_path, logfiles_path , esi_du_filepath, esi_ru_filepaths = extract_modump_logfiles(dcgm_file_path, nodename, target_folder_path)
			
			moshell_script_path = create_moshell_script(nodename, target_folder_path, esi_du_filepath, esi_ru_filepaths)
			output_filepath = decode_esi_by_gpg(nodename, target_folder_path, moshell_script_path)
			output_filepaths.append(output_filepath)
			#clear log after finish decrypted
			os.remove(modump_path)
			#print(f"{modump_path} has just been removed" )
		
			#remove temp moshell script
			os.remove(moshell_script_path)
			#print(f"{moshell_script_path} has just been removed" )
		
			#remove logfilepath
			os.remove(logfiles_path)
			#print(f"{logfiles_path} has just been removed" )
		
			##remove esi gpg file
			if esi_du:
				os.remove(esi_du_filepath)
				#print(f">>> {esi_du_filepath} has just been removed" )
			if esi_ru:
				for esi_ru_filepath in esi_ru_filepaths:
					os.remove(esi_ru_filepath)
					#print(f">>> {esi_ru_filepath} has just been removed" )
		
		
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
			print("\n".join(dcgm_filepaths))
			
		else:
			print(">>> Successful decode to below du, ru ESI files")
			print("\n".join(success_output_list))
			if len(success_nodenames) < len(input_nodenames):  #truong hop nay chi decode thanh cong vai esi, fail vai esi
				print("Detail:")
				print("#"*20)
				print("Failure nodes:")
				fail_nodes = input_nodenames.difference(success_nodenames)
				fail_nodes = list(fail_nodes)
				print("\n".join(fail_nodes))
				
				print("Success nodes:")
				success_nodenames = list(success_nodenames)
				print("\n".join(success_nodenames))
				print("#"*20)
			


if __name__ == "__main__":
	main()