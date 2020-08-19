import sys
def isAnagram2(str1, str2):
	'''
	>>> isAnagram2("abc", "cab")
	True
	>>> isAnagram2("abc", "caa")
	False
	>>> isAnagram2("abc", "bac")
	True
	'''
	return sorted(str1) == sorted(str2)

words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
words_sorted = ["".join(sorted(word)) for word in words]

print(words)
print(words_sorted)

#['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
#['ACRS', 'ADEIPR', 'DESU', 'ENOS', 'DEGINS', 'AELN', 'ADEIPR', 'ACRS', 'ABGR', 'DESU', 'ENOS', 'ABGR', 'DESU', 'AELN', 'ACRS', 'DEGINS']

mydict = {}
for i,word in enumerate(words_sorted):
	mydict.setdefault(word,[]).append(i)

print(mydict) #{'ACRS': [0, 7, 14], 'ADEIPR': [1, 6], 'DESU': [2, 9, 12], 'ENOS': [3, 10], 'DEGINS': [4, 15], 'AELN': [5, 13], 'ABGR': [8, 11]}

dict2 = {}
for key, index_of_duplicated in mydict.items():
	#print(key, index_of_duplicated)
	print(key, [words[index] for index in index_of_duplicated])
	dict2[key] = [words[index] for index in index_of_duplicated]

print(dict2)
#{'ACRS': ['CARS', 'ARCS', 'SCAR'], 'ADEIPR': ['REPAID', 'PAIRED'], 'DESU': ['DUES', 'USED', 'SUED'], 'ENOS': ['NOSE', 'ONES'], 'DEGINS': ['SIGNED', 'DESIGN'], 'AELN': ['LANE', 'LEAN'], 'ABGR': ['GRAB', 'BRAG']}