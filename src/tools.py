import random
from collections import defaultdict


def build_deck():
    return [
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


def shuffle_deck(deck):
    return random.sample(deck, len(deck))


def deal_cards(deck):
    tabletop = get_tabletop()
    i = 0
    while i < len(deck):
        j = 0
        while j < 8:
            temp_list = tabletop["center"][j]
            if type(temp_list) is not list:
                temp_list = []
            card = deck.pop(0)
            temp_list.append(card)
            tabletop["center"][j] = temp_list
            j += 1
        i += 1
    return tabletop


def get_tabletop():
    tabletop = defaultdict(list)
    tabletop["center"] = [[], [], [], [], [], [], [], []]
    tabletop["freecell"] = [None, None, None, None]
    tabletop["well"] = [None, None, None]
    return tabletop
