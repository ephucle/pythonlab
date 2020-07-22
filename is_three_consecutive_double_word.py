import re
def is_three_consecutive_double_word(word):
	count = 0
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			count += 1
			i += 2
		else :
			i += 1
	if count >= 3: return True
	else: return False
	
#print(is_three_consecutive_double_word("aabbcc123"))
#print(is_three_consecutive_double_word("aaibbjccdda"))
#print(is_three_consecutive_double_word("aaibbcdf"))
#print(is_three_consecutive_double_word("abcd"))

words_list = re.findall( "\w+", open('words.txt').read())

tripple_words = [word for word in words_list if is_three_consecutive_double_word(word)]
print(tripple_words)
print("No of words found:", len(tripple_words))