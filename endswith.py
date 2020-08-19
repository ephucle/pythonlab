import re
def endswith(target_string, pattern):
	'''
	>>> endswith("abc123", "123")
	True
	>>> endswith("abc1234", "123")
	False
	>>> endswith("abc1234", "abc")
	False
	>>> endswith("abc123def", "3def")
	True
	>>>
	'''
	m = re.compile(pattern+"$")
	if m.search(target_string):
		return True
	else:
		return False

import doctest
doctest.testmod()