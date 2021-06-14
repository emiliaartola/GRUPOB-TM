import random

from player import Player


class DiceFaces:
    ONE = 1
    TWO = 2
    THREE = 3
    ENERGY = 4
    HEART = 5
    CLAW = 6


class DiceManager:
    
    def __init__(self):
        self.dice_faces = [
            DiceFaces.ONE,
            DiceFaces.TWO,
            DiceFaces.THREE,
            DiceFaces.ENERGY,
            DiceFaces.CLAW,
            DiceFaces.HEART]

    def get_random_dices(self, count):
        dices = []
        for throw_number in range(count):
            dices.append(self.dice_faces[random.randint(0, len(self.dice_faces) - 1)])
        return dices

    def apply_dices(self, dices, target_player):
        points = 0
        dice_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for dice in dices:
            dice_counter[dice] = dice_counter[dice] + 1

        if dice_counter[DiceFaces.ONE] >= 3:
            points += dice_counter[DiceFaces.ONE] - 2
        if dice_counter[DiceFaces.TWO] >= 3:
            points += dice_counter[DiceFaces.TWO] - 1
        if dice_counter[DiceFaces.THREE] >= 3:
            points += dice_counter[DiceFaces.THREE]

        energy = dice_counter[DiceFaces.ENERGY]
        health = dice_counter[DiceFaces.HEART]
        damage = dice_counter[DiceFaces.CLAW]

        print("__ JUGADA __")
        print("dados: ", dices)
        print("puntos: ", points)
        print("energia: ", energy)
        print("curación: ", health)
        print("daño: ", damage)
        print(" ")

        # ToDo usar metodos para filtrar los maximos y minimos
        target_player.lives += health
        target_player.energy += energy
        target_player.victoryPoints = points


# Pruebas
d_manager = DiceManager()
player = Player(1, "player1", "Godzilla")
# d_manager.apply_dices([1, 1, 1, 1, 1, 1], player)
# d_manager.apply_dices([1, 1, 1, 2, 2, 2], player)
# d_manager.apply_dices([1, 2, 3, 4, 5, 6], player)
# d_manager.apply_dices([2, 2, 2, 2, 1, 1], player)
# d_manager.apply_dices([3, 3, 3, 4, 5, 6], player)
# d_manager.apply_dices([3, 3, 3, 3, 3, 3], player)
# d_manager.apply_dices([5, 5, 5, 5, 5, 5], player)
# d_manager.apply_dices([6, 6, 6, 6, 4, 4], player)

# for i in range(10):
#     d_manager.apply_dices(d_manager.get_random_dices(6), player)

print("simulando jugadas")

turn_dices = d_manager.get_random_dices(6)
for j in range(2):
    print("new dices: ", turn_dices)
    n = 0
    while n < len(turn_dices):
        if turn_dices[n] != DiceFaces.CLAW:
            turn_dices.remove(turn_dices[n])
            print(turn_dices)
        else:
            n += 1

    turn_dices.extend(d_manager.get_random_dices(6-len(turn_dices)))


d_manager.apply_dices(turn_dices, player)
