color_list_1 = set(["White", "Black", "Red"])
color_list_2 = {"Red", "Green"}

#khoi tao empty set
result = set()
print(color_list_1)
print(color_list_2)
print (type(color_list_1))
print (type(color_list_2))

#cach 1
print ("method1")
for item in color_list_1:
	if item not in color_list_2:
		result.add(item)

print (result)

print('difference')
#https://www.w3schools.com/python/python_sets.asp
# difference()	Returns a set containing the difference between two or more sets
different  = color_list_1.difference(color_list_2)
print (different)


print('union')
# union()	Return a set containing the union of sets
union  = color_list_1.union(color_list_2)
print (union)

print('intersection')
# intersection()	Returns a set, that is the intersection of two other sets
intersection  = color_list_1.intersection(color_list_2)
print (intersection)
