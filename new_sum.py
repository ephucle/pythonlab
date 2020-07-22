def sum(*arg):
	total = 0
	for item in arg:
		total += item
	return total

print(f"sum(1,2)={sum(1,2)}")
print(f"sum(1,2,3)={sum(1,2,3)}")
print(f"sum(1,2,3,4)={sum(1,2,3,4)}")
