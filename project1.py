import sys
from bigfloat import *

#from math import pi as pi


def print_pi_len_n(n):
	with precision(1000):
		pi = const_pi()
		print(pi)
		type(pi)
		#pi = round(pi,n)
		#print(pi)



def main():
	#output = callcommand(sys.argv[1])

	n = int(sys.argv[1])
	print (n)
	print_pi_len_n(n)
	


if __name__ == '__main__':
	main()