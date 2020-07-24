"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

#from Card import *
import sys
from Card1 import *


class PokerHand(Hand):

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
        #my code
        #calcu self.ranks
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    def has_twopair(self):
        self.rank_hist()
        no_of_pair = 0
        #print("print from has_twopair, self.ranks=", self.ranks)
        for val in self.ranks.values():
            if val >= 2:
                no_of_pair +=1
        print("No of pair found:", no_of_pair)
        if no_of_pair >=2: 
            return True
        else: 
            return False

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(5):
        hand = PokerHand()

        deck.move_cards(hand, 7)
        hand.sort()
        print (hand)

        hand.rank_hist()
        print("hank.ranks:", hand.ranks, type(hand.ranks))  #hank.ranks: {3: 1, 9: 1, 10: 2, 11: 1, 8: 1, 4: 1} <class 'dict'>

        hand.suit_hist()
        print("hank.suits:", hand.suits, type(hand.suits))  #hank.suits: {0: 4, 1: 1, 2: 2} <class 'dict'>

        #test hand type
        print ("has_flush:", hand.has_flush())
        print ("has_pair:", hand.has_pair())
        print ("has_twopair:", hand.has_twopair())
        print ('')

