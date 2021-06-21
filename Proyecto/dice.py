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
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.render('preparando', 0, 0)
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()