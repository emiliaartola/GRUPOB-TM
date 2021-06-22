import pygame, random, time
from menu import *
from game import *
from player_selection import PlayerSelection

class Dice:
    global ultimoroll
    global ultimoroll2
    global ultimoroll3
    cara = 6
    cara_png = []
    ultimoroll = random.randint(0, 5)
    ultimoroll2 = random.randint(0, 5)
    ultimoroll3 = random.randint(0, 5)
    for i in range(1, cara + 1):
            cara_png.append(pygame.image.load(f'Recursos\Cara{i}.png'))
    def __init__(self, game):
        self.game = game
        
        
    def rolldados(self):
        global ultimoroll
        check = 0
        temp = random.randint(1, self.cara)
        self.display.blit(self.cara_png[temp - 1], (715, 835))
        for i in range(10):
            if temp == check:
                temp = random.randint(1, self.cara)
            self.display.blit(self.cara_png[temp - 1], (715, 835))
            time.sleep(0.07)
            ultimoroll = temp
            pygame.display.update()
            check = temp

    def rolldados2(self):
        global ultimoroll2
        check = 0
        temp = random.randint(1, self.cara)
        self.display.blit(self.cara_png[temp - 1], (815, 835))
        for x in range(10):
            if temp == check:
                temp = random.randint(1, self.cara)
            self.display.blit(self.cara_png[temp - 1], (815, 835))
            time.sleep(0.07)
            ultimoroll2 = temp
            pygame.display.update()
            check = temp

    def rolldados3(self):
        global ultimoroll3
        check = 0
        temp = random.randint(1, self.cara)
        self.display.blit(self.cara_png[temp - 1], (915, 835))
        for x in range(10):
            if temp == check:
                temp = random.randint(1, self.cara)
            self.display.blit(self.cara_png[temp - 1], (915, 835))
            time.sleep(0.07)
            ultimoroll3 = temp
            pygame.display.update()
            check = temp

class Board(Dice):
    player_img = []
    def __init__(self,game):
        Dice.__init__(self,game)
        self.game = game
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)
        self.naranja = (255, 165, 0)
        self.plateado = (192, 192, 192)
        self.rojo = (200, 0, 0)
        self.amarillo = (227, 158, 31)
        self.azul = (30, 150, 249)
        self.X, self.Y = 1600, 1000
        self.tableroimg = pygame.image.load('Recursos\Tokyo_Tablero2.png')
    def tablero(self):
        self.display.blit(self.tableroimg, (315, 17))
    #EJECUCION tablero    
    def display_menu(self):
        self.run_display = True
        self.botonreal_png = pygame.image.load("Recursos/botonreal.png")
        self.botonreal = pygame.Rect(615, 835, 63, 65)
        self.boton = pygame.Rect(715, 835, 63, 65)
        self.boton2 = pygame.Rect(815, 835, 63, 65)
        self.boton3 = pygame.Rect(915, 835, 63, 65)
        self.font = pygame.font.Font("Recursos/Japanese Robot.ttf", 20)
        while self.run_display:
            self.display = pygame.display.set_mode((self.X, self.Y))
            self.tablero()
            self.show_monster()
            self.display.fill(self.plateado)
            for event in pygame.event.get():
                self.display.blit(self.botonreal_png, (self.botonreal))
                self.printearcartas()
                self.display.blit(self.cara_png[ultimoroll - 1], (self.boton))
                self.display.blit(self.cara_png[ultimoroll2 - 1], (self.boton2))
                self.display.blit(self.cara_png[ultimoroll3 - 1], (self.boton3))
                if event.type == pygame.QUIT:
                    bandera = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.botonreal.collidepoint(mouse_pos):
                    self.tablero()
                    self.display.blit(self.botonreal_png, (self.botonreal))
                    self.display.blit(self.cara_png[ultimoroll - 1], (self.boton))
                    self.display.blit(self.cara_png[ultimoroll2 - 1], (self.boton2))
                    self.display.blit(self.cara_png[ultimoroll3 - 1], (self.boton3))
                    self.rolldados()
                    self.rolldados2()
                    self.rolldados3()
            self.tablero()
            self.printearcartas()
            self.display.blit(self.botonreal_png, (self.botonreal))
            self.display.blit(self.cara_png[ultimoroll - 1], (self.boton))
            self.display.blit(self.cara_png[ultimoroll2 - 1], (self.boton2))
            self.display.blit(self.cara_png[ultimoroll3 - 1], (self.boton3))
            pygame.display.update()
    def show_monster(self): 
        for i in range(0, 4):
            tempimg = pygame.image.load(f"Recursos/carta{i}.png").convert_alpha()
            w, h = tempimg.get_size()
            tempimg = pygame.transform.smoothscale(tempimg, (int(w / 4), int(h / 4)))
            self.player_img.append(tempimg)
    def pantalla_printall(self,playernumber):
        jugador = PlayerSelection.players[playernumber]
        vida = jugador.lives
        pvictoria = jugador.victoryPoints
        energia = jugador.energy
        posicionesgrals = [(75, 100), (75, 500), (1325, 100), (1325, 500)]
        vidatext = self.font.render(str(vida), True, self.rojo)
        pvictext = self.font.render(str(pvictoria), True, self.azul)
        energtext = self.font.render(str(energia), True, self.amarillo)
        self.display.blit(self.player_img[playernumber], (posicionesgrals[playernumber][0], posicionesgrals[playernumber][1]))
        self.display.blit(vidatext, (posicionesgrals[playernumber][0] + 100 / 4, posicionesgrals[playernumber][1] + 1255 / 4))
        self.display.blit(energtext, (posicionesgrals[playernumber][0] + 660 / 4, posicionesgrals[playernumber][1] + 1255 / 4))
        self.display.blit(pvictext, (posicionesgrals[playernumber][0] + 115 / 4, posicionesgrals[playernumber][1] + 148 / 4))
    def printearcartas(self):
        if int(self.game.number_of_players) == 2:
            self.pantalla_printall(0)
            self.pantalla_printall(1)
        if int(self.game.number_of_players) == 3:
            self.pantalla_printall(0)
            self.pantalla_printall(1)
            self.pantalla_printall(2)
        if int(self.game.number_of_players) == 4:
            self.pantalla_printall(0)
            self.pantalla_printall(1)
            self.pantalla_printall(2)
            self.pantalla_printall(3)
