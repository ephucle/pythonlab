#Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.

def mul(a,b):
	if a == 0 or b == 0:
		return 0
	if b == 1:
		return a
	else:
		return a + mul(a,b-1)