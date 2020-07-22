#!/usr/bin/env python3
#how to use
#./filter.py test.py links.py sample.csv
import sys

files = sys.argv[1:]
print(files)

def readfiles(filenames):
	for f in filenames:
		for line in open(f):
			yield line.strip()

def filter_lines(lines):
	filtered = (line for line in lines if len(line) > 40)
	return filtered


lines = readfiles(files)
#print(lines) #<generator object readfiles at 0x7fa04eaf9270>
#print(type(lines)) #<class 'generator'>


filted = filter_lines(lines)
#print(filted) #<generator object filter_lines.<locals>.<genexpr> at 0x7f76034327b0>
#print(type(filted))  #<class 'generator'>

print ("Lines which have len more than 40 as below:")
for line in filted:
	print(line)

