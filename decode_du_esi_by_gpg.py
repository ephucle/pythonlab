#!/usr/bin/env python3

#note
#support to run from cygwin only due to gpg does not work on WSL 
#(Unable to contact server main-csdp.internal.ericsson.com. Please run while connected to Ericsson Corporate Network.)

from zipfile import ZipFile
import os,sys, datetime, subprocess
import shutil
#root_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"
root_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM"
nodename = "bs-yeonje-yeonjeb-GX19"
date = datetime.date.today().strftime("%Y-%m-%d")

#check if folder exist
target_folder = nodename+"_"+date
target_folder_path = os.path.join(root_path, target_folder)

if not os.path.isdir(target_folder_path):
	os.mkdir(target_folder_path)
	print(f"New folder {target_folder_path} has just been created")
else: 
	print(f"Folder {target_folder_path} existed")
	

if not os.path.isfile(os.path.join(target_folder_path,"bs-yeonje-yeonjeb-GX19_modump.zip")):
	source = os.path.join(root_path, "bs-yeonje-yeonjeb-GX19_modump.zip")
	target = os.path.join(target_folder_path, "bs-yeonje-yeonjeb-GX19_modump.zip")
	shutil.copyfile(source, target)
	print(f"Successful copy {source} to {target}")
else:
	print(f"File bs-yeonje-yeonjeb-GX19_modump.zip existed in {target_folder_path}")

#dcgm_file_path = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/bs-yeonje-yeonjeb-GX19_200804_120521_KST_MSRBS-N_CXP9024418-12_R69B43_dcgm.zip"
dcgm_file_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/bs-yeonje-yeonjeb-GX19_200804_120521_KST_MSRBS-N_CXP9024418-12_R69B43_dcgm.zip"



#bs-yeonje-yeonjeb-GX19_logfiles.zip
#bs-yeonje-yeonjeb-GX19
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
		myzip_logfiles.extract(du_esi_path, target_folder_path)
		esi_du_folder = os.path.join(target_folder_path,"rcslogs")
		global esi_du_filepath
		esi_du_filepath = os.path.join(esi_du_folder, du_esi_filename)
		print (f"Successful extract {du_esi_path} to {esi_du_folder}")  
		
		#Successful extract rcslogs/esi.du1.20200804T030752+0000.tar.gz.gpg to /mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/bs-yeonje-yeonjeb-GX19_2020-08-04/rcslogs


#['bs-yeonje-yeonjeb-GX19_bgpmrf.log.gz', 'bs-yeonje-yeonjeb-GX19_dcg_e2.log.gz', 'bs-yeonje-yeonjeb-GX19_dcg_m.log.gz', 'bs-yeonje-yeonjeb-GX19_enmfiles.zip', 'bs-yeonje-yeonjeb-GX19_logfiles.zip', 'bs-yeonje-yeonjeb-GX19_modump.zip', 'bs-yeonje-yeonjeb-GX19_ropfiles.zip', 'bs-yeonje-yeonjeb-GX19_wrateventlog_traffic.zip', 'bs-yeonje-yeonjeb-GX19_xml.zip', 'bglog_1.log.gz', 'dcgziplog.txt']


#['rcslogs/SupportUnitLog_20200627__051434.cfg', 'rcslogs/AlertLog_20200627__051434_20200802__161428.cfg', 'rcslogs/esi.ru_05-F-AIR3239.20200804T030930+0000.tar.gz.gpg', 'rcslogs/esi.ru_02-C-AIR3239.20200804T031326+0000.tar.gz.gpg', 'rcslogs/SwErrorAlarmLog_20200627__051434.log', 'rcslogs/UnitTemperatureLevelLog_20200803__000006_20200804__000004.log', 'rcslogs/SupportUnitLog_20200719__000534_20200728__000534.log', 'rcslogs/AlertLog_20200802__161428.log', 'rcslogs/esi.du1.20200804T030752+0000.tar.gz.gpg', 'rcslogs/SupportUnitLog_20200627__051434_20200719__000534.log', 'rcslogs/SwmLog_20200627051434Z', 'rcslogs/UnitTemperatureLevelLog_20200803__000003_20200803__000006.log', 'rcslogs/AlertLog_20200627__051434_20200802__161428.log', 'rcslogs/TnNetworkLog_20200627__051434.cfg', 'rcslogs/SecurityLog_20200722163514Z', 'rcslogs/TnNetworkLog_20200627__051434.log', 'rcslogs/TnApplicationLog_20200627__051434.cfg', 'rcslogs/esi.ru_01-B-AIR3239.20200804T031439+0000.tar.gz.gpg', 'rcslogs/RBS_CS_AVAILABILITY_LOG_20200804030747.xml.gz', 'rcslogs/UnitTemperatureLevelLog_20200804__000004.log', 'rcslogs/esi.ru_00-A-AIR3239.20200804T031501+0000.tar.gz.gpg', 'rcslogs/TnApplicationLog_20200627__051434.log', 'rcslogs/AiLog_19700101000027Z', 'rcslogs/esi.ru_04-E-AIR3239.20200804T031047+0000.tar.gz.gpg', 'rcslogs/AuditTrailLog_20200715185827Z', 'rcslogs/esi.ru_03-D-AIR3239.20200804T031213+0000.tar.gz.gpg', 'rcslogs/ClimateLog_20200627__051434.log', 'rcslogs/PowerSupplyLog_20200627__051434.log', 'rcslogs/PowerSupplyLog_20200627__051434.cfg', 'rcslogs/saLogAlarm_20200627__051333.log', 'rcslogs/ClimateLog_20200627__051434.cfg', 'rcslogs/AlertLog_20200802__161428.cfg', 'rcslogs/UnitTemperatureLevelLog_20200627__051434.cfg', 'rcslogs/saLogAlarm_20200627__051333.cfg', 'rcslogs/PowerDistributionLog_20200627__051434.log', 'rcslogs/BatteryLog_20200627__051434.cfg', 'rcslogs/PowerDistributionLog_20200627__051434.cfg', 'rcslogs/BatteryLog_20200627__051434.log', 'rcslogs/SupportUnitLog_20200728__000534.log', 'rcslogs/SwErrorAlarmLog_20200627__051434.cfg', 'rcslogs/date.log', 'llog.log', 'teread.log', 'pmdzpm.log']


def create_moshell_script():
	global moshell_script_path
	moshell_script_path =  os.path.join(target_folder_path, nodename + "_script.mos")
	file = open(moshell_script_path,"w+")

	file.write("gpg "+ esi_du_filepath+"\n" )
	
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
	modump_path = os.path.join(target_folder_path, "bs-yeonje-yeonjeb-GX19_modump.zip")
	print (">>> moshell path:", moshell_path )
	
	full_script = moshell_path + " " + modump_path + " " + moshell_script_path + " | tee " + output_filepath
	
	print("\n")
	print (">>> Full bash script:",full_script)
	print("\n")
	print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),"Decoding esi file by gpg...")
	
	#call bash script, to see the progress on terminal
	os.system(full_script)
	

decode_esi_by_gpg()