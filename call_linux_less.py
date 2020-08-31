#!/usr/bin/env python3
import subprocess
import shlex
def less(file_path):
	#subprocess.call(shlex.split('/usr/bin/less /mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt'))
	subprocess.call(shlex.split('/usr/bin/less ' + file_path))
	

def main():
	file_path = '/mnt/c/working/02-Project/16-SKT_5G_Project/07-Databases/03-MHWEB/combine_file.txt'
	less(file_path)

if	__name__ == '__main__':
	main()
