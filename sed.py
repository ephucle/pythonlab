#!/usr/bin/env python3
import re, sys, os


def sed(pattern_str, replacement_str, filename1="file1.txt", filename2="file2.txt"):
	'''
	Exercise 2  
	http://greenteapress.com/thinkpython/html/thinkpython015.html
	sed("sed", "SED" , 'file1.txt', 'file2.txt')
	'''
	try:
		infile = open(filename1)
		with open(filename2,'w') as outfile:
			for line in infile:
				#re.sub(pattern, repl, string, count=0, flags=0)
				line_after_replace = re.sub(pattern_str, replacement_str, line)
				outfile.write(line_after_replace)
		infile.close()
	except FileNotFoundError as e:
		print(f"The file {filename1} is not existed")
			
#sed("sed", "SED" , 'file1.txt', 'file2.txt')
#sed("sed", "SED" , 'filen.txt', 'file2.txt')

if	__name__ == '__main__':
	''' 
	./sed "sed" "SED" 'file1.txt' 'file2.txt'
	'''
	pattern_str = sys.argv[1]
	replacement_str = sys.argv[2]
	filename1 = sys.argv[3]
	filename2 = sys.argv[4]
	sed(pattern_str, replacement_str , filename1, filename2)
	print("replace successful")
	print("compare two file as below")
	os.system(f"diff {filename1} {filename2}")