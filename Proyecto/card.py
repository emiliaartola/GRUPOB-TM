class Card:

    last_id = 0

    def __init__(self, price, description, image):
        Card.last_id += 1
        self.id = Card.last_id
        self.price = price
        self.description = description
        self.image = image
        self.used = False

    def action(self):
        self.used = True


class CardRepository:

    def __init__(self):
        self.cards = [
            Card(4, 'Tu vida maxima se incrementa en 2 y ganas 2 de vida', ''),
            Card(4, 'Si alguien muere ganas 3 puntos de victoria', ''),
            Card(5, 'Ganás 2 puntos de victoria y entrás en Tokyo ', ''),
            Card(3, 'Le haces 2 de daño a tus oponentes', ''),
            Card(2, 'Ganas 1 punto de victoria', ''),
            Card(4, 'Recuperas 4 de vida', '')
        ]



