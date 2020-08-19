#!/usr/bin/env python3
import sys
filename = sys.argv[1]
num_of_lines = int(sys.argv[2])
with open(filename) as infile:
	lines = infile.readlines()

for i in range(num_of_lines):
	print(lines[i],end="")
