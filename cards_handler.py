# מוחמד סלימאן 211831227
# פחאמנה אברהים - 203119987
def check_deck_of_cards_duplicates(deck_values: list) -> bool:
    """
    function that checks if the given list(deck values) contains duplications
    :param deck_values: a list that contains all the deck of cards values(2,3,4.....ace)
    :return: true if there are no duplicates else false
    """
    if len(deck_values) == len(set(deck_values)):
        return True
    else:
        return False


def valid_deck_symbols(symbol: str) -> bool:
    """
    function that checks the symbol in the deck of cards are the same as in one of the original deck of card symbols
    :param symbol: a string that includes the symbol of a deck of card
    :return: true if its valid else false
    """
    # symbols represents the symbols in the deck of cards
    symbols = ["spades♠", "clubs♣", "hearts♡", "diamonds♢"]
    if symbol in symbols:
        return True
    else:
        return False


def valid_deck_values(deck_values: list) -> bool:
    """
    function that checks if the list(deck values) contains valid deck of cards values(2,3,4..ace or 6,7...ace)
    :param deck_values: a list that contains the values of the deck
    :return:true if the deck values are valid else false
    """
    # values for a full deck of cards
    deck_values_of2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
    # values for a half deck of cards
    deck_values_of6 = [6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]

    if deck_values == deck_values_of2 or deck_values == deck_values_of6:
        return True
    else:
        return False


def check_deck(deck_of_cards: dict) -> bool:
    """
    function that calls a dictionary(deck_of_cards) checks all the requirements that would make a deck of cards
    :param deck_of_cards: a dictionary that contains symbols as a key and a list to each key that contains values of
    the deck of card
    :return: true if deck of cards is valid else false
    """
    if isinstance(deck_of_cards, dict):
        for key, value in deck_of_cards.items():
            if not (valid_deck_symbols(key) and isinstance(value, list) and check_deck_of_cards_duplicates(
                    value) and valid_deck_values(value)):
                return False
        return True
    else:
        return False


def create_deck_of_cards(starting_cards_amount: int) -> dict:
    """
    this function creates a deck of cards depending on the inserted integer
    2 will create a full deck, 6 will create a half deck else an empty deck
    after creating the deck it will be returned
    :param starting_cards_amount: number to start the deck of the cards from
    :return: returns a dictionary of deck of cards depending on the inserted integer
    """
    # a list that contains the 4 deck of card marks
    deck_symbols = ["spades♠", "clubs♣", "hearts♡", "diamonds♢"]
    # a list that contains all the numbers in the deck of cards
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
    # an element that contains the starting index of the 6 deck of cards
    start_range = starting_cards_amount - 2
    # if the users input is 2 then it will return the whole deck of cards
    if starting_cards_amount == 2:
        return {symbol: [value for value in values] for symbol in deck_symbols}
    # if the users input is 6 it will return a deck of cards starting with number 6
    elif starting_cards_amount == 6:
        return {symbol: [values[value] for value in range(start_range, len(values))] for symbol in deck_symbols}
    # anything other than number 2 or 6 will return an empty deck of cards
    else:
        return {}


def print_deck_of_cards(starting_range_for_deck: int) -> None:
    """
    function that creates a deck of cards by using the given element
    after creating the deck it will be printed to the user in an organized way
    :param starting_range_for_deck: an integer that contains the starting range of the deck of cards
    :return: prints the deck of cards depending on the users input
    """
    # deck_of_cards contains the whole deck of cards
    deck_of_cards = create_deck_of_cards(starting_range_for_deck)
    print("deck of cards: ")
    if check_deck(deck_of_cards):
        if deck_of_cards == {}:
            print(
                f"\tis empty, there are two types of deck cards (2 or 6) and your choice was '{starting_range_for_deck}'")
        else:
            for key, value in deck_of_cards.items():
                print(key, " => ", value)
    else:
        print("This deck of cards is not valid , either the symbols are invalid or the values are invalid")
