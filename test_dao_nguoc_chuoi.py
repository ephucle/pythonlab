def reverse_list(list1):
	new_list = list1[-1:-len(list1)-1:-1]
	return new_list
print(reverse_list("123456"))
print(reverse_list(list("123456")))
