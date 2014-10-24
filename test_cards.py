#!/usr/bin/env python
import pytest
from cards import Card, Deck

def test_init_card():
    card = Card("Ace", "Spades")
    assert card.rank == "Ace"
    assert card.suit == "Spades"

def test_init_deck():
    deck = Deck()
    assert len(deck._cards) == 52

def test_deck_length():
    deck = Deck()
    assert len(deck) == 52