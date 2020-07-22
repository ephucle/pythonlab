#!/usr/bin/env python3
import itertools
#lazy code, reuse code from basic package

def permute(list1):
	'''
	>>> permute([1, 2, 3])
	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
	>>> permute(['a', 'b'])
	[['a', 'b'], ['b', 'a']]
	'''

	#print(list1)
	results =  list(itertools.permutations(list1, len(list1)))
	convert_set_to_list = []
	for item in results:
		convert_set_to_list.append(list(item))
	
	return convert_set_to_list



if __name__ == "__main__":
    import doctest
    doctest.testmod()