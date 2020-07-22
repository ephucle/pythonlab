from math import factorial as fact
from math import sqrt
from math import fabs
import math
def estimate_pi(epsilon=0.0001):
	'''
	#The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of 1 / π:
	'''
	n=0
	x = 3
	
	y = 1/ ( 2*sqrt(2)/9801*(1103+ 26390))
	print("Init n, x, y:", n, x, y)
	while fabs(y-x) > epsilon:
		x = y
		sum = 0
		n += 1
		for i in range(n):
			sum += fact(4*i)*(1103+26390*i)/( (fact(i))**4 * 396**(4*i) )
		y = 1/(2*sqrt(2)/9801*sum)
		print("New n, x, y:", n, x, y)

	return y

#print("estimate_pi:", estimate_pi(epsilon=0.0001))
#print("estimate_pi, epsilon=10**(-6) :", estimate_pi(epsilon=10**(-6)))

print("estimate_pi, epsilon=10**(-15) :", estimate_pi(epsilon=10**(-15)))
print("*"*15)
print("math.pi: ", math.pi)
