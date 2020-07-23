#debug class
class Point:
	def __init__(self,x = 0,y =0):
		self.x = x
		self.y = y
p = Point(3, 4)
print (f"p.__dict__ = {p.__dict__}")


def print_attributes(obj):
    for attr in obj.__dict__:
        print (attr, getattr(obj, attr))

print_attributes(p)
