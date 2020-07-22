def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(string):
	'''
	>>> is_palindrome('aa')
	True
	>>> is_palindrome('noon')
	True
	>>> is_palindrome('redivider')
	True
	>>> is_palindrome('ab')
	False
	>>> is_palindrome('hoang')
	False
	'''
	if first(string) != last(string):
		return False
	else:
		middle_string = middle(string)
		if middle_string == "":
			return True
		else:
			return is_palindrome(middle_string)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
