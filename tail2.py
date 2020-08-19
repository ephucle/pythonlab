#!/usr/bin/env python3
import sys
import argparse
parser = argparse.ArgumentParser(description='tail')
parser.add_argument('filepath', type=str, help='filepath')
parser.add_argument("-n",dest='count', type=int, help="number of line")

filepath = parser.parse_args().filepath
num_of_lines = parser.parse_args().count


with open(filepath) as infile:
	lines = infile.readlines()

#get last n line
extracted_line = lines[-1*num_of_lines:]

print("".join(extracted_line))
