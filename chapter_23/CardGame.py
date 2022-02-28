from Hand import Hand, Deck, Card

class CardGame():
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):

    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]

        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(match)
                self.cards.remove(card)
                print(f'{self.name}\'s hand:\n{card} matches {match}\n')
                count += 1
        return count


game = CardGame()
hand0 = OldMaidHand("Frank")
hand1 = OldMaidHand("Hank")
game.deck.deal([hand0, hand1], 26)
hand0.remove_matches()
hand1.remove_matches()
print(hand0)
print(hand1)
