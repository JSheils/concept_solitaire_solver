from src.automatic_actions import check_for_free_card, get_last_card_in_stack
from src.tools import build_deck, deal_cards, shuffle_deck


class Solver:
    def __init__(self):
        self.prep_game = self.prep_game()


def prep_game():
    deck = build_deck()
    cards = shuffle_deck(deck)
    tabletop = deal_cards(cards)
    check_for_free_card(tabletop)
    return tabletop
