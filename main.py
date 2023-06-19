import pygame as pg
from utilidades import *
from disapro import Disparo
from naveEnemiga import NaveEnemiga
from navePrincipal import NavePrincipal
from constantes import *
from score import Score
from contadores import Contadores
from baseDeDatos import BaseDeDatos

baseDeDatos = BaseDeDatos()
baseDeDatos.crear_tabla()

x = 0
lista_disparos = []
lista_enemigos = []
texto_usuario = ""


def correr_inicio():

    global flag_estado_juego
    global flag_correr
    global texto_usuario

    boton_start = pg.image.load("galaxian/images/boton_start.png")
    boton_start = pg.transform.scale(boton_start, (260, 120))
    rect_boton_start = pg.Rect(
        ANCHO_VENTANA / 2 - boton_start.get_width() / 2, 620, boton_start.get_width(), boton_start.get_height())

    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_correr = False
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_BACKSPACE:
                texto_usuario = texto_usuario[0:-1]
            elif len(texto_usuario) < 13:
                texto_usuario += evento.unicode
        if evento.type == pg.MOUSEBUTTONDOWN:
            if rect_boton_start.collidepoint(evento.pos) and len(texto_usuario) > 0:
                flag_estado_juego = ESTADO_JUGANDO

    input_texto = pg.Rect((ANCHO_VENTANA / 2) - (240) / 2, 400, 240, 70)
    titulo_imagen = pg.image.load("galaxian/images/titulo.png")

    texto_a_mostrar = fuente.render(texto_usuario, True, (255, 255, 255))

    pantalla.blit(titulo_imagen, ((ANCHO_VENTANA / 2) -
                                  (titulo_imagen.get_width() / 2), 30))
    pantalla.blit(boton_start, ((ANCHO_VENTANA / 2) -
                                (boton_start.get_width() / 2), 620))
    pantalla.blit(texto_a_mostrar, (input_texto.x + 10, input_texto.y + 15))
    pg.draw.rect(pantalla, (255, 255, 255), input_texto, 2)


def correr_juego():
    global x
    global flag_estado_juego
    global flag_correr

    current_time = pg.time.get_ticks()
    contadores.ciclos(current_time, puntaje, fuente)

    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_correr = False
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_SPACE and contadores.poder_disparar == True:
                disparo = Disparo(personajePrincipal.x, personajePrincipal.y,
                                  False, personajePrincipal.imagen_disparo)
                lista_disparos.append(disparo)
                contadores.cooldown_disparos(
                    current_time, personajePrincipal.velocidad_tiro)

    manejar_movimiento_pantalla(background, pantalla, x)
    x -= 4

    manejar_moviimento_enemigos(lista_enemigos, pantalla)

    manejar_teclas(pg, personajePrincipal)

    manejar_disparos(lista_disparos, pantalla, lista_enemigos,
                     personajePrincipal, puntaje, NaveEnemiga, fuente)

    personajePrincipal.dibujar_corazones(pantalla)
    personajePrincipal.dibujar(pantalla)

    for item in lista_enemigos:
        item.dibujar(pantalla)

    # print(puntaje.puntuacion)
    puntaje.dibujar_texto(pantalla)

    if personajePrincipal.vidas == 0:
        baseDeDatos.insertar_puntajes(texto_usuario, puntaje.puntuacion)
        flag_estado_juego = ESTADO_FINAL


