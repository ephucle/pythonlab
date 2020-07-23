class Kangaroo:
	def __init__(self, pouch_contents = []):
		self.pouch_contents = []
	def put_in_pouch(self, object):
		self.pouch_contents.append(object)
	def __str__(self):
		return str(self.pouch_contents)

#Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo, 
kanga  = Kangaroo()
roo = Kangaroo()

#and then adding roo to the contents of kanga’s pouch.
kanga.put_in_pouch(roo)

print(kanga)

print(kanga.__dict__)
