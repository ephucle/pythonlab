#!/usr/bin/env python3
#how to use
#./split.py filename n
import sys
import itertools

filename = sys.argv[1]
n = int(sys.argv[2])

#count_total_line
total_line = 0
with open(filename) as f:
	for lines in enumerate(f):
		total_line += 1
#print (total_line)


infile = open(filename)


def write_to_file(file, iter_n):
	outfile = open(file,'w')
	for line in iter_n:
		outfile.write(line[1])
	print("Saved n item to file", file)
	outfile.close()

#print(type(infile))

lines_enum = enumerate(infile)

patch = 1
while total_line > 0:
	iter_n = itertools.islice(lines_enum, n)
	filename_new = filename+"."+str(patch)
	write_to_file(filename_new, iter_n)
	
	total_line = total_line-n
	#patch for filename
	patch += 1
