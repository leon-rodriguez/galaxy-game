import pygame as pg
from utilidades import *
from constantes import *
from baseDeDatos import BaseDeDatos
from entorno import Entorno

# seteos generales
pg.init()
pg.mixer.init(frequency=44100)

baseDeDatos = BaseDeDatos()
baseDeDatos.crear_tabla()
entorno = Entorno()
entorno.inicializar_juego()
pantalla = pg.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pg.display.set_caption("GALACTIC ODDYSEY")

clock = pg.time.Clock()

background = pg.image.load("galaxian/images/background.jpg").convert()
background = pg.transform.scale(background, (ANCHO_VENTANA, LARGO_VENTANA))

while entorno.flag_correr:

    if entorno.flag_estado_juego == ESTADO_INICIAL:
        entorno.correr_inicio(pantalla)

    if entorno.flag_estado_juego == ESTADO_JUGANDO:
        entorno.correr_juego(pantalla, baseDeDatos, background)

    if entorno.flag_estado_juego == ESTADO_FINAL:
        entorno.correr_final(pantalla, baseDeDatos)

    clock.tick(FPS)
    pg.display.flip()
pg.quit


# TODO sonidos
# TODO animacion aparicion de personajes
