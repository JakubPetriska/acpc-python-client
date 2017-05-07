_MAX_SUITS = 4


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
