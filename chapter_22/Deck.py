from Cards import Card

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
        if self.is_empty():
            return f'The deck is empty'
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []


red_deck = Deck()
blue_deck = Deck()
print(red_deck.cards[0])
print(red_deck.cards[0] > blue_deck.cards[12])
