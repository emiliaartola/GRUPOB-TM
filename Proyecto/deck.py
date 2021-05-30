import random

from card import Card


class Deck:

    def __init__(self):
        self.cards = Card.create_cards()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) > 0:
            draw_card = self.cards[0]
            self.cards.pop(0)
            return draw_card
        else:
            return None

    def show_cards_console(self, cards_to_show):
        if len(cards_to_show)>0:
            print("#", "\t", "ID", "\t", "Price", "\t", "Description")

            for i in range(len(cards_to_show)):
                print(str(i + 1).zfill(2), "\t", str(cards_to_show[i].id).zfill(2), "\t",
                      cards_to_show[i].price, "\t\t", cards_to_show[i].description)

    def show_all_cards_console(self):
        self.show_cards_console(self.cards)
