class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def show(self):
        print(self.r, self.i)
x = Complex(3.0, -4.5)
print (x.r, x.i)


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    print("Inside loop: ", x.counter)
print(x.counter)
del x.counter

##test method
print("##test method")
x.show()

#https://docs.python.org/3/tutorial/classes.html
##test method2
print("##test method2")
xf = x.show
xf()


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs
print(e.kind)                  # shared by all dogs
print(d.name)                  # unique to d
print(e.name)                  # unique to e


class Dog2:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)                # unexpectedly shared by all dogs
print(e.tricks)                # unexpectedly shared by all dogs


class Dog3:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog3('Fido')
e = Dog3('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)


class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

b = Bag()
b.add("egg")
b.addtwice("rice")
print(b.data)
#['egg', 'rice', 'rice']

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

m = MappingSubclass(['x','y','z'])
m.update([1,2,3], ["1a", "2b", "3c"])
print(m.items_list)
#['x', 'y', 'z', (1, '1a'), (2, '2b'), (3, '3c')]