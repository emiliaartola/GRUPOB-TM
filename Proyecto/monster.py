import pygame
from menu import *
from game import *
from player_selection import *
class Monster:
    def __init__(self, monster_name, monster_sound):
        self.monster_name = monster_name
        self.monster_sound = monster_sound

    def get_monster_name(self):
        return self.monster_name

    def get_monster_sound(self):
        return self.monster_sound
    def list_of_monsters():
    #Cargo los monstruos que pueden jugar 
        list= []
        list.append(Monster("Alienoid", "Bleh!"))
        list.append(Monster("Cyber Kitty", "Meow."))
        list.append(Monster("Giga Zaur", "Rawr!"))
        list.append(Monster("Space Penguin", "Squeak!"))
        list.append(Monster("The King", "Grawrr"))
        return list