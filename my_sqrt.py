import math
def my_sqrt(a):
	epsilon = 0.0000001
	#start point
	x= 3
	y = (x+a/x)/2
	while math.fabs(y - x ) > epsilon:   #math.fabs: Return the absolute value of the float x
		x=y
		y= (x+a/x)/2
	return y

for i in range(1,10):
	line_new = '{:>1}  {:>20}  {:>20} {:>20}'.format(i, my_sqrt(i), math.sqrt(i), math.fabs(my_sqrt(i)-math.sqrt(i)))
	print(line_new)

