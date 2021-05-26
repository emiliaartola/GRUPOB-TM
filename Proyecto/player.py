import pygame

from menu import *

class player:
    def __init__(self):
        self.name = ""
        self.life = 10
        self.energy = 10
        self.victory_points = 0
        self.avatar = pygame.image.load()