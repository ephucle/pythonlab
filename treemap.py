#!/usr/bin/env python3
#Problem 4: Write a function treemap to map a function over nested list.
#>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]

def treemap(func, list1):
	new_list = []
	for item in list1:
		if isinstance(item,list):
			treemap(func, item)
		else:
			new_list.append(func(item))
	return new_list
	

if __name__ == "__main__":
    import doctest
    doctest.testmod()