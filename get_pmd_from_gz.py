import tarfile

fname = "/mnt/c/cygwin/home/ephucle/test_esi/bs-yeonje-yeonjeb-GX19_2020-08-24/rcslogs/esi.du1.20200804T030752+0000.tar.gz"
with tarfile.open(fname, "r:gz") as tar:
	all_files = tar.getnames()
	print("extract", 'rcs/dumps/pmd/4/pmd-csAdaptor_mo_to-6007-20200803-094008.tgz')
	tar.extract('rcs/dumps/pmd/4/pmd-csAdaptor_mo_to-6007-20200803-094008.tgz', '/mnt/c/cygwin/home/ephucle/test_esi/bs-yeonje-yeonjeb-GX19_2020-08-24/rcslogs/')
	#print(all_files)
	#print("test extract all file")
	#tar.extractall('/mnt/c/cygwin/home/ephucle/test_esi/bs-yeonje-yeonjeb-GX19_2020-08-24/rcslogs/')


pmd_files = [file for file in all_files if "pmd" in file]
print("pmd file--------------")
print(pmd_files)
#pmd file--------------
#['var/pmd', 'rcs/dumps/pmd', 'rcs/dumps/pmd/3', 'rcs/dumps/pmd/3/pmd-Cat_AisPmfwkPmi-5998-20200803-094008.tgz', 'rcs/dumps/pmd/2', 'rcs/dumps/pmd/2/pmd-Antc_AisPmfwkPm-5781-20200803-094009.tgz', 'rcs/dumps/pmd/1', 'rcs/dumps/pmd/1/pmd-Cra_AisPmfwkPmi-6043-20200803-094009.tgz', 'rcs/dumps/pmd/4', 'rcs/dumps/pmd/4/pmd-csAdaptor_mo_to-6007-20200803-094008.tgz']

