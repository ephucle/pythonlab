#One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = #gcd(b, r). As a base case, we can use gcd(a, 0) = a.
def gcd(a,b):
	'''
	TIM UOC CHUNG LON NHAT
	>>> from gcd import gcd
	>>> gcd(3,1)
	1
	>>> gcd(3,0)
	3
	>>> gcd(6, 3)
	3
	>>> gcd(6, 2)
	2
	'''
	if(b==0): 
		return a 
	else: 
		return gcd(b,a%b) 

if __name__ == "__main__":
	import doctest
	doctest.testmod()