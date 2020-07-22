#Exercise 1  
#Write a function called distance_between_points that takes two Points as arguments and returns the distance between them.
from math import sqrt
class Point():
	def __init__(self, x, y ):
		self.x = x
		self.y = y
	def distance_to(self, other):
		delx = self.x - other.x
		dely = self.y - other.y
		return sqrt(delx **2 + dely **2)

a = Point(0,0)
b = Point(3,4)
print(f"Distant from a({a.x}, {a.y}) to b({b.x}, {b.y}) is {a.distance_to(b)}")

a = Point(0,1)
b = Point(0,5)
print(f"Distant from a({a.x}, {a.y}) to b({b.x}, {b.y}) is {a.distance_to(b)}")
