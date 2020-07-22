def is_triangle(a,b,c):
	if a+b < c:
		return False
	elif a+c < b:
		return False
	elif b+c < a:
		return False
	else:
		return True
		

def is_triangle_input():
	a = int(input("a:"))
	b = int(input("b:"))
	c = int(input("c:"))
	if a+b < c:
		print(f"{a}, {b}, {c} cannot form a tringle")
		return False
	elif a+c < b:
		print(f"{a}, {b}, {c} cannot form a tringle")
		return False
	elif b+c < a:
		print(f"{a}, {b}, {c} cannot form a tringle")
		return False
	else:
		print(f"{a}, {b}, {c} can form a tringle")
		return True