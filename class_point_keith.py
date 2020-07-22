import matplotlib.pyplot as plt
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def plot(self):
		plt.scatter(self.x, self.y)
		plt.show()
	def __add__(self, other):
		if not isinstance(other, Point):
			#chuyen doi int var to Point object
			other=Point(other,0)
		x = self.x + other.x
		y = self.y + other.y
		return Point(x,y)


point1 = Point(4,5)
print(point1.x, point1.y)
#point1.plot()

#plt.show()

a= Point(1,1)
b= Point(2,2)
c = a+b

print(c.x, c.y)
a.plot()
#b.plot()
#c.plot()
#plt.show()
d = a+5
d.plot()
#plt.show()
