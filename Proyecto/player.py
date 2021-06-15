import pygame
from menu import *
class Player:
    def __init__(self, number):
        self.playerid = number
        self.lives = 10
        self.energy = 0
        self.victoryPoints = 0
    def sayHi(self):
        print("HIIIIIII")

