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

def test_draw_card():
    deck = Deck()
    card = deck.draw_card()
    assert card.rank == "King"
    assert card.suit == "Spades"

def test_shuffle():
    deck = Deck()
    deck.shuffle()
    card1 = deck.draw_card()
    card2 = deck.draw_card()
    assert card1.rank != "King" and card1.suit != "Spades" and card2.rank != "King" and card2.suit != "Hearts"
    