#!/usr/bin/env python3
import sys


def reverse_list(list1):
	'''
	>>> reverse_list("12345")
	'54321'
	>>> reverse_list(list("12345"))
	['5', '4', '3', '2', '1']
	'''
	new_list = list1[-1:-len(list1)-1:-1]
	return new_list

#test mini func first
import doctest
doctest.testmod()
print("-----------------------Test DONE--------------------")

if __name__ == "__main__":
	filename = sys.argv[1]
	lines = open(filename).readlines()
	reverse_lines = reverse_list(lines)
	print("".join(reverse_lines))