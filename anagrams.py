import sys
# Function to group anagrams together from given
# list of words
def anagrams(words):
	anagrams_list = []
	#words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS', 'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
	# sort each word in the list
	A = [''.join(sorted(word)) for word in words]
	
	#>>> A
	#['ACRS', 'ADEIPR', 'DESU', 'ENOS', 'DEGINS', 'AELN', 'ADEIPR', 'ACRS', 'ABGR', 'DESU', 'ENOS', 'ABGR', 'DESU', 'AELN', 'ACRS', 'DEGINS']
	
	# construct a dictionary where key is each sorted word
	# and value is list of indices where it is present
	dict = {}
	for i, e in enumerate(A):
		#print (i, e)
		dict.setdefault(e, []).append(i)
		#print(dict)

	# traverse the dictionary and read indices for each sorted key.
	# The anagrams are present in actual list at those indices
	
	#>>> dict.values()
	#dict_values([[0, 7, 14], [1, 6], [2, 9, 12], [3, 10], [4, 15], [5, 13], [8, 11]])
	
	for index in dict.values():
		
		#find anagram from index list
		anagram = [words[i] for i in index]
		#print([words[i] for i in index])
		#print(index, anagram)
		#[0, 7, 14] ['CARS', 'ARCS', 'SCAR']
		#[1, 6] ['REPAID', 'PAIRED']
		#[2, 9, 12] ['DUES', 'USED', 'SUED']
		#[3, 10] ['NOSE', 'ONES']
		#[4, 15] ['SIGNED', 'DESIGN']
		#[5, 13] ['LANE', 'LEAN']
		#[8, 11] ['GRAB', 'BRAG']
		anagrams_list.append(anagram)
	return anagrams_list


# Group anagrams together from given list of words
if __name__ == '__main__':
	
	# list of words
	words = [
		"CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE",
		"PAIRED", "ARCS", "GRAB", "USED", "ONES", "BRAG",
		"SUED", "LEAN", "SCAR", "DESIGN"]
	
	
	#anagrams(words)
	result = anagrams(words)
	print(result)

