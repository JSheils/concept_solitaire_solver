from src.tools import build_deck, shuffle_deck, deal_cards
from src.automatic_actions import get_last_card_in_stack, check_for_free_card


def solver():
    return


def prep_game():
    deck = build_deck()
    cards = shuffle_deck(deck)
    tabletop = deal_cards(cards)
    check_for_free_card(tabletop)
    return tabletop
