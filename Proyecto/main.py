import pygame, random, time


# Inicializacion del modulo
pygame.init()
font = pygame.font.SysFont("Japanese Robot", 20)
# crea la pantalla
pantalla = pygame.display.set_mode((1600, 1000))

# Titulo y icono

pygame.display.set_caption("King of Tokyo")
icono = pygame.image.load('TokyioIcon.png')
pygame.display.set_icon(icono)

# Tablero
tableroimg = pygame.image.load('Tokyo_Tablero2.png')


def tablero():
    pantalla.blit(tableroimg, (315, 17))


# Dados

cara = 5
cara_png = []

global ultimoroll
global ultimoroll2
global ultimoroll3
ultimoroll = random.randint(0,5)
ultimoroll2 = random.randint(0,5)
ultimoroll3 = random.randint(0,5)
for i in range(1, cara + 1):
    cara_png.append(pygame.image.load('Cara' + str(i) + '.png'))


def rolldados():
    global ultimoroll
    check = 0
    temp = random.randint(1, cara)
    pantalla.blit(cara_png[temp - 1], (715, 835))
    for i in range(10):
        if temp == check:
            temp = random.randint(1, cara)
        pantalla.blit(cara_png[temp - 1], (715, 835))
        time.sleep(0.07)
        ultimoroll = temp
        pygame.display.update()
        check = temp
def rolldados2():
    global ultimoroll2
    check = 0
    temp = random.randint(1, cara)
    pantalla.blit(cara_png[temp - 1], (815, 835))
    for x in range(10):
        if temp == check:
            temp = random.randint(1, cara)
        pantalla.blit(cara_png[temp - 1], (815, 835))
        time.sleep(0.07)
        ultimoroll2 = temp
        pygame.display.update()
        check = temp
def rolldados3():
    global ultimoroll3
    check = 0
    temp = random.randint(1, cara)
    pantalla.blit(cara_png[temp - 1], (915, 835))
    for x in range(10):
        if temp == check:
            temp = random.randint(1, cara)
        pantalla.blit(cara_png[temp - 1], (915, 835))
        time.sleep(0.07)
        ultimoroll3 = temp
        pygame.display.update()
        check = temp
# Colores pantalla

blanco = (255, 255, 255)
negro = (0, 0, 0)
naranja = (255, 165, 0)
plateado = (192, 192, 192)

# Botones
botonreal_png=pygame.image.load("botonreal.png")
botonreal = pygame.Rect(615, 835, 63, 65)
boton = pygame.Rect(715, 835, 63, 65)
boton2 = pygame.Rect(815, 835, 63, 65)
boton3 = pygame.Rect(915, 835, 63, 65)

# Ejecucion del juego

bandera = True

while bandera:

    pantalla.fill(plateado)

    for event in pygame.event.get():
        pantalla.blit(botonreal_png, (botonreal))
        pantalla.blit(cara_png[ultimoroll - 1], (boton))
        pantalla.blit(cara_png[ultimoroll2 - 1], (boton2))
        pantalla.blit(cara_png[ultimoroll3 - 1], (boton3))
        if event.type == pygame.QUIT:
            bandera = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if botonreal.collidepoint(mouse_pos):
            tablero()
            pantalla.blit(botonreal_png, (botonreal))
            pantalla.blit(cara_png[ultimoroll - 1], (boton))
            pantalla.blit(cara_png[ultimoroll2 - 1], (boton2))
            pantalla.blit(cara_png[ultimoroll3 - 1], (boton3))
            rolldados()
            rolldados2()
            rolldados3()
    tablero()
    pantalla.blit(botonreal_png, (botonreal))
    pantalla.blit(cara_png[ultimoroll-1], (boton))
    pantalla.blit(cara_png[ultimoroll2-1], (boton2))
    pantalla.blit(cara_png[ultimoroll3-1], (boton3))

    pygame.display.update()