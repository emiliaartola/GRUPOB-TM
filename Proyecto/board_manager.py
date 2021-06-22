from dice_manager import DiceManager


class BoardManager:

    def __init__(self, players):
        self.players = players
        self.playersInside = []
        self.playersOutside = []
        self.playersOutside = players
        self.diceManager = DiceManager()
        self.currentPlayerIndex = 0

        self.currentPlayer = self.players[0]

    def start_turn(self):

        self.currentPlayer = self.players[self.currentPlayerIndex]

#mover el jugador al centro si no hay nadie
        if len(self.playersInside) == 0:
            self.playersInside.append(self.currentPlayer)
            self.playersOutside.remove(self.currentPlayer)

    def finish_turn(self):
#mover pasar al siguiente player
        self.currentPlayerIndex += 1
        if self.currentPlayerIndex >= len(self.players):
            self.currentPlayerIndex = 0
        




