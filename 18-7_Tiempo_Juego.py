# CONSTRUYENDO LA BASE DEL JUEGO

# Importar librerias
import sys # Proporciona algunas funciones del sistema
import pygame # Libreria para crear algunos juegos
from pygame.locals import * # Importar todas las funcionalidades de pygame
from pynput import keyboard as kb # Deteccion de teclas

# Inicializar libreria (no aplica para todas)
pygame.init()

# Capturador de teclas
def pulsa(tecla):
	print("El usuario presiono la tecla " + str(tecla))

# Crear una ventana independiente
ventana = pygame.display.set_mode((600, 600)) # 400 = ancho, 300 = alto

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

# Configurar fuente
fuente = pygame.font.SysFont("Arial", 20)
Color_Texto = Negro

# Crear iterador while
while True:
    ventana.fill(Color_Fondo)

    # Configurar el tiempo de juego
    Tiempo = pygame.time.get_ticks() / 1000 # Dividido en milisegundos
    tiempo_juego = fuente.render("Tiempo de juego: " + str(Tiempo), True, Color_Texto)

    # Imprimir el texto en pantalla
    ventana.blit(tiempo_juego, (300, 300)) # Las coordenadas se almacenan en una tupla
    
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