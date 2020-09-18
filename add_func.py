def func(a,b):
	'''
	>>> func(2,3)
	5
	>>> func(2,10)
	12
	'''
	return a+b
	
print(func(1,2))

if __name__ == "__main__":
	import doctest
	doctest.testmod()