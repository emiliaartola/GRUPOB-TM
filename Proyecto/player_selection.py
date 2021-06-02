import pygame
from menu import *
from player import *
class PlayerSelection():
    number_of_players= [1, 2]
    players = []
    
    def __init__(self,game):
        self.game=game
        self.display = self.game.display
        self.window = self.game.window
        self.run_display = True
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2 , self.game.DISPLAY_H / 2
        #self.number_of_players= [1, 2]  
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
    def reset_players(self):
        self.number_of_players= [1, 2]
        
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
            #movement= pygame.mouse.get_pos()
            #print(movement)
            self.game.draw_text('Numero de jugadores : ', 45, self.mid_w + 20, self.game.DISPLAY_H / 3, self.game.BLACK)
            self.game.draw_button('2',40, self.number2x, self.number2y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton1 = pygame.Rect(self.number2x,self.number2y, 100, 100)
            self.game.draw_button('3',40, self.number3x, self.number3y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton2 = pygame.Rect(self.number3x,self.number3y, 100, 100)
            self.game.draw_button('4',40, self.number4x, self.number4y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton3 = pygame.Rect(self.number4x,self.number4y, 100, 100)
            self.blit_screen()
            self.check_input()
            
    #Ubicar el puntero 
    #def move_cursor(self):
    #Para saber que hace click en el boton y se active
    def check_input (self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                #depende el numero los mando a elegir el monstruo
                if self.boton1.collidepoint(mouse_pos):
                    self.create_players()    
                if self.boton2.collidepoint(mouse_pos):
                    self.number_of_players.append(3)
                    self.create_players()
                if self.boton3.collidepoint(mouse_pos):
                    self.number_of_players.append(3)
                    self.number_of_players.append(4)
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
                    self.game.playing=False
                    self.game.reset_keys()
                    self.run_display = False
                    self.reset_players()
    def create_players(self):
        self.run_display = False
        self.game.curr_menu = self.game.create_player
        self.game.curr_menu.display_menu()
    
class CreatePlayers(PlayerSelection):
    def __init__(self, game):
        PlayerSelection.__init__(self, game)
        self.sel1x, self.sel1y = self.mid_w - 300, self.mid_h - 100
        self.sel2x, self.sel2y = self.mid_w - 67, self.mid_h
        self.sel3x, self.sel3y = self.mid_w + 160, self.mid_h - 100
        self.sel4x, self.sel4y = self.mid_w - 300, self.mid_h + 100
        self.sel5x, self.sel5y = self.mid_w + 160, self.mid_h + 100
        self.number2x, self.number2y = self.mid_w - 300, self.mid_h
        self.number3x, self.number3y = self.mid_w - 50, self.mid_h
        self.number4x, self.number4y = self.mid_w + 180, self.mid_h
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.reset_keys()
            self.game.render("options", 0, 0)
            self.draw_buttons_monsters()
            self.check_input()
                   
    def draw_buttons_monsters(self):
        self.game.draw_text(f'MODO {len(self.number_of_players)} JUGADORES: ', 30, self.mid_w + 20, self.game.DISPLAY_H / 4, self.game.BLACK)
        self.game.draw_text(f' Jugador {self.number_of_players[0]} seleccione un monstruo: ', 20, self.mid_w + 20, self.game.DISPLAY_H / 3 + 20, self.game.BLACK)
        self.draw_buttons_img('penguin', self.sel1x, self.sel1y, 150,150, "X")
        self.sel1 = pygame.Rect(self.sel1x,self.sel1y, 150, 150)
        self.game.draw_button('kitty',30, self.sel2x , self.sel2y, 150,150, self.game.BLACK, self.game.ORANGE)
        self.sel2 = pygame.Rect(self.sel2x, self.sel2y, 150, 150)
        self.game.draw_button('el dino',30, self.sel3x, self.sel3y, 150,150, self.game.BLACK, self.game.ORANGE)
        self.sel3 = pygame.Rect(self.sel3x,self.sel3y, 150, 150)
        self.game.draw_button('king',30, self.sel4x, self.sel4y, 150,150, self.game.BLACK, self.game.ORANGE)
        self.sel4 = pygame.Rect(self.sel4x,self.sel4y, 150, 150)
        self.game.draw_button('alien',30, self.sel5x, self.sel5y , 150,150, self.game.BLACK, self.game.ORANGE)
        self.sel5 = pygame.Rect(self.sel5x, self.sel5y, 150, 150)
        self.blit_screen()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for x in self.number_of_players:
                    if self.sel1.collidepoint(mouse_pos):
                        print(x)
                    if self.sel2.collidepoint(mouse_pos):
                        print("CLICKKK")
                    if self.sel3.collidepoint(mouse_pos):
                        print("CLICKKK")
                    if self.sel4.collidepoint(mouse_pos):
                        print("CLICKKK")
                    if self.sel5.collidepoint(mouse_pos):
                        print("CLICKKK")
                return 

            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                if event.key == pygame.K_BACKSPACE:
                    self.game.curr_menu = self.game.select_character
                    self.game.curr_menu.display_menu()
                    self.run_display = False
                    self.game.reset_keys()
                    self.reset_players()

    def draw_buttons_img(self, name ,x, y, width, height, text ):
        button_surface = pygame.image.load(f'Recursos/{name}.png').convert()
        button_surface = pygame.transform.scale(button_surface,(150,150))
        rect = button_surface.get_rect()
        rect = rect.move((x, y))
        mouse= pygame.mouse.get_pos()
        pygame.draw.rect (button_surface, self.game.BLACK, (x,y,width,height))
        self.display.blit(button_surface, rect)
        


    ##################################################
    #### POR HACER : 
    #### COLLIDE DE LOS BOTONES ( PRIMERO ELIGE EL PLAYER 1 , DESPUES 2 Y ASI )
    #### ELIMINAR UN MONSTRUO CUANDO YA ESTA ELEGIDO
    #### OPCIONAL O AL FINAL AGREGAR SONIDOS DE MONSTRUO
    #### 
    #### GUARDAR LOS MONSTRUOS EN UN OBJETO (Y CREAR OBJETO) DE CLASE PLAYER CUADNO SELECCIONAN MONSTRUO
    #### PASAR AL BOARD CUANDO SE TERMINA DE ELEGIR
    ###################################################

