#!/usr/bin/env python3
#dirty code
def izip(iter1, iter2):
	l1 =list(iter1)
	l2 =list(iter2)
	l3 = [(item1, item2) for i,item1 in enumerate(l1) for j,item2 in enumerate(l2) if i == j]
	l3_to_iter = iter(l3)
	return l3_to_iter



i1 =iter(["a", "b", "c"])
i2 = iter([1, 2, 3])
i3 = izip(i1,i2)

print(i3)
print(list(i3))
