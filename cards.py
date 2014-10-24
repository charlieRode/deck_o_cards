#!/usr/bin/env python
import random, itertools

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{rank} of {suit}".format(rank=self.rank, suit=self.suit)


class Deck(object):
    def __init__(self):
        ranks = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
        suits = ("Diamonds", "Clubs", "Hearts", "Spades")
        tups = [tup for tup in itertools.product(ranks, suits)]
        self._cards = [Card(tup[0], tup[1]) for tup in tups]

    def __len__(self):
        return len(self._cards)