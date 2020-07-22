def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

s=[[1,2],[3,4]]
#print("Flattened list is: ",flatten(s))
#Flattened list is:  [1, 2, 3, 4]

s=[[1,2],[3,4,[5,6, [7,8]]]]
#print("Flattened list is: ",flatten(s))
#Flattened list is:  [1, 2, 3, 4, 5, 6, 7, 8]

def nested_sum(list_of_num):
	'''
	>>> nested_sum([1,2,3])
	6
	>>> nested_sum([1,2,[3,4]])
	10
	>>> nested_sum([1,2,[3,4,[7,8]]])
	25
	'''
	flatten_list= flatten(list_of_num)
	return sum(flatten_list)
	
if	__name__ == '__main__':
	import doctest
	doctest.testmod()
