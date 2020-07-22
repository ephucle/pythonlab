from swampy.TurtleWorld import *
import time
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def koch(t, x):
	'''
	Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.
	'''
	if x < 3 :
		fd(t, x)
	else:
		koch(t, int(x/3))
		lt(t, 60)
		koch(t, int(x/3))
		rt(t, 120)
		koch(t, int(x/3))
		lt(t, 60)
		koch(t, int(x/3))

#koch(bob, 90)
#wait_for_user()


def snowflake(sides):
	'''#2.	Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.'''
	
	for i in range(sides):
		koch(bob, 180)
		rt(bob, 360/sides)

snowflake(3)
wait_for_user()

#https://www.cs.swarthmore.edu/~adanner/cs21/s09/lab12.php
#The algorithm for drawing a Koch snowflake with n sides is:
#
#for each side:
#  draw a Koch curve of the appropriate length and level
#  turn right 360.0/n degrees
