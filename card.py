import random, sys

class Card(object):
	"""Represents a standard playing card."""
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	#suit_names = ['Bich', 'Chuong', 'Ro', 'Co']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	#rank_names = [None, 'Ach', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Ri', 'Dam', 'Gia']
	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		#return str(self.rank_names[self.rank]) + " of " +  str(self.suit_names[self.suit])
		#return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
		#return '%s of %s' % (self.rank_names[self.rank], self.suit_names[self.suit])
		return '%d %d [%s %s]' % (self.suit, self.rank, Card.suit_names[self.suit], Card.rank_names[self.rank] )
	
	
	def __lt__(self, other):
		# check the suits
		if self.suit < other.suit: return True
		if self.suit > other.suit: return False
		# suits are the same... check ranks
		if self.rank < other.rank: return True
		if self.rank >= other.rank: return False
	
	def __gt__(self, other):
		# check the suits
		if self.suit > other.suit: return True
		if self.suit < other.suit: return False
		# suits are the same... check ranks
		if self.rank > other.rank: return True
		if self.rank <= other.rank: return False
	def __eq__(self, other):
		if self.suit == other.suit and self.rank == other.rank: return True
		else: return False

#class Deck(object):
class Deck:
	'''Class nay tuong ung boi 1 bo bai, co 52 la bai'''
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
	def __str__(self):
		res = []
		
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)
	def pop_card(self):
		'''
		Method nay dung de rut bai, Since pop removes the last card in the list
		'''
		return self.cards.pop()
	def add_card(self, card):
		self.cards.append(card)
	def shuffle(self):
		'''xao bao'''
		random.shuffle(self.cards)
	def sort(self):
		'''Bubble sort, https://www.geeksforgeeks.org/python-program-for-bubble-sort/'''
		
		n = len(self.cards)

		#sys.exit()
		# Traverse through all array elements 
		for i in range(n-1): 
		# range(n) also work but outer loop will repeat one time more than needed. 
		# Last i elements are already in place 
			for j in range(0, n-i-1): 
			# traverse the array from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element 
				#print(f"self.cards[{j+1}] = {self.cards[j+1]} self.cards[{j}] = {self.cards[j]} ")
				if self.cards[j+1] < self.cards[j] : 
					self.cards[j], self.cards[j+1] = self.cards[j+1], self.cards[j] 
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
	def deal_hands(self, no_of_hand, no_of_card_per_hand):
		list_of_hand = []
		for i in range(no_of_hand):
			#khoi tao new hand
			hand = Hand(f"Hand{i}")
			#move card to hand
			self.move_cards(hand, no_of_card_per_hand)
			#add vao list
			list_of_hand.append(hand)
		return list_of_hand
def main():
	#dung ham main, de co the import, ma ko chay lai full code
	queen_of_diamonds = Card(1, 12)
	
	print(queen_of_diamonds.suit)
	print(queen_of_diamonds.rank)
	print(Card.suit_names)
	print(Card.rank_names)
	print(queen_of_diamonds)
	
	print("Test compare:")
	card1 = Card(2, 11)
	card2 = Card(3, 13)
	card3 = Card(2, 11)
	card4 = Card(0, 13)
	card5 = Card(2, 13)
	print(f"Compare {card1} < {card2}: {card1 < card2}")
	print(f"Compare {card1} > {card2}: {card1 > card2}")
	print(f"Compare {card1} = {card3}: {card1 == card3}")
	print(f"Compare {card1} > {card4}: {card1 > card4}")
	print(f"Compare {card5} > {card1}: {card5 > card1}")
	#sys.exit()
	
	deck = Deck()
	print("Bo bai/Deck:")
	print (deck)
	
	
	
	#xao bai
	print("Tien hanh xao bai...")
	deck.shuffle()
	
	##rut 13 la
	#print("Tien hanh rut ra 13 la...")
	#for i in range(13):
	#	card = deck.pop_card()
	#	print(i, card)
	print("Deck after suffle:", "*"*50)
	print(deck)
	print(len(deck.cards))
	
	print("Sort the deck by Deck.sort method...")
	deck.sort()
	print("deck after sort", "*"*50)
	print(deck)
	print(len(deck.cards))


class Hand(Deck):
	"""Represents a hand of playing cards. that is, the set of cards held by one player"""
	def __init__(self, label=''):
		"the init method for Hands should initialize cards with an empty list."
		self.cards = []
		self.label = label
def main2():
	#hand = Hand('new hand')
	#print (hand.cards)
	#print (hand.label)
	
	#deck = Deck()
	#card = deck.pop_card()
	#hand.add_card(card)
	#print (hand)
	
	##test move card.
	#deck.move_cards(hand, 3)
	#print("all card in hand after move:")
	#print(hand)  #luc nay hand se co 4 card
	
	print("Test deal_hands")
	deck = Deck()

	#deal card to 5 hand, each hand 2 crash
	list_of_hand = deck.deal_hands(5, 2)
	print(list_of_hand)
	print("length list_of_hand:", len(list_of_hand))
	for hand in list_of_hand:
		print("#"*10)
		print(hand.label)
		print(hand)

if __name__ == "__main__":
	main2()