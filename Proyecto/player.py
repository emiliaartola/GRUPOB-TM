import pygame
from menu import *
from game import *
class Player:
    def __init__(self, id, name, monster_name):
        self.id = id
        self.name = name
        self.monster = monster_name
        self.lives = 10
        self.energy = 0
        self.victoryPoints = 0
        self.cards = []
        
    def __repr__(self):
        return self.name
    def sayHi(self):
        print("HIIIIIII")