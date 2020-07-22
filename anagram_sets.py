import sys
#https://pymotw.com/2/shelve/
import shelve
"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""


def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print (len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    """

    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print (x)


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    Returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.iteritems():
        if len(word) == n:
            res[word] = anagrams
    return res

def store_anagrams(dict_data, filename):
    s = shelve.open(filename)
    s['key1'] = dict_data
    #s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
    s.close()
    print(f"Saved successful dict data to {filename}")

def read_anagrams(shelve_db_filename, word):
	s = shelve.open(shelve_db_filename)
	d = s['key1']
	t = signature(word)
	return d[t]

if __name__ == '__main__':
    d = all_anagrams('words.txt')
    #save to db
    store_anagrams(d, 'shelve1.db')
    #test read from db 
    print(read_anagrams('shelve1.db', 'abba'))
    sys.exit()
    print_anagram_sets_in_order(d)

    eight_letters = filter_length(d, 8)
    print_anagram_sets_in_order(eight_letters)
    
