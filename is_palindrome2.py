def is_palindrome2(string1):
	'''
	>>> is_palindrome2('noon')
	True
	>>> is_palindrome2('noon1')
	False
	>>> is_palindrome2('redivider')
	True
	>>> is_palindrome2('redivider_')
	False
	>>> is_palindrome2('abba')
	True
	>>> is_palindrome2('a')
	True
	'''
	reverse_string1 = string1[::-1]
	if string1 == reverse_string1:
		return True
	else:
		return False
		
if	__name__ == '__main__':
	import doctest
	doctest.testmod()