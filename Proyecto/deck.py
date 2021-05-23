import random


class Deck:
    cards = []

    def __init__(self, cards):
        self.cards = cards.copy()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards[0]
