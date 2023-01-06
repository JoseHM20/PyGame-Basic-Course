# CARGANDO IMAGENES EN NUESTRA VENTANA D EJUEGO

# Importar librerias
import sys # Proporciona algunas funciones del sistema
import pygame # Libreria para crear algunos juegos
from random import randint # Posiciones aleatorias, posiblemente para enemigos
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

Imagen = pygame.image.load("Juegos Python/michi.jpg")
# Tambien se puede utilizar una variable de posicionamiento y sustituirlo en la funcion
# posX, posY = (100, 200)

# Crear iterador while
while True:
    ventana.fill(Color_Fondo)
    ventana.blit(Imagen, (150, 300)) # Posicion de la imagen

    # Generar posiciones aletaorias
    for i in range(10):
        posX, posY = randint(1, 600), randint(1, 700)
        pygame.draw.rect(ventana, Rojo, (posX, posY, 50, 100))
    
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