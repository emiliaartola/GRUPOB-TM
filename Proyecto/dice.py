import pygame, random, time
from menu import *
from game import *

class Dice:
    def __init__(self, game):
        self.game = game
        self.faces, self.dices = [] , 3
        self.last_state = 0

    def roll_dice(self):
        for i in range(1, self.faces +1):
            self.faces.append(pygame.image.load('Cara' + str(i) + '.png'))
            self.game.display(self.faces(800,700))

class Board:
    def __init__(self,game):
        Dice.__init__(self,game)
        self.game = game
        self.display = self.game.display
        self.window = self.game.window
        self.run_display = True
    def display_board(self):
        self.game.render("credits", 0, 0)