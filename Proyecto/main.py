import pygame, random, time


# Inicializacion del modulo
pygame.init()

# crea la pantalla
pantalla = pygame.display.set_mode((1100, 800))

# Titulo y icono
pygame.display.set_caption("King of Tokyo")
icono = pygame.image.load("Recursos/TokyioIcon.jpg")
pygame.display.set_icon(icono)

# Tablero
tableroimg = pygame.image.load('Recursos/Tablero.jpg')


def tablero():
    pantalla.blit(tableroimg, (300, 125))


# Dados

cara = 3
cara_png = []
global ultimoroll
ultimoroll = 0
for i in range(1, cara + 1):
    cara_png.append(pygame.image.load('Recursos/Cara' + str(i) + '.png'))


def rolldados():
    global ultimoroll
    check = 0
    for i in range(10):

        temp = random.randint(1, cara)
        if temp == check:
            temp = random.randint(1, cara)
        pantalla.blit(cara_png[temp - 1], (315, 635))
        time.sleep(0.07)
        ultimoroll = temp
        pygame.display.update()
        check = temp

# Colores pantalla

blanco = (255, 255, 255)
negro = (0, 0, 0)
naranja = (255, 165, 0)
plateado = (192, 192, 192)

# Boton

boton = pygame.Rect(315, 635, 85, 85)

# Ejecucion del juego

bandera = True

while bandera:

    pantalla.fill(plateado)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if boton.collidepoint(mouse_pos):
            tablero()
            rolldados()

    pantalla.fill(pygame.Color("Black"), boton)
    pantalla.blit(cara_png[ultimoroll-1], (boton))
    tablero()

    pygame.display.update()

