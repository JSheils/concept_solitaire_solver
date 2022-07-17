from collections import defaultdict
from src.automatic_actions import get_last_card_in_stack, check_for_free_card, move_set_of_dragon_cards_to_freecells
from src.tools import build_deck, get_tabletop, shuffle_deck, deal_cards
from src.solver import prep_game


def test_can_get_last_card_from_stack():
    stack = [
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
    ]
    last_card = get_last_card_in_stack(stack)
    assert last_card == "B4"


def test_free_card_is_removed_when_it_is_exposed():
    tabletop = defaultdict(list)
    tabletop["center"] = [[], [], [], [], [], [], [], []]
    # tabletop["center"][0] = []
    stack = ["R9", "G1", "G2", "G3", "FC"]
    tabletop["center"][0] = stack
    result = check_for_free_card(tabletop)
    assert "FC" not in result["center"][0]


def test_complete_dragon_sets_moved_to_freecells():
    tabletop = get_tabletop()
    tabletop["freecell"] = ["RD", "R7", None, "B4"]
    tabletop["center"][0] = ["R7", "R8", "R9", "G1", "G2"]
    tabletop["center"][1] = ["R7", "R8", "R9", "G1", "RD"]
    tabletop["center"][2] = ["R7", "R8", "R9", "G1", "G2"]
    tabletop["center"][3] = ["R7", "R8", "R9", "G1", "G2"]
    tabletop["center"][4] = ["R7", "R8", "RD"]
    tabletop["center"][5] = ["R7", "R8", "R9", "G1", "G2"]
    tabletop["center"][6] = ["RD"]
    tabletop["center"][7] = ["R7", "R8", "R9", "G1", "G2"]
    result = move_set_of_dragon_cards_to_freecells(tabletop)
    assert result == True
