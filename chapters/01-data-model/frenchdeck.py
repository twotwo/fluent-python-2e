import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """一摞 Python 风格的纸牌

    Attributes
    ----------
    _cards: list

    _card_dict: dict
        黑红方梅4色各13张牌
        黑桃Ace: .sa
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades hearts diamonds clubs".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self._card_dict = {f"{card.suit[0]}{card.rank.lower()}": card for card in self._cards}

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __getattr__(self, key):
        if key in self._card_dict:
            return self._card_dict[key]
        else:
            raise AttributeError(f"'FrenchDeck' not find '{key}' in _card_dict.")
