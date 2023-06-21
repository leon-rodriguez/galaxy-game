import pygame as pg


def cargar_imagen(path, rotacion):
    imagen = pg.image.load(
        path)
    imagen = pg.transform.rotate(imagen, rotacion)
    return imagen


def cargar_imagen_corazon(path):
    corazon = pg.image.load(path)
    corazon = pg.transform.scale(corazon, (30, 30))
    return corazon


MOVIMIENTO_PERSONAJE = 8
MOVIMIENTO_ENEMIGO = 3
COLOR_PANTALLA = (255, 155, 155)
BLANCO = (255, 255, 255)
ANCHO_VENTANA = 1200
LARGO_VENTANA = 800
FPS = 60
ANCHO_TABLA = 500
ALTO_FILA = 60
MITAD_PANTALLA = ANCHO_VENTANA / 2
ESTADO_INICIAL = 1
ESTADO_JUGANDO = 2
ESTADO_FINAL = 3

# valores de inicio de la nave que manjeas
NAVE = {
    "vida": 100,
    "daño": 1,
    "velocidad": 1,
    "velocidadTiro": 400,
    "imagen": cargar_imagen("galaxian/images/naves/personaje_principal.png", -90),
    "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_personaje_principal.png", -90),
    "imagen_corazon": cargar_imagen_corazon("galaxian/images/corazon.png"),
    "imagen_corazon_vacio": cargar_imagen_corazon("galaxian/images/corazon_vacio.png"),
    "x": 0,
    "y": LARGO_VENTANA / 2,
    "modificador_h": -40,
    "vidas": 5
}

# valores con los que inician los 6 tipos de enemigo
NAVES_E = [
    # NAVE 1
    {
        "vida": 3,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 1100,
        "imagen": cargar_imagen("galaxian/images/naves/nave1.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave1.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
    # NAVE 3
    {
        "vida": 4,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 1600,
        "imagen": cargar_imagen("galaxian/images/naves/nave3.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave3.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
    # NAVE 4
    {
        "vida": 2,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 2500,
        "imagen": cargar_imagen("galaxian/images/naves/nave4.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave4.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
    # NAVE 5
    {
        "vida": 4,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 2200,
        "imagen": cargar_imagen("galaxian/images/naves/nave5.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave5.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
    # NAVE 7
    {
        "vida": 2,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 1000,
        "imagen": cargar_imagen("galaxian/images/naves/nave7.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave7.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
    # NAVE 11
    {
        "vida": 6,
        "daño": 1,
        "velocidad": 1,
        "velocidadTiro": 4000,
        "imagen": cargar_imagen("galaxian/images/naves/nave11.png", 90),
        "imagen_disparo": cargar_imagen("galaxian/images/disparos/disparo_nave11.png", 90),
        "modificador_h": 20,
        "moviendose": True,
    },
]
