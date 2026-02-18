import collections
from random import choice

SUIT_VALUES = dict(spades=3, hearts=2, diamonds=1, clubs=0)

Card = collections.namedtuple('Card', ['rank', 'suit'])

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(SUIT_VALUES) + SUIT_VALUES[card.suit]

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def main():
    print("Chapter 1: Data Model")
    test_card = Card('7', 'diamonds')
    print(test_card)

    deck = FrenchDeck()
    print(len(deck))

    second_card = deck[1]
    print(second_card)

    random_card = choice(deck)
    print(random_card)

    top_three = deck[:3]
    print(top_three)

    # pick just the aces by starting at index 12 and skipping 13 cards at a time:
    aces = deck[12::13]
    print(aces)

    found_q = Card('Q', 'hearts') in deck
    print(f"found queen? {found_q}")

    found_ahoy = Card('ahoy', 'hearts') in deck
    print(f"found ahoy? {found_ahoy}")
    
    for card in sorted(deck, key=spades_high):
        print(card)


if __name__ == "__main__":
    main()
