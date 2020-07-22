#>>> def square(x): return x * x
#...
#>>> f = vectorize(square)
#>>> f([1, 2, 3])
#[1, 4, 9]
#>>> g = vectorize(len)
#>>> g(["hello", "world"])
#[5, 5]
#>>> g([[1, 2], [2, 3, 4]])
#[2, 3]

def vectorize(f):
	def g(x):
		value = map(f,x)
		return list(value)
	return g