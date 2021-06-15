import pygame
from menu import *
from dice import Board
from player_selection import Selection, CreatePlayers
from player import Player

class Game:
    number_of_players = None
    def __init__(self):
        pygame.init()
        # El juego puede estar abierto o no, y el juego puede estar abierto pero capaz no estan jugando.
        self.running, self.playing = True, False

        # Los controles empiezan en False PORQUE EL JUGADOR TODAVIA NO TOCO NINGUNA TECLA
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # Dimensiones de la pantalla
        self.DISPLAY_W, self.DISPLAY_H = 720, 740
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = 'Japanese Robot.ttf'
        pygame.display.set_caption("King of Tokyo")
        self.icono = pygame.image.load('Recursos/TokyioIcon.jpg')
        pygame.display.set_icon(self.icono)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.ORANGE = (255, 165, 0)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.select_character = Selection(self)
        self.create_player = CreatePlayers(self)
        self.board = Board(self)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()

    # Bucle del juego
    def game_loop(self):
        while self.playing:
            self.curr_menu = self.select_character
            self.curr_menu.display_menu()
            self.check_events()
            # self.render("background", 0, 0)
            # self.render("Tablero", 150, 150)
            # self.render_png('Cara1', 300, 300)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()
            self.clock.tick(30)

    # Traer los datos de lo que hace el jugador
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y, color):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        # Rectangulo donde estara el texto
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    # CAMBIO DE BACKGROUND
    def render(self, name, x, y):
        image = pygame.image.load(f'Recursos/{name}.jpg').convert()
        self.display.blit(image, (x, y))

    def render_png(self, name, x, y):
        image = pygame.image.load(f'Recursos/{name}.png').convert()
        self.display.blit(image, (x, y))

    def draw_button(self, text, font_size, x, y, width, height, color, hover):
        mouse = pygame.mouse.get_pos()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.display, hover, (x, y, width, height))
        else:
            pygame.draw.rect(self.display, color, (x, y, width, height))
        font = pygame.font.Font(self.font_name, font_size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        # se centra en la X primero
        text_rect.center = ((x + (width / 2)), (y + (height / 2)))
        self.display.blit(text_surface, text_rect)

