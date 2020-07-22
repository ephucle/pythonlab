print('convert text to list and tuble')
string = '3, 5, 7, 23'
print (string)
list_string = string.split(',')
print (list_string)
tuple_string = ()
for item in list_string:
	tuple_string += (item,)

print (tuple_string)