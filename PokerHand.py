#!/usr/bin/env python

"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

#update by Hoang Le P
"""

#from Card import *
import sys
from Card1 import *
import itertools

def check_continuity(lst):
	'''
	>> check_continuity([1,2,3,4,5])
	True
	>>> check_continuity([1,2,4,5])
	False
	>>> check_continuity([4,3,2,1])
	False
	>>> check_continuity([1,2,4,5])
	False
	'''
	return all(a+1==b for a, b in zip(lst, lst[1:]))

class PokerHand(Hand):
	all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush', 'straight', 'threekind', 'twopair', 'pair', 'highcard']
	def cal_suit_rank_list(self):
		self.suit_rank_list = []
		for card in self.cards:
			self.suit_rank_list.append((card.suit, card.rank))
		return self.suit_rank_list
	def suit_hist(self):
		"""Builds a histogram of the suits that appear in the hand.

		Stores the result in attribute suits.
		"""
		#reset every time cal
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
	def rank_hist(self):
		'''Build a histogram of ranks appears in hand
		Store the result in attribute ranks
		'''
		self.ranks = {}
		for card in self.cards:
			self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
	def rank_list(self):
		'''
		Build a list of ranks appears in hand
		Store the result in attribute ranks_list
		'''
		self.ranks_list = []
		for card in self.cards:
			self.ranks_list.append(card.rank)
	def has_flush(self):
		"""Returns True if the hand has a flush, False otherwise.
		flush: five cards with the same suit
		Note that this works correctly for hands with more than 5 cards.
		"""
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False
	def has_pair(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 2:
				return True
		return False
	def has_twopair(self):
		self.rank_hist()
		no_of_pair = 0
		for val in self.ranks.values():
			if val >= 2:
				no_of_pair +=1
		if no_of_pair >=2: 
			return True
		else: 
			return False
	def has_three_of_a_kind(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 3:
				return True
		return False
	def has_four_of_a_kind(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 4:
				return True
		return False
	def has_straight(self, size=5):
		'''has five cards with ranks in sequence'''
		self.cal_suit_rank_list()  #cal self.suit_rank_list
		#tao ra list , moi phan tu co size card
		iter2 = itertools.permutations(self.suit_rank_list, size)
		
		new_list_of_item2 = []
		for card_pack in iter2:
			card_pack_to_list = list(card_pack)
			card_pack_to_list.sort(key = lambda x:x[1])
			#remove duplicated comine
			if card_pack_to_list not in new_list_of_item2:
				#print(card_pack_to_list)
				new_list_of_item2.append(card_pack_to_list)
		
		for combine in new_list_of_item2:
			#print (combine) #[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
			ranks_of_combine = [item[1] for item in combine]    #[1, 2, 3, 4, 5]
			#print (combine, ranks_of_combine)  #[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)] [1, 2, 3, 4, 5]
			if check_continuity(ranks_of_combine):
				return True
		return False
	def has_straight_flush(self, size=5):
		'''five cards in sequence (as defined above) and with the same suit'''
		self.cal_suit_rank_list()  #cal self.suit_rank_list
		#tao ra list , moi phan tu co size card
		iter2 = itertools.permutations(self.suit_rank_list, size)
		
		new_list_of_item2 = []
		for card_pack in iter2:
			card_pack_to_list = list(card_pack)
			card_pack_to_list.sort(key = lambda x:x[1])
			#remove duplicated comine
			if card_pack_to_list not in new_list_of_item2:
				#print(card_pack_to_list)
				new_list_of_item2.append(card_pack_to_list)
		
		#duyet combine va tim ket hop
		for combine in new_list_of_item2:
			#print (combine) #[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
			ranks_of_combine = [item[1] for item in combine]    #[1, 2, 3, 4, 5]
			suits_of_combine = [item[0] for item in combine]
			#print (combine, ranks_of_combine)  #[(0, 1), (2, 2), (1, 3), (3, 4), (0, 5)] [1, 2, 3, 4, 5]
			#print (combine, suits_of_combine)  #[(0, 1), (2, 2), (1, 3), (3, 4), (0, 5)] [0, 2, 1, 3, 0]
			
			if check_continuity(ranks_of_combine) and len(set(suits_of_combine)) == 1:
				return True
		return False
	def has_full_house(self):
		''' three cards with one rank, two cards with another '''
		self.rank_hist()
		#print("self.ranks:",self.ranks) #self.ranks: {1: 3, 3: 2, 6: 1, 7: 1}
		
		hist = list(self.ranks.values())
		three = False
		#check three
		for i in range(len(hist)):
			if hist[i] >= 3:
				three = True
				hist.pop(i)
				break
		#check two
		two = False
		for i in range(len(hist)):
			if hist[i] >= 2:
				two = True
				break
		if three == True and two == True: return True
		else: return False
	def classify(self):
		self.d = {}
		for label in self.all_labels:
			self.d[label] = 0
		#print("init_dict")
		#print(self.d) #{'straightflush': 0, 'fourkind': 0, 'fullhouse': 0, 'flush': 0, 'straight': 0, 'threekind': 0, 'twopair': 0, 'pair': 0, 'highcard': 0}
		
		#all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush', 'straight', 'threekind', 'twopair', 'pair', 'highcard']
		if self.has_flush():
			self.d['flush'] = 1
		if self.has_four_of_a_kind():
			self.d['fourkind'] = 1
		if self.has_full_house():
			self.d['fullhouse'] = 1
		if self.has_pair():
			self.d['pair'] = 1
		if self.has_straight():
			self.d['straight'] = 1
		if self.has_straight_flush():
			self.d['straightflush'] = 1
		
		if self.has_three_of_a_kind():
			self.d['threekind'] = 1
			
		if self.has_twopair():
			self.d['twopair'] = 1
		
		#khong co gi ca thi se la highcard
		if not self.has_flush() and not self.has_four_of_a_kind() and not self.has_full_house() and not self.has_pair() and not self.has_straight() and not self.has_straight_flush() and not self.has_three_of_a_kind() and not self.has_twopair():
			self.d['highcard'] = 1
		
		list_of_label_with_value = list(self.d.items())
		print("All class found:",list_of_label_with_value) 
		#dict_items([('straightflush', 0), ('fourkind', 0), ('fullhouse', 0), ('flush', 0), ('straight', 0), ('threekind', 0), ('twopair', 0), ('pair', 1), ('highcard', 0)])
		
		index= 0
		while index < len(list_of_label_with_value):
			if list_of_label_with_value[index][1] > 0:
				return list_of_label_with_value[index][0]  #'pair'
			index += 1
			

def deal_to_hand_and_test():
	hand = PokerHand("Hand with straigh flush")
	#Card(suit, rank)
	card1 = Card(3,6)
	card2 = Card(1,1)
	card3 = Card(1,2)
	card4 = Card(1,3)
	card5 = Card(1,4)
	card6 = Card(1,5)
	card7 = Card(0,4)
	hand.add_card(card1)
	hand.add_card(card2)
	hand.add_card(card3)
	hand.add_card(card4)
	hand.add_card(card5)
	hand.add_card(card6)
	hand.add_card(card7)
	hand.cal_suit_rank_list()

	print(hand.label)
	print(hand.suit_rank_list)
	
	print(hand)
	
	print("---test has_three_of_a_kind---")
	print(f"hand.has_three_of_a_kind(): {hand.has_three_of_a_kind()}")
	
	print("---test has_straight---")
	print(f"hand.has_straight(): {hand.has_straight()}")
	
	print("---test has_straight_flush---")
	print(f"hand.has_straight_flush(): {hand.has_straight_flush()}")
	
	print("---test has_full_house---")
	print(f"hand.has_full_house(): {hand.has_full_house()}")

	print("--- test classify---")
	print(f"highest_class = {hand.classify()}")
	
if __name__ == '__main__':
	#deal_to_hand_and_test()
	#sys.exit()
	
	# make a deck
	deck = Deck()
	deck.shuffle()

	# deal the cards and classify the hands
	for i in range(7):
		print(f"***********Hand {i+1}**********")
		hand = PokerHand()

		deck.move_cards(hand, 7)
		hand.sort()
		print (hand)

		#hand.rank_hist()
		#print("hand.ranks:", hand.ranks)  #hand.ranks: {3: 1, 9: 1, 10: 2, 11: 1, 8: 1, 4: 1} <class 'dict'>

		#hand.suit_hist()
		#print("hand.suits:", hand.suits)  #hand.suits: {0: 4, 1: 1, 2: 2} <class 'dict'>

		#test hand type
		
		print ("has_flush:", hand.has_flush())
		print ("has_pair:", hand.has_pair())
		print ("has_twopair:", hand.has_twopair())
		print ("has_three_of_a_kind:", hand.has_three_of_a_kind())
		print ("has_four_of_a_kind:", hand.has_four_of_a_kind())
		print ("has_straight:", hand.has_straight())
		print("has_straight_flush:",  hand.has_straight_flush())
		print("has_full_house:",  hand.has_full_house())
	
		print(f">>> highest_class = {hand.classify()}")
		print("")


