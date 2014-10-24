#!/usr/bin/env python
import pytest
from cards import Card, Deck

def test_init_card():
    card = Card()
    assert card.suit is None
    assert card.rank is None

def test_init_deck():
    deck = Deck()