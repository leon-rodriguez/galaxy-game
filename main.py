import pygame as pg
from utilidades import *
from constantes import *
from baseDeDatos import BaseDeDatos
from entorno import Entorno

# se inicia pygame
pg.init()
pg.mixer.init(frequency=44100)

# seteos generales
baseDeDatos = BaseDeDatos()
baseDeDatos.crear_tabla()
entorno = Entorno()
entorno.inicializar_juego()
pantalla = pg.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pg.display.set_caption("GALACTIC ODDYSEY")
clock = pg.time.Clock()

# agrego el fondo del juego
background = pg.image.load("galaxian/images/background.jpg").convert()
background = pg.transform.scale(background, (ANCHO_VENTANA, LARGO_VENTANA))

while entorno.flag_correr:
    # si el juego esta en pausa se ejecuta esta funcion
    if entorno.flag_estado_juego == ESTADO_INICIAL:
        entorno.correr_inicio(pantalla)

    # si el juego esta corriendo se ejecuta esta funcion
    if entorno.flag_estado_juego == ESTADO_JUGANDO:
        entorno.correr_juego(pantalla, baseDeDatos, background)

    # si el juego ya termino se ejecuta esta funcion
    if entorno.flag_estado_juego == ESTADO_FINAL:
        entorno.correr_final(pantalla, baseDeDatos)

    # se controlan los fps y se actualiza la pantalla
    clock.tick(FPS)
    pg.display.flip()
pg.quit
