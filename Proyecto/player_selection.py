import pygame
import game
import player
from menu import *
from player import *
import dice


class PlayerSelection:
    players = []

    def __init__(self, game):
        self.game = game
        self.display = self.game.display
        self.window = self.game.window
        self.run_display = True
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        # self.number_of_players= [1, 2]

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def reset_players(self):
        game.Game.number_of_players = None


class Selection(PlayerSelection):
    def __init__(self, game):
        PlayerSelection.__init__(self, game)
        self.state = "2"
        self.number2x, self.number2y = self.mid_w - 200, self.mid_h
        self.number3x, self.number3y = self.mid_w - 50, self.mid_h
        self.number4x, self.number4y = self.mid_w + 100, self.mid_h

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.render("Select", 0, 0)
            # movement= pygame.mouse.get_pos()
            # print(movement)
            self.game.draw_text('Numero de jugadores : ', 45, self.mid_w + 20, self.game.DISPLAY_H / 3, self.game.BLACK)
            self.game.draw_button('2', 40, self.number2x, self.number2y, 100, 100, self.game.BLACK, self.game.ORANGE)
            self.boton1 = pygame.Rect(self.number2x, self.number2y, 100, 100)
            self.game.draw_button('3', 40, self.number3x, self.number3y, 100, 100, self.game.BLACK, self.game.ORANGE)
            self.boton2 = pygame.Rect(self.number3x, self.number3y, 100, 100)
            self.game.draw_button('4', 40, self.number4x, self.number4y, 100, 100, self.game.BLACK, self.game.ORANGE)
            self.boton3 = pygame.Rect(self.number4x, self.number4y, 100, 100)
            self.blit_screen()
            self.check_input()

    # Ubicar el puntero
    # def move_cursor(self):
    # Para saber que hace click en el boton y se active
    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                mouse_pos = pygame.mouse.get_pos()
                # depende el numero los mando a elegir el monstruo
                if self.boton1.collidepoint(mouse_pos):
                    game.Game.number_of_players = 2
                    print(game.Game.number_of_players)
                    self.create_players()
                if self.boton2.collidepoint(mouse_pos):
                    game.Game.number_of_players = 3
                    print(game.Game.number_of_players)
                    self.create_players()
                if self.boton3.collidepoint(mouse_pos):
                    game.Game.number_of_players = 4
                    print(game.Game.number_of_players)
                    self.create_players()
            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                if event.key == pygame.K_BACKSPACE:
                    self.game.curr_menu = self.game.main_menu
                    self.game.curr_menu.display_menu()
                    self.game.playing = False
                    self.game.reset_keys()
                    self.run_display = False

    def create_players(self):
        self.run_display = False
        self.game.curr_menu = self.game.create_player
        self.game.curr_menu.display_menu()