def correr_final():
    global flag_correr
    global flag_estado_juego
    global puntaje
    global contadores
    global personajePrincipal
    global lista_enemigos
    global lista_disparos

    boton_start = pg.image.load("galaxian/images/boton_start.png")
    boton_start = pg.transform.scale(boton_start, (260, 120))
    rect_boton_start = pg.Rect(800, LARGO_VENTANA / 2 - boton_start.get_height() /
                               2, boton_start.get_width(), boton_start.get_height())

    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            flag_correr = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            if rect_boton_start.collidepoint(evento.pos):
                # resetear_juego(personajePrincipal, NavePrincipal,
                #    lista_disparos, lista_enemigos, fuente, puntaje, contadores, NaveEnemiga, Score, Contadores)
                # resetear_juego(NavePrincipal, fuente,
                #                NaveEnemiga, Score, Contadores)
                personajePrincipal = NavePrincipal(NAVE["vida"], NAVE["daño"], NAVE["velocidad"],
                                                   NAVE["velocidadTiro"], NAVE["imagen"], NAVE["imagen_disparo"], NAVE["imagen_corazon"], NAVE["imagen_corazon_vacio"], NAVE["x"], NAVE["y"], NAVE["modificador_h"], NAVE["vidas"])
                lista_disparos = []
                lista_enemigos = []
                puntaje.resetear_score(fuente)
                contadores.resetear_contadores(
                    lista_disparos, personajePrincipal, lista_enemigos)

                personajePrincipal = setear_personaje(NavePrincipal)
                primer_enemigo = setear_personaje_enemigo(NaveEnemiga)
                segundo_enemigo = setear_personaje_enemigo(NaveEnemiga)
                tercer_enemigo = setear_personaje_enemigo(NaveEnemiga)

                puntaje = Score(fuente)
                contadores = Contadores(
                    lista_disparos, personajePrincipal, lista_enemigos)

                lista_enemigos.append(primer_enemigo)
                lista_enemigos.append(segundo_enemigo)
                lista_enemigos.append(tercer_enemigo)
                flag_estado_juego = ESTADO_JUGANDO

    pantalla.fill((0, 0, 0))

    pantalla.blit(boton_start, (800, LARGO_VENTANA / 2 - boton_start.get_height() /
                                2))
    actual_puntaje_texto = fuente.render(
        "TU PUNTAJE ES: {0}".format(puntaje.puntuacion), True, BLANCO)
    pantalla.blit(actual_puntaje_texto, (100, LARGO_VENTANA / 2 - actual_puntaje_texto.get_height() /
                                         2))

    x_tabla = MITAD_PANTALLA - (ANCHO_TABLA / 2)

    titulo_tabla = pg.Rect((x_tabla, 100), (ANCHO_TABLA, ALTO_FILA))

    tabla_ordenada = baseDeDatos.devolver_tabla_ordenada()

    y_texto_linea = 180
    if len(tabla_ordenada) > 10:
        titulo = fuente.render("TOP 10 PUNTAJES", True, BLANCO)
        pantalla.blit(titulo, ((ANCHO_VENTANA / 2) -
                               (titulo.get_width() / 2), titulo_tabla.y))
        for i in range(10):
            texto_linea = "{0}: {1}".format(
                tabla_ordenada[i]["usuario"], tabla_ordenada[i]["puntaje"])
            texto_linea_a_mostrar = fuente.render(texto_linea, True, BLANCO)
            pantalla.blit(texto_linea_a_mostrar, ((ANCHO_VENTANA / 2) -
                          (texto_linea_a_mostrar.get_width() / 2), y_texto_linea))
            y_texto_linea += ALTO_FILA
    else:
        titulo = fuente.render("TOP PUNTAJES", True, BLANCO)
        pantalla.blit(titulo, ((ANCHO_VENTANA / 2) -
                               (titulo.get_width() / 2), titulo_tabla.y))
        for i in range(len(tabla_ordenada)):
            texto_linea = "{0}: {1}".format(
                tabla_ordenada[i]["usuario"], tabla_ordenada[i]["puntaje"])
            texto_linea_a_mostrar = fuente.render(texto_linea, True, BLANCO)
            pantalla.blit(texto_linea_a_mostrar, ((ANCHO_VENTANA / 2) -
                          (texto_linea_a_mostrar.get_width() / 2), y_texto_linea))
            y_texto_linea += ALTO_FILA


pg.init()

pantalla = pg.display.set_mode((ANCHO_VENTANA, LARGO_VENTANA))
pg.display.set_caption("GALACTIC ODDYSEY")

clock = pg.time.Clock()


background = pg.image.load("galaxian/images/background.jpg").convert()
background = pg.transform.scale(background, (ANCHO_VENTANA, LARGO_VENTANA))

fuente = pg.font.SysFont("Fixedsys Normal", 45)

personajePrincipal = setear_personaje(NavePrincipal)
primer_enemigo = setear_personaje_enemigo(NaveEnemiga)
segundo_enemigo = setear_personaje_enemigo(NaveEnemiga)
tercer_enemigo = setear_personaje_enemigo(NaveEnemiga)


puntaje = Score(fuente)
contadores = Contadores(
    lista_disparos, personajePrincipal, lista_enemigos)

lista_enemigos.append(primer_enemigo)
lista_enemigos.append(segundo_enemigo)
lista_enemigos.append(tercer_enemigo)


# timer_Segundos = pg.USEREVENT
# pg.time.set_timer(timer_Segundos, 1000)

segundos = 1
medio_Segundos = 0.5

flag_correr = True

ESTADO_INICIAL = 1
ESTADO_JUGANDO = 2
ESTADO_FINAL = 3

flag_estado_juego = ESTADO_INICIAL

while flag_correr:
    # lista_eventos = pg.event.get()
    # for evento in lista_eventos:
    #     if evento.type == pg.QUIT:
    #         flag_correr = False
    #     if evento.type == pg.KEYDOWN:
    #         if evento.key == pg.K_BACKSPACE:
    #             texto_usuario = texto_usuario[0:-1]
    #         else:
    #             texto_usuario += evento.unicode
    #         print(texto_usuario)
    #     if evento.type == pg.KEYDOWN:
    #         if evento.key == pg.K_x and personajePrincipal.vidas != 0:
    #             flag_estado_juego = ESTADO_JUGANDO

    if flag_estado_juego == ESTADO_INICIAL:
        correr_inicio()

    if flag_estado_juego == ESTADO_JUGANDO:
        correr_juego()

    if flag_estado_juego == ESTADO_FINAL:
        correr_final()

    clock.tick(FPS)
    pg.display.flip()
pg.quit

# barra de vida - hecho
# guardar nombre - hecho
# guardar en base de datos sql los puntajes - hecho
# ordenarlos y decir la posicion del usuario - hecho
# sonidos
# animacion aparicion de personajes
