_MAX_SUITS = 4
_MAX_RANKS = 13


def card_rank(card):
    """Returns card rank from card's int representation.

    Args:
        card (int): Int representation of the card. This representation
                    has each card rank of each suit represented by unique integer.

    Returns:
        int: Card rank as 0 based index.
    """
    return card // _MAX_SUITS


def card_suit(card):
    """Returns card suit from card's int representation.

    Args:
        card (int): Int representation of the card. This representation
                    has each card rank of each suit represented by unique integer.

    Returns:
        int: Card suit as 0 based index.
    """
    return card % _MAX_SUITS


def generate_deck(game):
    deck = []
    for suit in range(_MAX_SUITS - game.get_num_suits(), _MAX_SUITS):
        for rank in range(_MAX_RANKS - game.get_num_ranks(), _MAX_RANKS):
            deck.append(rank * _MAX_SUITS + suit)
    return deck
