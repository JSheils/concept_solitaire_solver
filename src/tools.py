import random


def build_deck():
    deck = [
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
    return deck


def shuffle_deck(deck):
    return random.sample(deck, len(deck))
