#!/usr/bin/env python3

def rotate_word(string, num):
	'''
	>>> rotate_word("cheer", 7)
	'jolly'
	>>> rotate_word("melon",-10)
	'c[bed'
	>>> rotate_word("abc",1)
	'bcd'
	>>> rotate_word("bcd",-1)
	'abc'
	>>> rotate_word("abcd", 2)
	'cdef'
	'''
	new_string = ""
	for c in string:
		#rotate
		new_c = chr(ord(c) + num)
		new_string += new_c
	return new_string

if	__name__ == '__main__':
	import doctest
	doctest.testmod()