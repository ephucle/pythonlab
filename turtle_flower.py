from swampy.TurtleWorld import *
import time


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print(type(bob))


def square(t, length = 100, angle = 90):
	#ve hinh vuong
	for i in range(4):
		fd(t, length)
		#lt(self, angle=90)
		lt(t, angle)

#square(bob)
#square(bob, length = 150 )
#square(bob, length = 100, angle = 45 )

def polygon(t, length = 100, n = 4):
	#Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
	angle = 360/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

#polygon(bob,length = 100, n = 5)
#polygon(bob,length = 70, n = 6)
#polygon(bob,length = 50, n = 7)
#wait_for_user()

def circle(t, r):
	'''
	draw a circle
	'''
	from math import pi
	#chu vi hinh tron
	circumference = 2*pi*r
	step = 30
	#hint: length * n = circumference
	n = circumference / step
	#convert n to float
	n = int(n)
	polygon(t, length = step, n = n)

#circle(bob, 50)
#wait_for_user()

def arc(t, radius, angle_cirle = 360):
	'''
	draw a circle
	'''
	from math import pi
	circumference = 2*pi*radius
	step = 10
	#tong so canh
	n = int(circumference / step)
	# draw a fraction angle of circle
	fraction_n = int(n*(angle_cirle/360))
	#goc ngoai cua da giac
	angle = 360/n
	for i in range(fraction_n):
		fd(t, step)
		lt(t, angle)

#arc(bob, 100, angle_cirle = 360)
#arc(bob, 50, angle_cirle = 180)
arc(bob, radius = 100, angle_cirle = 60)



#arc(bob, 100, angle_cirle = 360)
#arc(bob, 50, angle_cirle = 180)
arc(bob, radius = 100, angle_cirle = 30)


wait_for_user()