def lensort(list_of_items, reverse = False):
		new_list = sorted(list_of_items, key=len, reverse = reverse)
		return new_list

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'], reverse = True))
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'], True))

#ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$ python test_sort.py
#['c', 'perl', 'java', 'ruby', 'python', 'haskell']
#['haskell', 'python', 'perl', 'java', 'ruby', 'c']
#['haskell', 'python', 'perl', 'java', 'ruby', 'c']