#Birthday Paradox
import random, sys

def has_duplicates(l):
	'''
	>>> has_duplicates([1,1,2])
	True
	>>> has_duplicates([1,2,3])
	False
	>>> has_duplicates(['a', 'b'])
	False
	>>> has_duplicates(['a', 'b','b','c'])
	True
	'''
	if len(l)  == len(set(l)):return False
	else : return True

def create_randome_birthday():
	class_size =23
	birth_days = []
	for i in range(class_size):
		month = random.randint(1,12)
		day = random.randint(1,30)
		birth_days.append(str(month) + "-" + str(day) )
	
	return birth_days



if	__name__ == '__main__':
	bd = create_randome_birthday()
	print(bd)
	
	#check duplicates
	
	if has_duplicates(bd):print("has duplicated birthdays")
	else: print("does not have duplicated birth days")
	sys.exit()
	
	import doctest
	doctest.testmod()
