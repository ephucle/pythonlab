#!/usr/bin/env python
#Bulk File Rename Tool
import os, shutil
import datetime, sys

def get_size(filepath):
	info = os.stat(filepath)
	return info.st_size

def get_mtime(filepath):
	info = os.stat(filepath)
	return info.st_mtime

class Folder:
	def __init__(self, root='./'):
		self.root = root
		self.files = [os.path.join(root, file) for file in os.listdir(root) if os.path.isfile(os.path.join(root, file))]
		self.dirs = [os.path.join(root, folder) for folder in os.listdir(root) if os.path.isdir(os.path.join(root, folder))]
	def rename(self, prefix_name, subfolder, key = "alphabe"):
		print("Prefix:", prefix_name)
		new_target_folder = os.path.join(self.root,subfolder)
		if not os.path.isdir(new_target_folder):
			print ("New folder", new_target_folder, "is created")
			os.mkdir(new_target_folder)
		else:
			print ("Folder", new_target_folder, "existed")
		
		init_no = 1
		#sort follow key
		if key == "alphabe":
			self.sort()
		if key == "size":
			self.sort(key = "size")
		if key == "mtime":
			self.sort(key = "mtime")
			
		#for filepath in self.files:
		for filepath in self.files:
			#print(filepath)
			folder, name = os.path.split(filepath)
			#print (str(init_no).zfill(5),folder, name)
			new_filename = prefix_name+str(init_no).zfill(5)
			#print(new_filename)
			new_filename_path =os.path.join(new_target_folder, new_filename)
			print(new_filename_path)
			print(f"Copying {filepath} to {new_filename_path}..")
			shutil.copy(filepath, new_filename_path)
			init_no += 1

	def sort(self, key = "alphabe"):
		#sort files
		if key == "alphabe":
			self.files.sort()
		if key == "size":
			self.files.sort(key = get_size)
		if key == "mtime":
			self.files.sort(key = get_mtime)

folder = Folder("./test_rename")

#print(folder.files)
#print(folder.dirs)

#test rename

#folder.rename("myfiles", "newfolder2")
#folder.rename("part_", "newfolder1")

print("files before sort")
print(folder.files)


print("after sort alphabe")
print(folder.sort())
print(folder.files)


print("after sort size")
print(folder.sort(key = "size"))
print(folder.files)

print("after sort size")
print(folder.sort(key = "mtime"))
print(folder.files)

#test rename
folder.rename("myfiles", "newfolder1", key = "alphabe")
folder.rename("filenames_", "newfolder2", key = "size")
folder.rename("mtime_", "newfolder3", key = "mtime")
#end



