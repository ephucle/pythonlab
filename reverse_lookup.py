def reverse_lookup(d,v):
	keys = []
	for k in d:
		if d[k] == v:
			if k not in keys:
				keys.append(k)
	return keys
	
d1 = {'a':1, 'b':2, 'c':10}
print(f"reverse_lookup({d1, 10}) = {reverse_lookup(d1, 10)}")

d2 = {'a':1, 'b':2, 'c':10, 'd':2}
print(f"reverse_lookup({d2, 2}) = {reverse_lookup(d2, 2)}")

d2 = {'a':1, 'b':2, 'c':10, 'd':2}
print(f"reverse_lookup({d2, 5}) = {reverse_lookup(d2, 5)}")


