from deck import Deck


class Market:
    deck = Deck()
    marketCards = []

    def __init__(self):
        # probando la lógica de la baraja del mercado en consola

        self.show_market_state()
        self.prepare_market(3)

    def show_market_state(self):
        print("__ ESTADO DEL MERCADO __")
        print("Cartas del mercado:", len(self.marketCards))
        self.deck.show_cards_console(self.marketCards)
        print("cartas en el mazo: ", len(self.deck.cards))
        print(" ")


    def buy_card(self, card):
        print("__ COMPRA_ _")
        print("Se compra la carta: #", card.id)
        print(" ")

        index = self.marketCards.index(card)
        self.marketCards.remove(card)
        self.marketCards.insert(index, self.deck.draw())

        self.show_market_state()

    def prepare_market(self, market_size):
        print("__ PREPARANDO CARTAS __")
        print("Se reparten ", market_size, " cartas")
        print(" ")

        for i in range(market_size):
            self.marketCards.append(self.deck.draw())

        self.show_market_state()


market = Market()
market.buy_card(market.marketCards[0])
market.buy_card(market.marketCards[1])
market.buy_card(market.marketCards[2])
