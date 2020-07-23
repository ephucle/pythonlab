from card import *
class Hand(Deck):
	"""Represents a hand of playing cards. that is, the set of cards held by one player"""
	def __init__(self, label=''):
		"the init method for Hands should initialize cards with an empty list."
		self.cards = []
		self.label = label

hand = Hand('new hand')
print (hand.cards)
print (hand.label)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print (hand)

#test move card.
deck.move_cards(hand, 3)
print("all card in hand after move:")
print(hand)  #luc nay hand se co 4 card

print("Test deal_hands")
deck = Deck()

#deal card to 5 hand, each hand 2 crash
list_of_hand = deck.deal_hands(5, 2)
print(list_of_hand)