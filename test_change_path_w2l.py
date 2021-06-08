import re, sys, os , platform
home_path = os.path.dirname(os.path.realpath(__file__))
print("home_path", home_path)

relative_path = "./test_dir/file3.txt"

print(relative_path)

#relative_path nay dung dung duoc cho ca window va linux



#with open(relative_path) as infile:
#	print(infile.read())


#fullpath = os.path.join(home_path,"test_dir","file3.txt")
fullpath = os.path.join(home_path,relative_path)
print("platform.system:", platform.system(), " | fullpath:", fullpath)


with open(fullpath) as infile:
	print(infile.read())