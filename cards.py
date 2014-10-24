#!/usr/bin/env python

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{rank} of {suit}".format(rank=self.rank, suit=self.suit)


class Deck(object):
    def __init__(self):
        pass


