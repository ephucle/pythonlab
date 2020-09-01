import tarfile
import os, sys, myfunc
fname = "/mnt/c/working/02-Project/16-SKT_5G_Project/03-1-DCGM/metro2dg-dalseo-hosan-10-B4_2020-09-01/rcslogs/esi.du1.20200901T025304+0000.tar.gz"

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


pmd_paths = get_pmd_path_from_tgz(fname)
print("\n".join(pmd_paths))



#rcs/dumps/pmd/34/pmd-cra_main_thread-16439-20200830-054519.tgz
#rcs/dumps/pmd/75/pmd-cra_main_thread-23580-20200830-231252.tgz
#rcs/dumps/pmd/78/pmd-hdlc_lnh-3714-20200831-021545.tgz
#rcs/dumps/pmd/14/pmd-rpcScH2-8603-20200828-043736.tgz
#rcs/dumps/pmd/38/pmd-hdlc_lnh-3707-20200830-070432.tgz
#rcs/dumps/pmd/81/pmd-nc_main_thread-31353-20200831-083608.tgz
#rcs/dumps/pmd/80/pmd-nc_main_thread-5893-20200831-024152.tgz
#rcs/dumps/pmd/30/pmd-Nci_control_pro-5306-20200830-051005.tgz
#rcs/dumps/pmd/46/pmd-nc_main_thread-14833-20200830-091227.tgz
#rcs/dumps/pmd/56/pmd-cra_main_thread-24554-20200830-151528.tgz
#rcs/dumps/pmd/28/pmd-cra_main_thread-19705-20200830-025950.tgz


filter_pmd_files = [path for path in pmd_paths if "nc_main_thread" in path]
print(filter_pmd_files)

#['rcs/dumps/pmd/81/pmd-nc_main_thread-31353-20200831-083608.tgz', 'rcs/dumps/pmd/80/pmd-nc_main_thread-5893-20200831-024152.tgz', 'rcs/dumps/pmd/46/pmd-nc_main_thread-14833-20200830-091227.tgz', 'rcs/dumps/pmd/37/pmd-nc_main_thread-20726-20200830-070430.tgz', 'rcs/dumps/pmd/19/pmd-nc_main_thread-714-20200828-145412.tgz', 'rcs/dumps/pmd/10/pmd-nc_main_thread-16633-20200828-011956.tgz', 'rcs/dumps/pmd/31/pmd-nc_main_thread-30450-20200830-051005.tgz', 'rcs/dumps/pmd/33/pmd-nc_main_thread-5445-20200830-051006.tgz', 'rcs/dumps/pmd/77/pmd-nc_main_thread-12482-20200831-021545.tgz', 'rcs/dumps/pmd/53/pmd-nc_main_thread-30574-20200830-133306.tgz', 'rcs/dumps/pmd/39/pmd-nc_main_thread-6242-20200830-070432.tgz', 'rcs/dumps/pmd/20/pmd-nc_main_thread-5991-20200828-145413.tgz', 'rcs/dumps/pmd/25/pmd-nc_main_thread-16123-20200829-030441.tgz', 'rcs/dumps/pmd/5/pmd-nc_main_thread-19918-20200827-171803.tgz', 'rcs/dumps/pmd/55/pmd-nc_main_thread-6010-20200830-133307.tgz', 'rcs/dumps/pmd/47/pmd-nc_main_thread-6279-20200830-091227.tgz', 'rcs/dumps/pmd/69/pmd-nc_main_thread-12073-20200830-204921.tgz', 'rcs/dumps/pmd/12/pmd-nc_main_thread-22581-20200828-011956.tgz', 'rcs/dumps/pmd/71/pmd-nc_main_thread-14561-20200830-204922.tgz', 'rcs/dumps/pmd/23/pmd-nc_main_thread-19366-20200829-022403.tgz', 'rcs/dumps/pmd/59/pmd-nc_main_thread-6326-20200830-162721.tgz']



def extract_pmd_from_du_dump(tgz_file_path, pmdfiles):
	esi_path, name = os.path.split(tgz_file_path)
	with tarfile.open(tgz_file_path, "r:gz") as tar:
		for pmd_path in pmdfiles:
			tar.extract(pmd_path, esi_path)
			print("successful extracting", pmd_path)
	print("check again unzip output")
	print("all file below", esi_path)
	print("\n".join(myfunc.ls(esi_path)))

extract_pmd_from_du_dump(fname, filter_pmd_files)