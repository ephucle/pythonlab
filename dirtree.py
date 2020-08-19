#!/usr/bin/env python3
import os, sys
root = sys.argv[1]

level = 0
def pretty_print_folder(root):
	global level
	#print("|--"*level + " "+root)
	level += 1
	dir_list_result = os.listdir(root)
	
	files = [item for item in dir_list_result if os.path.isfile(os.path.join(root, item))]
	#print file first
	for file in files:
		fpath = os.path.join(root, file)
		if os.path.isfile(fpath):
			if files.index(file) == len(files) - 1:
				print("\\" + '--'*level +' ' +file)
			else:
				print("|" + "--"*level + " "+file)

	#check no of folder in result
	folders = [item for item in dir_list_result if os.path.isdir(os.path.join(root, item))]
	#print (f"folder only, {folders}")
	no_of_sub_folder = len(folders)
	#print("no_of_sub_folder", no_of_sub_folder)
	if no_of_sub_folder > 0:
		for folder in folders:
			new_root = os.path.join(root, folder)
			print("|" + "--|"*level +folder)
			
			#dung ham de quy
			pretty_print_folder(new_root)


pretty_print_folder(root)