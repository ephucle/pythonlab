#!/usr/bin/env python
#Bulk File Rename Tool
import os, shutil
import datetime

class Folder:
	def __init__(self, root='./'):
		self.root = root
		self.files = [os.path.join(root, file) for file in os.listdir(root) if os.path.isfile(os.path.join(root, file))]
		self.dirs = [os.path.join(root, folder) for folder in os.listdir(root) if os.path.isdir(os.path.join(root, folder))]
	def rename(self, prefix_name, subfolder, filter_size = 0):
		print("Prefix:", prefix_name)
		new_target_folder = os.path.join(self.root,subfolder)
		if not os.path.isdir(new_target_folder):
			print ("New folder", new_target_folder, "is created")
			os.mkdir(new_target_folder)
		else:
			print ("Folder", new_target_folder, "existed")
		
		
		#filter file  by size 
		if filter_size > 0:
			src_files = self.filter(filter_size = 40)
		else:
			src_files = self.files
		
		init_no = 1
		#for filepath in self.files:
		for filepath in src_files:
			#print(filepath)
			folder, name = os.path.split(filepath)
			#print (str(init_no).zfill(5),folder, name)
			new_filename = prefix_name+str(init_no).zfill(5)
			#print(new_filename)
			new_filename_path =os.path.join(new_target_folder, new_filename)
			print(new_filename_path)
			print("Copying {filepath} to {new_filename_path}..")
			shutil.copy(filepath, new_filename_path)
			init_no += 1
	def filter(self, filter_size = 40):
		filter_filepaths_result = []
		for filepath in self.files:
			
			info = os.stat(filepath)
			#print (info)  #os.stat_result(st_mode=33279, st_ino=1970324837036388, st_dev=12, st_nlink=1, st_uid=1000, st_gid=1000, st_size=29, st_atime=1596075614, st_mtime=1596075614, st_ctime=1596075614) 2020-07-30 09:20:14.926953
			#print (info.st_mtime)
			#modify_time = datetime.datetime.fromtimestamp(info.st_mtime)
			file_size = info.st_size
			#print(modify_time) #2020-07-30 09:19:55.676615
			print(filepath,file_size, type(file_size)) #65
			
			if file_size >= filter_size:
				filter_filepaths_result.append(filepath)
		return filter_filepaths_result
	

folder = Folder("./test_rename")

print(folder.files)
print(folder.dirs)

#test rename

folder.rename("myfiles", "newfolder2")
folder.rename("part_", "newfolder1")

print("files before sort")
print(folder.files)
print("files filter")
print(folder.files)
files_size_more_than30 = folder.filter(filter_size = 40)
print("files_size_more_than30", files_size_more_than30)


#rename with filter option
folder.rename("prefix_", "newfolder3", filter_size = 40)



#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ ./rename.py
#['./test_rename/abc.txt', './test_rename/def.txt', './test_rename/file1.txt', './test_rename/file1000.txt', './test_rename/file2.txt']
#['./test_rename/newfolder1', './test_rename/newfolder2', './test_rename/newfolder3']
#Prefix: myfiles
#Folder ./test_rename/newfolder2 existed
#./test_rename/newfolder2/myfiles00001
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder2/myfiles00002
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder2/myfiles00003
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder2/myfiles00004
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder2/myfiles00005
#Copying {filepath} to {new_filename_path}..
#Prefix: part_
#Folder ./test_rename/newfolder1 existed
#./test_rename/newfolder1/part_00001
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder1/part_00002
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder1/part_00003
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder1/part_00004
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder1/part_00005
#Copying {filepath} to {new_filename_path}..
#files before sort
#['./test_rename/abc.txt', './test_rename/def.txt', './test_rename/file1.txt', './test_rename/file1000.txt', './test_rename/file2.txt']
#files filter
#['./test_rename/abc.txt', './test_rename/def.txt', './test_rename/file1.txt', './test_rename/file1000.txt', './test_rename/file2.txt']
#./test_rename/abc.txt 29 <class 'int'>
#./test_rename/def.txt 65 <class 'int'>
#./test_rename/file1.txt 68 <class 'int'>
#./test_rename/file1000.txt 188 <class 'int'>
#./test_rename/file2.txt 402 <class 'int'>
#files_size_more_than30 ['./test_rename/def.txt', './test_rename/file1.txt', './test_rename/file1000.txt', './test_rename/file2.txt']
#Prefix: prefix_
#Folder ./test_rename/newfolder3 existed
#./test_rename/abc.txt 29 <class 'int'>
#./test_rename/def.txt 65 <class 'int'>
#./test_rename/file1.txt 68 <class 'int'>
#./test_rename/file1000.txt 188 <class 'int'>
#./test_rename/file2.txt 402 <class 'int'>
#./test_rename/newfolder3/prefix_00001
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder3/prefix_00002
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder3/prefix_00003
#Copying {filepath} to {new_filename_path}..
#./test_rename/newfolder3/prefix_00004
#Copying {filepath} to {new_filename_path}..
#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$