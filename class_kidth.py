#https://www.youtube.com/watch?v=tmY6FEF8f1o
import turtle
class Polygon:
	def __init__(self,sides, name, size=100, color="black", line_thickness = 2):
		self.sides = sides
		self.name = name
		self.size = size
		self.color = color
		self.line_thickness = line_thickness
		self.interior_angles = (self.sides-2)*180
		self.angle = self.interior_angles/self.sides
	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.line_thickness)
		for i in range(self.sides):
			turtle.forward(self.size)
			turtle.right(180 - self.angle)
		#turtle.done()

p = Polygon(6,"Luc Giac")
p.draw()

p10 = Polygon(10,"Da Giac 10 canh")
p10.draw()

class Square(Polygon):
	def __init__(self, size=100, color="red", line_thickness = 3):  # nho thua ke , nen giam duoc 1 bien o day
		super().__init__(4, "Square", size, color, line_thickness)  # bien common la 4, vi la hinh vuong
	def draw(self):
		turtle.begin_fill()
		super().draw() #thua ke lai ham draw cua Polygon, save code
		turtle.end_fill()
	
square = Square()

print(square.name)
print(square.sides)
print(square.size)
print(square.angle)
square.draw()

class Octagon(Polygon):
	def __init__(self, size=100/2, color="yellow", line_thickness = 4):  # nho thua ke , nen giam duoc 1 bien o day
		super().__init__(8, "Octagon", size, color, line_thickness)  # bien common la 8, vi la hinh bat giac
	def draw(self):
		turtle.begin_fill()
		super().draw() #thua ke lai ham draw cua Polygon, save code
		turtle.end_fill()

o1 = Octagon()
o1.draw()

turtle.done()