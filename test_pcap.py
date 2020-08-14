print("test class construction")
class A:
	def __init__(self):
		pass
	
	def __init__(self, x=1):
		self.x = 1
		return 1
class A1():
	pass
class B(A):
	pass

class C(B):
	pass

class E(A,A1):
	pass
a= A(3)

try :
	print("a.x",a.x)
except:
	print("a.y",a.y)
print(C.__bases__ )
print(E.__bases__ )