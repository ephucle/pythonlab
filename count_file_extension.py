#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python$ python3 count_file_extension.py './'
import sys
folder_path = sys.argv[1]
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

dict1 = dict()
for f in onlyfiles:
	split_names = f.split('.')
	extension = split_names[-1]
	if extension not in dict1:
		dict1[extension] = 1
	else:
		dict1[extension] += 1

print(dict1)
#{'csv': 13, 'py': 132, 'log': 4, 'sh': 1, 'html': 2, 'txt': 16, 'xlsx': 4, 'zip': 2, 'png': 2, 'jpg': 1, 'xml': 2, 'pyc': 1, 'json': 1, 'amos': 1, 'db': 1}

items1 = dict1.items()
for item in items1:
	print(item[1],item[0])