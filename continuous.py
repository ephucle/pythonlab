#!/usr/bin/env python
import sys
import itertools
def check_continuity(lst):
	'''
	>> check_continuity([1,2,3,4,5])
	True
	>>> check_continuity([1,2,4,5])
	False
	>>> check_continuity([4,3,2,1])
	False
	>>> check_continuity([1,2,4,5])
	False
	'''
	return all(a+1==b for a, b in zip(lst, lst[1:]))

#method2
#def check_continuity(my_list):
#	return not any(a+1!=b for a, b in zip(my_list, my_list[1:]))

#print(f'check_continuity([1,2,3] = {check_continuity([1,2,3])}')  #check_continuity([1,2,3] = True
#print(f'check_continuity([1,2,4] = {check_continuity([1,2,4])}')  #check_continuity([1,2,4] = False
#print(f'check_continuity([1,2,3,4,5] = {check_continuity([1,2,3,4,5])}')  #check_continuity([1,2,3,4,5] = True
#print(f'check_continuity([1,2,3,4,5,7,8] = {check_continuity([1,2,3,4,5,7,8])}')  #check_continuity([1,2,3,4,5,7,8] = False

def has_straight(lst, size=5):
	'''
	>>> has_straight([1,2,3,4,5])
	True
	>>> has_straight([1,2,3,4,6])
	False
	>>> has_straight([1,2,3,4,5,7,8])
	True
	>>> has_straight([1,2,3,4, 10 ,11], size = 3)
	True
	'''
	
	#permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
	#permutations(range(3),3) --> (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)
	iter1 = itertools.permutations(lst, size)
	new_list_of_item = []
	for item in iter1:
		item_to_list = sorted(list(item))
		if item_to_list not in new_list_of_item:
			new_list_of_item.append(item_to_list)
	
	#any(iterable, /) :Return True if bool(x) is True for any x in the iterable.,If the iterable is empty, return False.
	result = any(map(check_continuity,new_list_of_item))
	
	return result

#print(f'has_straight([1,2,3,4,5,6,7]): {has_straight([1,2,3,4,5,6,7])}')
#print(f'has_straight([1,2,3,4,7,8,9]): {has_straight([1,2,3,4,7,8,9])}')

if __name__ == "__main__":
	import doctest
	doctest.testmod()