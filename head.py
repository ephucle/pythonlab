#!/usr/bin/env python3
import sys
import argparse
parser = argparse.ArgumentParser(description='head')
parser.add_argument('filepath', type=str, help='filepath', default='hamlet.txt')
parser.add_argument("-n",dest='count', type=int, help="number of line")

filepath = parser.parse_args().filepath
num_of_lines = parser.parse_args().count

with open(filepath) as infile:
	lines = infile.readlines()

list_of_first_line = lines[:num_of_lines]
print("".join(list_of_first_line))