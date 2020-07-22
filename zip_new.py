def zip_new(x,y):
	#z= [(xi, yi) for xi in x  for yi in y ]
	z= [(xi, yi) for xi in x  for yi in y if x.index(xi) == y.index(yi)] 
	return z

x = [1,2,3]
y =	[2,4,6]
z = zip_new(x,y)
print(x)
print(y)
print(z)
[1, 2, 3]
[2, 4, 6]
[(1, 2), (2, 4), (3, 6)]

z2 = zip_new([1, 2, 3], ["a", "b", "c"])
print(z2)