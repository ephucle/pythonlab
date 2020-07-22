#!/usr/bin/env python3
#findfiles 


import os, sys


def findfiles(root):
	for root, directories, filenames in os.walk(root):
		#for directory in directories:
		#	print(os.path.join(root, directory))
		for filename in filenames: 
			#print(os.path.join(root,filename))
			yield os.path.join(root,filename)
def main():
	root = sys.argv[1]
	files = findfiles(root)
	for file in files:
		print(file)

def count_py_file(path):
	all_files = findfiles(path)
	filter_py_file = (file for file in all_files if file.endswith(".py"))
	
	convert_to_list = list(filter_py_file)
	return len(convert_to_list), convert_to_list

def readfiles_py(path):
	'''
	return generator of lines
	'''
	count, filenames = count_py_file(path)
	for f in filenames:
		for line in open(f):
			yield line.strip()
			

if	__name__ == '__main__':
	main()