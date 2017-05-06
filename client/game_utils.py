_MAX_SUITS = 4


def card_rank(card):
    return card // _MAX_SUITS


def card_suit(card):
    return card % _MAX_SUITS
