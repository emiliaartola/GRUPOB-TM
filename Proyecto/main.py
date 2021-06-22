import random, time
from player import *

playercount = int(input("Poné la cantidad de jugadores: "))
jugadornumero = []
for i in range(playercount + 1):
    jugadornumero.append(Player(i))
# Inicializacion del modulo
pygame.init()
font = pygame.font.Font("Japanese Robot.ttf", 20)

# Crea la pantalla
X = (1600)
Y = (1000)
pantalla = pygame.display.set_mode((X, Y))

# Colores pantalla

blanco = (255, 255, 255)
negro = (0, 0, 0)
naranja = (255, 165, 0)
plateado = (192, 192, 192)
rojo = (200, 0, 0)
amarillo = (227, 158, 31)
azul = (30, 150, 249)
# Titulo y icono

pygame.display.set_caption("King of Tokyo")
icono = pygame.image.load('TokyioIcon.png')
pygame.display.set_icon(icono)

# Tablero
tableroimg = pygame.image.load('Tokyo_Tablero2.png')


def tablero():
    pantalla.blit(tableroimg, (315, 17))


# Dados

cara = 6
cara_png = []

global ultimoroll
global ultimoroll2
global ultimoroll3
ultimoroll = random.randint(0, 5)
ultimoroll2 = random.randint(0, 5)
ultimoroll3 = random.randint(0, 5)
for i in range(1, cara + 1):
    cara_png.append(pygame.image.load('Cara' + str(i) + '.png'))

turnojugador = 1




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

def turnos():
    pass

player_img = []
for i in range(0, 4):
    tempimg = pygame.image.load("carta" + str(i) + ".png").convert_alpha()
    w, h = tempimg.get_size()
    tempimg = pygame.transform.smoothscale(tempimg, (int(w / 4), int(h / 4)))
    player_img.append(tempimg)

def pantalla_printall(playernumber):
    jugador = jugadornumero[playernumber]
    vida = jugador.lives
    pvictoria = jugador.victoryPoints
    energia = jugador.energy
    posicionesgrals = [(75, 100), (75, 500), (1325, 100), (1325, 500)]
    vidatext = font.render(str(vida), True, rojo)
    pvictext = font.render(str(pvictoria), True, azul)
    energtext = font.render(str(energia), True, amarillo)
    pantalla.blit(player_img[playernumber], (posicionesgrals[playernumber][0], posicionesgrals[playernumber][1]))
    pantalla.blit(vidatext, (posicionesgrals[playernumber][0] + 100 / 4, posicionesgrals[playernumber][1] + 1255 / 4))
    pantalla.blit(energtext, (posicionesgrals[playernumber][0] + 660 / 4, posicionesgrals[playernumber][1] + 1255 / 4))
    pantalla.blit(pvictext, (posicionesgrals[playernumber][0] + 115 / 4, posicionesgrals[playernumber][1] + 148 / 4))


def printearcartas():
    if int(playercount) == 2:
        pantalla_printall(0)
        pantalla_printall(2)
    if int(playercount) == 3:
        pantalla_printall(0)
        pantalla_printall(1)
        pantalla_printall(2)
    if int(playercount) == 4:
        pantalla_printall(0)
        pantalla_printall(1)
        pantalla_printall(2)
        pantalla_printall(3)


# Botones
botonreal_png = pygame.image.load("botonreal.png")
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
        printearcartas()
        pantalla.blit(cara_png[ultimoroll - 1], (boton))
        pantalla.blit(cara_png[ultimoroll2 - 1], (boton2))
        pantalla.blit(cara_png[ultimoroll3 - 1], (boton3))
        if event.type == pygame.QUIT:
            bandera = False
            pygame.quit()

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
    printearcartas()
    pantalla.blit(botonreal_png, (botonreal))
    pantalla.blit(cara_png[ultimoroll - 1], (boton))
    pantalla.blit(cara_png[ultimoroll2 - 1], (boton2))
    pantalla.blit(cara_png[ultimoroll3 - 1], (boton3))

    pygame.display.update()
