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
        if (other.rank == 13) and (self.rank == 1):  return -1
        if self.rank > other.rank:  return 1
        if self.rank < other.rank:  return -1
        return 0
