# HACIENDO COLISIONES CON OBJETOS

# Importar librerias
import sys
from turtle import pos # Proporciona algunas funciones del sistema
import pygame # Libreria para crear algunos juegos
from random import randint # Generar numeros aleatorios
from pygame.locals import * # Importar todas las funcionalidades de pygame
from pynput import keyboard as kb # Deteccion de teclas

# Inicializar libreria (no aplica para todas)
pygame.init()

# Capturador de teclas
def pulsa(tecla):
	print("El usuario presiono la tecla " + str(tecla))

# Crear una ventana independiente
ventana = pygame.display.set_mode((600, 700)) # 400 = ancho, 300 = alto

# Crear un titulo para la ventana
pygame.display.set_caption("Mi primer juego")

# Dandole color al fondo de la ventana
Color_Fondo = (152, 251, 152)
"""
Utilizar la imagen adjunta al script o los siguientes links

https://www.calculadoraconversor.com/colores-rgb/
https://htmlcolorcodes.com/es/
""" 

# Algunos colores basicos
Negro = (0, 0 ,0)
Blanco = (255, 255, 255)
Verde = (0, 255, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Violeta = (98, 0, 255)

# Creaamos dos figuras que colisionaran
Color_Figura1 = Rojo
Color_Figura2 = Blanco

# Configurar posiciones de las figuras
posX1, posY1 = randint(1, 600), randint(1, 700)
posX2, posY2 = randint(1, 600), randint(1, 700)
lado = 50

# Crear iterador while
while True:
    ventana.fill(Color_Fondo)

    # Dibujar dos figuras
    cuadrado_1 = pygame.draw.rect(ventana, Color_Figura1, (posX1, posY1, lado, lado))
    cuadrado_2 = pygame.draw.rect(ventana, Color_Figura2, (posX2, posY2, lado, lado))

    # Deteccion de colision
    if cuadrado_1.colliderect(cuadrado_2):
        print("Vaya, acabas de chocar")

        # Cambio de posicion
        posX2, posY2 = randint(1, 600), randint(1, 700)
        cuadrado_2.left = posX2 - (lado / 2)
        cuadrado_2.top = posY2 - (lado / 2)

    # Movimiento de el primer cuadrado con el mouse
    posX1, posY1 = pygame.mouse.get_pos()
    posX1 = posX1 - 25 # mitad del limite de la figura
    posY1 = posY1 - 25 # Alternativa (Lado / 2)

    # Verificar las acciones/eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("El usuario solicito salir de la aplicacion...")
            pygame.quit() # Detener modulos del juego
            sys.exit() # Cerrar la ventana
        elif evento.type == pygame.KEYDOWN:
            with kb.Listener(pulsa) as lector: # Detctar la telca seleccionada
                lector.join()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("El usuario presiono una tecla del raton")
    pygame.display.update() # Actualizar ventana independiente
    """Si se desea que la pantalla se actualice automaticamente y no por el raton
    se debe quitar una tabulacion de esta parte, para que quede afuera del ciloc For"""
