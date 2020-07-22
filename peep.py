#!/usr/bin/env python3
#>>> it = iter(range(5))
#>>> x, it1 = peep(it)
#>>> print(x, list(it1))
#0 [0, 1, 2, 3, 4]
import itertools

def peep(iter_item):
	'''
	it = iter(range(5))
	x, it1 = peep(it)
	print(x, list(it1))
	0 [0, 1, 2, 3, 4]
	'''
	iter_to_list = list(iter_item)
	first = iter_to_list[0]
	return first, iter(iter_to_list)
	

def peep2(iter_var):
	'''
	it = iter(range(5))
	x, it1 = peep2(it)
	print(x, list(it1))
	0 [0, 1, 2, 3, 4]
	'''
	first_item = next(iter_var)
	temp_list = []
	temp_list.append(first_item)
	temp_iter = iter(temp_list)
	#create again old iter
	old_iter_var = itertools.chain(temp_iter, iter_var)
	return first_item, old_iter_var
	

if __name__ == "__main__":
    import doctest
    doctest.testmod()