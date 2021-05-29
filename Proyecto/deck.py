import random

from card import Card


class Deck:

    def __init__(self):
        self.cards = Card.create_cards()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        draw_card = self.cards[0]
        self.cards.pop(0)
        return draw_card

    def show_cards_console(self, cards):
        if(len(cards)>0):
            print("#", "\t", "ID", "\t", "Price", "\t", "Description")

            for i in range(len(cards)):
                print(str(i + 1).zfill(2), "\t", str(cards[i].id).zfill(2), "\t",
                      cards[i].price, "\t\t", cards[i].description)

    def show_all_cards_console(self):
        self.show_cards_console(self.cards)
