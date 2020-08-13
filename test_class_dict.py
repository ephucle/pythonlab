class Person:
	leg = 2
	def __init__(self, name):
		self.name = name
	def introduce(self):
		print("Myname is:", self.name)

person1 = Person("hoang")
print("leg", person1.leg)
person1.introduce()

print(person1.__dict__)


class President(Person):
	def __init__(self, name, country):
		self.country = country
		super().__init__(name)

p1 = President('obama', 'usa')
print(p1.__dict__)
