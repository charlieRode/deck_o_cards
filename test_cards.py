#!/usr/bin/env python
import pytest
from cards import Card, Deck

def test_init_card():
    card = Card("Ace", "Spades")
    assert card.rank == "Ace"
    assert card.suit == "Spades"

def test_init_deck():
    deck = Deck()