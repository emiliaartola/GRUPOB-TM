import pygame


class Menu():
    def __init__(self, game):
        # Obtener variables y atributos de la clase Game
        self.game = game
        # Mitad de pantalla
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 200
        # Nos deja en el menu
        self.run_display = True
        # Acomoda el cursor del menu que va a ser un *
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    # Aqui esta dibujado

    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x - 20, self.cursor_rect.y, self.game.BLACK)

    # Actualiza la pantalla
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        # POSICIONAMIENTO DEL MENU
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    # MOSTRAR MENU
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.render("background", 0, 0)
            self.game.draw_text('Main Menu', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 230, self.game.BLACK)
            self.game.draw_text("Start Game", 30, self.startx, self.starty, self.game.BLACK)
            self.game.draw_text("Options", 30, self.optionsx, self.optionsy, self.game.BLACK)
            self.game.draw_text("Credits", 30, self.creditsx, self.creditsy, self.game.BLACK)
            self.draw_cursor()
            self.blit_screen()

    # NAVEGAR EN EL MENU
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
    # PUES COMO DICE EL NOMBRE CHEQUEA INPUTS cuando le damos enter
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

# POSICIONAMIENTO MENU OPTIONS
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30, self.game.ORANGE)
            self.game.draw_text("Volume", 15, self.volx, self.voly, self.game.ORANGE)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy, self.game.ORANGE)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # aca si queremos crear un control de volumen SI ES QUE PONEMOS MUSICA
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.render("credits", 0, 0)
            self.game.draw_text('Version digital de King of Tokyo', 35, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20, self.game.BLACK)
            self.game.draw_text('Desarrollado por : ', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50,
                                self.game.BLACK)
            self.game.draw_text('Carla Piriz', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 110,
                                self.game.BLACK)
            self.game.draw_text('Emilia Artola', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 170,
                                self.game.BLACK)
            self.game.draw_text('Franco Gozalvez', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 240,
                                self.game.BLACK)
            self.blit_screen()
