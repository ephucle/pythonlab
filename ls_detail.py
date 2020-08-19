import sys, os
import datetime
folder_path = sys.argv[1]
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]



for f in onlyfiles:
	file_path = join(folder_path, f)
	file_stats = os.stat(file_path)
	
	print(f,file_stats.st_size, datetime.datetime.fromtimestamp(file_stats.st_mtime))

	