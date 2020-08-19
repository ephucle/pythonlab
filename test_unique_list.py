#def unique(list_of_item):
#	new_list = []
#	for item in list_of_item:
#		if item not in new_list: new_list.append(item)
#	return new_list
#lista = [1, 2, 1, 3, 2, 5]
#print(lista, unique(lista))


def unique(list_of_item, key=None):  #default is sort by len
		if key != None:
			new_list = [key(item) for item in list_of_item]
		else:
			new_list = set(list_of_item)
		return set(new_list)

l1 = unique(["python", "java", "Python", "Java"],key=lambda x:x.lower())
print(l1)

l2 = unique(["python", "java", "Python", "Java"])
print(l2)