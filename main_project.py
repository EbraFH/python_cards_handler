# מוחמד סלימאן 211831227
# פחאמנה אברהים - 203119987

from cards_handler import *

# the user will input his number and according to his input a deck of cards will be created and printed
while True:
    deck_of_cards_starting_range = input(
        "Enter a number (Either 2 or 6) that will be the starting number of your deck of cards: ")
    if deck_of_cards_starting_range.isnumeric():
        break
# using the function that will print the deck of cards depending on the users input
print_deck_of_cards(int(deck_of_cards_starting_range))