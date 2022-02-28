class Card:

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narft", "Ace", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "Jack", "Queen", "king"]

    def __init__(self, suit=0, rank=0):
        """ Intantiates a Card object. """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Prints the invoking object in a readibly format. """
        return f'{self.ranks[self.rank]} of {self.suits[self.suit]}'

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __ne__(self, other):
        return self.cmp(other) != 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def cmp(self, other):
        if self.suit > other.suit:  return 1
        if self.suit < other.suit:  return -1
        if (self.rank == 1) and (other.rank == 13):  return 1
        if (self.rank == 13) and (other.rank == 1):  return -1
        if self.rank > other.rank:  return 1
        if self.rank < other.rank:  return -1
        return 0


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        card = ''
        for i in range(len(self.cards)):
            card += f'{" " * i} {self.cards[i]} \n'
        return card

    def shuffle(self):
        from random import Random
        Random().shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)
