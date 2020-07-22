#!/usr/bin/env python3
import sys
filename = sys.argv[1]
count = int(sys.argv[2])
with open(filename) as infile:
	lines = infile.readlines()

total_line = len(lines)
extracted_line = lines[total_line-count:]

print("".join(extracted_line))
