# DIBUJANDO LINEAS EN EL JUEGO

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

Color_Linea = Negro
Color_Circulo = Rojo
Color_Rectangulo = Azul
Color_Poligono = Violeta

# Crear iterador while
while True:
    ventana.fill(Color_Fondo)
    # DIBUJAR LINEA
    pygame.draw.line(ventana, Color_Linea, (50, 100), (100, 150), 20)

    # La funcion solicta el tamño de ventana, color de la forma,
    # posicion inicial, posicion final y grosor

    # DIBUJAR CIRCULO
    pygame.draw.circle(ventana, Color_Circulo, (100, 150), 70, 20)
    # Solo se modifica la posicion final por el radio del circulo

    # DIBUJAR RECTANGULOS
    pygame.draw.rect(ventana, Color_Rectangulo, (200, 100, 200, 100), 20)

    # DINUJAR POLIGONO
    pygame.draw.polygon(ventana, Color_Poligono, ((200, 150), (100, 50), (200, 350), (120, 70)))

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
