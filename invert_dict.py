def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
def invert_dict(d):
	new_d = dict()
	for k in d:
		v = d[k]
		#neu key v chua ton tai thi set defaut new_d[v] = []
		new_d.setdefault(v,[])
		#new da ton tai k thi:
		if k not in new_d[v]:
			new_d[v].append(k)
	return new_d

dict1 = histogram('parrot')
print(f"dict1 = {dict1}")
hash_dict1 = invert_dict(dict1)
print(f"hash_dict1 = {hash_dict1}")