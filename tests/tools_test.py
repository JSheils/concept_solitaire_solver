import pytest
from src.tools import build_deck, shuffle_deck
from collections import Counter
import collections


def test_can_assert_true():
    assert True


def test_build_deck():
    deck = build_deck()
    element_count = Counter(deck)
    test_deck = [
        "R1",
        "R2",
        "R3",
        "R4",
        "R5",
        "R6",
        "R7",
        "R8",
        "R9",
        "G1",
        "G2",
        "G3",
        "G4",
        "G5",
        "G6",
        "G7",
        "G8",
        "G9",
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
        "B6",
        "B7",
        "B8",
        "B9",
        "RD",
        "RD",
        "RD",
        "RD",
        "GD",
        "GD",
        "GD",
        "GD",
        "BD",
        "BD",
        "BD",
        "BD",
        "F",
    ]
    assert deck == test_deck
    assert element_count["R1"] == 1
    assert element_count["B9"] == 1
    assert element_count["F"] == 1
    assert element_count["BD"] == 4


def test_shuffle_deck():
    deck = build_deck()
    shuffled = shuffle_deck(deck)
    assert deck != shuffled
    assert deck.sort() == shuffled.sort()
