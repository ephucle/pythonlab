import sys, re
from collections import Counter
filename = sys.argv[1]

words_in_book = re.findall('\w+', open(filename).read().lower())

words = re.findall('\w+', open('words.txt').read().lower())

count = Counter(words_in_book)
#print(count)

#top 20
print(f"Top 20 common words of {filename} is as below:")
print(count.most_common(20))


#set subtraction
set_words_of_book = set(words_in_book)
print(len(set_words_of_book))
set_words = set(words)
print(len(set_words))

#write a program that uses set subtraction to find words in the book that are not in the word list. 
#https://www.geeksforgeeks.org/python-set-difference/
words_in_books_not_in_words = set_words_of_book.difference(set_words) #for (A - B)
#print(words_in_books_not_in_words)
print(len(words_in_books_not_in_words))


