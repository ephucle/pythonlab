#https://realpython.com/python-super/
#An Overview of Python’s super() Function


class Rectangle:
    def __init__(self, length=10, width=20):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

#class Square:
#    def __init__(self, length):
#        self.length = length
#
#    def area(self):
#        return self.length * self.length
#
#    def perimeter(self):
#        return 4 * self.length

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)



class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

#Cube la class chau, thua huong tat ca attri va method from Cube and Rectangle
#>>> c = Cube(4)
#>>> c.
#c.area(          c.length         c.perimeter(     c.surface_area(  c.volume(        c.width
#>>> c.length
#4
#>>> c.area()
#16
#>>> c.perimeter()
#16
#>>> c.surface_area()
#96
#>>> c.volume()
#64
#>>>