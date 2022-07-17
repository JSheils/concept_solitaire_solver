# Concept Solitaire Solver
Tool for determining the percentage of Concept Solitaire games that are solvable.

## Operations
* Build Deck
* Shuffle Cards
* Deal Cards
* Algorythmicly Solve Game

## Setup Tools
* Build Deck
    * Three suits of cards each with:
        * values 1 through 9
        * four dragon cards
        * one free card
* Shuffle Cards
* Deal Cards

## Solving Tools
* Move Card to Card
    * One card can be placed on another card only if they are of a different suits and the lower card's value is one less that the target card
* Move Stack
    * a stack can be moved only if all other cards in moving stack are of alternating suits and decreasing values
    * Stacks can be moved to cards only if
        * top card of moving stack can be placed on target card
        * all other cards in moving stack are of alternating suits and decreasing values
* Move Card to Free Space
    * any card or stack can be moved to a free space
* Move Cards to Free Cell
    * Free Cells can store one card of any type
* All four Dragon cards of a suit can be moved permanently to a Free Cell if all four of a suit are exposed and there is a Free Cell that is empty of contains one of the Dragon cards of that suit
* Cards can be moved to the Well:
    * If the card is a 1
    * If the card is of the same suit and valued one higher than the top card in the well
    * Cards cannot be removed from the well once placed there
* The Free card can be removed from the game when it is exposed

    


