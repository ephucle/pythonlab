#Tagger.py
import math
from Wobbler import *
class Tagger (Wobbler):
	#overwrite steer method of Wobbler
	def steer(self):
		'''
		Add a steer method to Tagger to override the one in Wobbler. As a starting place, write a version that always points the Turtle toward the origin. Hint: use the math function atan2 and the Turtle attributes x, y and heading.

		'''
		x = self.get_x()
		y = self.get_y()
		angle = math.atan2(y,x)  #atan2(...) : atan2(y, x) Return the arc tangent (measured in radians) of y/x. Unlike atan(y/x), the signs of both x and y are considered.
		angle_to_degree = angle * 180/math.pi
		self.lt(self.get_heading() + 90 +  90 - angle_to_degree )   #get_heading(self) = Returns the current heading in degrees.  0 is east.
		
		#self.lt(angle_to_origin_degree)
	def away(self,x = 0, y = 0):
		"""Computes the heading away from the given point.
		x, y: point to face away from
		"""
		dx = self.x - x
		dy = self.y - y
		heading = math.atan2(dy, dx)
		return heading * 180 / math.pi
		
	def distance(self, x=0, y=0):
		"""Computes the distance from this turtle to the given point.
		x, y: point to find distance to
		"""
		dx = self.x - x
		dy = self.y - y
		return math.sqrt(dx**2 + dy**2)

	def distance_from(self, other):
		"""Computes the distance between turtles.
		other: Turtle object
		"""
		return self.distance(other.x, other.y)
	def turn_toward(self, x=0, y=0):
		"""Turns to face the given point.
		x, y: point to turn toward
		"""
		self.heading = self.away(x, y) + 180
		self.redraw() #Undraws and then redraws the animal.
		
world = make_world(Tagger)
world.mainloop()