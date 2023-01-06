# JUGANDO CON OBJETOS EN PYGAME Y TECLAS

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

Color_Figura = Rojo
Velocidad_Figura = 1 # Velocidad de movimiento
Direccion = True # Detectar el camino al que se va
posX, posY = randint(1, 500), randint(1, 600)

# Crear iterador while
while True:
    ventana.fill(Color_Fondo)

    # Dibujar figura
    pygame.draw.rect(ventana, Color_Figura, (posX, posY, 50, 50))
    
    # Verificar las acciones/eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("El usuario solicito salir de la aplicacion...")
            pygame.quit() # Detener modulos del juego
            sys.exit() # Cerrar la ventana
        elif evento.type == pygame.KEYDOWN:
            with kb.Listener(pulsa) as lector: # Detctar la telca seleccionada
                lector.join()
            if evento.key == K_LEFT: # De izquierda a derecha
                posX -= Velocidad_Figura
                if posX < 0:
                    posX = 0 # Evitar que se salga del recuadro
            elif evento.key == K_RIGHT:
                posX += Velocidad_Figura
                if posX > (600 - 50):
                    posX = 600 - 50
            # Movimientos de arriba a abajo
            elif evento.key == K_UP:
                posY -= Velocidad_Figura
                if posY < 0:
                    posY = 0
            elif evento.key == K_DOWN:
                posY += Velocidad_Figura
                if posY > (700 - 50):
                    posY = 700 - 50 # Tamaño de ventana - tamaño de figura

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("El usuario presiono una tecla del raton")
    pygame.display.update() # Actualizar ventana independiente
    """Si se desea que la pantalla se actualice automaticamente y no por el raton
    se debe quitar una tabulacion de esta parte, para que quede afuera del ciloc For"""
