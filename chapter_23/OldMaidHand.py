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


class OldMaidGame(CardGame):

    def play(self, names):
        # Remove queen of Clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print('------------ Cards have been dealt.')
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print('------------ Matches discarded, game begins.')
        self.print_hands()

        # Play until all 50 cards are matched.
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print('----------- Game Over!')
        self.print_hands()

    def play_one_turn(self, i):
        if self.hands[i].is_empty:
            return 0
        neighbor = self.find_neighboard(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print(f'{self.hands[i].name} picked {picked_card}.')
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def print_hands(self):
        for hand in self.hands:
            print(hand)


game = OldMaidGame()
players = ['Allen', 'Jeff', 'Chris']
game.play(players)
