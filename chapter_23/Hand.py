from Deck import Deck, Card

class Hand(Deck):

    def __init__(self, name=''):
        self.cards = []
        self.name = name

    def __str__(self):
        s = f'{self.name}\'s Hand '
        if self.is_empty():
            s += f'is empty\n'
            return s
        s += f'contains:\n{Deck.__str__(self)}'
        s += f'{len(self.cards)} cards in total.\n'
        return s

    def add(self, card):
        self.cards.append(card)