class CreatePlayers(PlayerSelection):
    def __init__(self, game):
        PlayerSelection.__init__(self, game)
        self.number2x, self.number2y = self.mid_w - 300, self.mid_h
        self.number3x, self.number3y = self.mid_w - 50, self.mid_h
        self.number4x, self.number4y = self.mid_w + 180, self.mid_h
        self.sel1x, self.sel1y = self.mid_w - 300, self.mid_h - 100
        self.sel2x, self.sel2y = self.mid_w - 67, self.mid_h
        self.sel3x, self.sel3y = self.mid_w + 160, self.mid_h - 100
        self.sel4x, self.sel4y = self.mid_w - 300, self.mid_h + 100
        self.sel5x, self.sel5y = self.mid_w + 160, self.mid_h + 100

    def display_menu(self):

        self.m1 = pygame.image.load('Recursos/penguin.png').convert()
        self.m1 = pygame.transform.scale(self.m1, (150, 150))
        monstruo1 = Button(self.sel1x, self.sel1y, self.m1, 1, "Pinguino")

        monstruo2 = Button(self.sel2x, self.sel2y, self.m1, 1, "Kitty")
        monstruo3 = Button(self.sel3x, self.sel3y, self.m1, 1, "Alien")
        monstruo4 = Button(self.sel4x, self.sel4y, self.m1, 1, "The King")
        monstruo5 = Button(self.sel5x, self.sel5y, self.m1, 1, "Dino")
        self.run_display = True
        while self.run_display:

            self.game.render("options", 0, 0)
            self.game.draw_text(f'MODO {self.game.number_of_players} JUGADORES: ', 30, self.mid_w + 20,
                                self.mid_h - 300, self.game.BLACK)
            self.game.draw_text(f'Primero Jugador 1 , despues en orden: ', 20, self.mid_w + 20,
                                self.mid_h - 200, self.game.BLACK)
            monstruo1.draw(self.display)
            if monstruo1.clicked is True:
                self.game.draw_text('x', 150, self.sel1x + 77, self.sel1y + 82, self.game.ORANGE)
            monstruo2.draw(self.display)
            if monstruo2.clicked is True:
                self.game.draw_text('x', 150, self.sel2x + 77, self.sel2y + 82, self.game.ORANGE)
            monstruo3.draw(self.display)
            if monstruo3.clicked is True:
                self.game.draw_text('x', 150, self.sel3x + 77, self.sel3y + 82, self.game.ORANGE)
            monstruo4.draw(self.display)
            if monstruo4.clicked is True:
                self.game.draw_text('x', 150, self.sel4x + 77, self.sel4y + 82, self.game.ORANGE)
            monstruo5.draw(self.display)
            if monstruo5.clicked is True:
                self.game.draw_text('x', 150, self.sel5x + 77, self.sel5y + 82, self.game.ORANGE)
            self.blit_screen()
            self.list_in_players()
            self.check_input()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                if event.key == pygame.K_BACKSPACE:
                    game.Game.number_of_players = 0
                    Button.list.clear()
                    Button.Counting = 0
                    self.game.curr_menu = self.game.select_character
                    self.game.curr_menu.display_menu()
                    self.run_display = False
                    self.game.reset_keys()

    def list_in_players(self):
        if game.Game.number_of_players == Button.Counting:
            for monster in Button.list:
                if monster == 1:
                    p1 = Player(monster, 'Player 1', Button.list[0])
                    self.players.append(p1)
                if monster == 2:
                    p2 = Player(monster, 'Player 2', Button.list[1])
                    self.players.append(p2)
                if monster == 3:
                    p3 = player.Player(monster, 'Player 3', Button.list[2])
                    self.players.append(p3)
                if monster == 4:
                    p4 = Player(monster, 'Player 4', Button.list[3])
                    self.players.append(p4)
            # ACA SE SALE CUANDO TERMINAN DE ELEGIR LOS MONSTRUOS
            #self.run_display = False
            #game.Game.number_of_players = 0
            #Button.list.clear()
            #Button.Counting = 0


class Button():
    Counting = 0
    list = []

    def __init__(self, x, y, image, scale, monster):

        self.monster = monster
        width = image.get_width()
        height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):

        # Posicion del mouse
        pos = pygame.mouse.get_pos()
        # Si aprieta y cumple las condiciones va a desactivar el boton
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:

            # Cuantas veces aprietan el mouse y guarda al monstruo
            Button.Counting = Button.Counting + 1
            Button.list.append(self.monster)
            print(Button.Counting)
            print(Button.list)
            print(game.Game.number_of_players)
            self.clicked = True
            print('CLICKED')
            if Button.Counting == game.Game.number_of_players:
                print("IGUALES!")

        # Dibuja el boton
        surface.blit(self.image, (self.rect.x, self.rect.y))

# GUARDAR LOS MONSTRUOS EN UN OBJETO (Y CREAR OBJETO) DE CLASE PLAYER CUADNO SELECCIONAN MONSTRUO
# PASAR AL BOARD CUANDO SE TERMINA DE ELEGIR
