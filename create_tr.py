#run script from cygwin
import subprocess
import shlex
import sys

#print(subprocess.getoutput('date'))

#signature = r'<!UPCDL.1084!> dlmacce_uecoord_getbbconfig_update.c:173: DBC: cmUeSession_p != ((__cm void*)0)n'

signature = 'Program restart. Reason: Program Crash. Program: radioapp.elf. Signal: 7. Extra: CXP2030006%5_R23B35'

dcgm_path = "/cygdrive/c/working/02-Project/16-SKT_5G_Project/03-DCGM/13Mar/bs-haeundae-jungdong-10-01_200313_134909_KST_MSRBS-N_CXP9024418-12_R54B47_dcgm.zip"


#https://stackoverflow.com/questions/5214578/print-string-to-text-file
#If you use a context manager, the file is closed automatically for you

script_file = "temp.amos"

#with open("temp.amos", "w") as file:
with open(script_file, "w") as file:
	#file.write("Purchase Amount: %s" % TotalAmount)
	file.write('l+ script.amos.log'+"\n")
	lgg_cmd = 'lgg | grep -i ' + '"' + signature + '"'
	file.write(lgg_cmd+"\n")
	file.write('invh'+"\n")
	file.write('l-'+"\n")



full_script = '/home/ephucle/moshell/moshell ' + dcgm_path + " " + script_file

print (full_script)

print ("Script content:  " + script_file)
print ("*"*40)
lines = [line.rstrip() for line in open(script_file)]
for line in lines:
	print (line)
print ("*"*40)





#print(subprocess.call(script))

#sys.exit()
#call moshell script
print(subprocess.call(shlex.split(full_script)))


