import os
def get_file_name_ext(filepath):
	'''
	#get_file_name_ext()
	>>> name, ext = get_file_name_ext('./folder/helloworld.txt')
	>>> print(name, ext)
	helloworld txt
	'''
	path, filename = os.path.split(filepath)
	allitem = filename.split(".")
	ext = allitem[-1]
	name = filename[:len(filename)-len(ext)-1]
	return name, ext

name, ext = get_file_name_ext('./helloworld.txt')
print(name, ext)

if __name__ == "__main__":
    import doctest
    doctest.testmod()