import sys
folder_path = sys.argv[1]
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

dict1 = dict()
for f in onlyfiles:
	split_names = f.split('.')
	extension = split_names[-1]
	#if extension not in dict1:
	#	dict1[extension] = 1
	#else:
	#	dict1[extension] += 1
	dict1.setdefault(extension,0)  #set defautl value = 0 if key does not exits
	dict1[extension] +=1

dict1 = dict(sorted(dict1.items(), key = lambda x:x[1], reverse = True))

print(dict1)
#{'py': 279, 'csv': 16, 'txt': 14, 'db': 8, 'zip': 4, 'xlsx': 4, 'log': 3, 'html': 3, 'png': 2, 'gif': 2, 'xml': 2, 'gitignore': 1, 'archive': 1, 'eps': 1, 'sh': 1, 'mp3': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, 'ps': 1, 'json': 1, 'ps_output_file': 1, 'jpg': 1, 'GIF': 1, 'amos': 1, 'xls': 1, 'text': 1}

print("Total file: ", sum(dict1.values()) )  #Total file:  355
print("Top 5 extension")
for item in list(dict1.items())[:5]:
	print(item)

#Top 5 extension
#('py', 279)
#('csv', 16)
#('txt', 14)
#('db', 8)
#('zip', 4)