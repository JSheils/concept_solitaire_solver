from src.tools import build_deck, shuffle_deck, deal_cards, get_tabletop
from collections import Counter


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
        "FC",
    ]
    assert deck == test_deck
    assert element_count["R1"] == 1
    assert element_count["B9"] == 1
    assert element_count["FC"] == 1
    assert element_count["BD"] == 4


def test_shuffle_deck():
    deck = build_deck()
    shuffled = shuffle_deck(deck)
    assert deck != shuffled
    assert deck.sort() == shuffled.sort()


def test_dealing_cards_into_eight_equal_stacks():
    deck = build_deck()
    shuffled = shuffle_deck(deck)
    tabletop = {}
    tabletop = deal_cards(shuffled)
    assert len(tabletop["center"][0]) == 5
    assert len(tabletop["center"]) == 8


def test_freecell_can_hold_4_cards():
    tabletop = get_tabletop()
    tabletop["freecell"] = ["BD", "BD", "BD", "F"]
    assert len(tabletop["freecell"]) == 4


def test_well_can_hold_3_cards():
    tabletop = get_tabletop()
    tabletop["well"] = ["R1", "R2", "R3"]
    assert len(tabletop["well"]) == 3
