from constantes import *
from naveEnemiga import NaveEnemiga
from random import randint
# from main import *


def setear_personaje(NavePrincipal):
    personajePrincipal = NavePrincipal(NAVE["vida"], NAVE["daño"], NAVE["velocidad"],
                                       NAVE["velocidadTiro"], NAVE["imagen"], NAVE["imagen_disparo"], NAVE["imagen_corazon"], NAVE["imagen_corazon_vacio"], NAVE["x"], NAVE["y"], NAVE["modificador_h"], NAVE["vidas"])
    return personajePrincipal


def setear_personaje_enemigo(NaveEnemiga):
    coordenada_x = ANCHO_VENTANA + NAVES_E[4]["imagen"].get_width() + 20
    coordenada_y = randint(0, LARGO_VENTANA -
                           NAVES_E[4]["imagen"].get_height())
    enemigo = NaveEnemiga(NAVES_E[4]["vida"], NAVES_E[4]["daño"], NAVES_E[4]["velocidad"],
                          NAVES_E[4]["velocidadTiro"], NAVES_E[4]["imagen"], NAVES_E[4]["imagen_disparo"], coordenada_x, coordenada_y, NAVE["modificador_h"], NAVES_E[4]["moviendose"], ANCHO_VENTANA - NAVES_E[4]["imagen"].get_height(),  coordenada_y)
    return enemigo


def manejar_disparos(pantalla, entorno, tiempo_actual):
    for item in entorno.lista_disparos:
        item.mover()
        item.dibujar(pantalla)
        if item.checkear_visibilidad(ANCHO_VENTANA) == False:
            entorno.lista_disparos.remove(item)
        flag = True
        for enemigo in entorno.lista_enemigos:

            if enemigo.comprobar_colision(item.rect) and flag and item.es_enemigo == False:
                try:
                    entorno.lista_disparos.remove(item)
                except ValueError:
                    print("ahi fallo")
                enemigo.restar_vida(entorno.personajePrincipal.daño)
                enemigo.actualizar_rectangulo_vida(pantalla)
                flag = False
                if enemigo.vida < 1:
                    entorno.lista_enemigos.remove(enemigo)
                    nuevo_enemigo = randint(0, len(NAVES_E) - 1)
                    coordenada_x = ANCHO_VENTANA + \
                        NAVES_E[nuevo_enemigo]["imagen"].get_width() + 20
                    coordenada_y = randint(0, LARGO_VENTANA -
                                           NAVES_E[nuevo_enemigo]["imagen"].get_height())
                    nueva_nave_enemiga = NaveEnemiga(NAVES_E[nuevo_enemigo]["vida"], NAVES_E[nuevo_enemigo]["daño"], NAVES_E[nuevo_enemigo]["velocidad"],
                                                     NAVES_E[nuevo_enemigo]["velocidadTiro"], NAVES_E[nuevo_enemigo]["imagen"], NAVES_E[nuevo_enemigo]["imagen_disparo"], coordenada_x, coordenada_y, NAVE["modificador_h"], NAVES_E[nuevo_enemigo]["moviendose"], ANCHO_VENTANA - NAVES_E[nuevo_enemigo]["imagen"].get_height(),  coordenada_y)
                    entorno.lista_enemigos.append(nueva_nave_enemiga)
                    entorno.puntaje.sumar_bonus_enemigo()
                    entorno.puntaje.actualizar_texto(entorno.fuente)

        if entorno.personajePrincipal.comprobar_colision(item.rect) and item.es_enemigo == True and entorno.contadores.poder_recibir_disparos == True:
            entorno.contadores.no_recibir_disparos(tiempo_actual, 2000)
            if entorno.personajePrincipal.vidas > 1:
                entorno.sonido_disparo_recibido.play()
            entorno.personajePrincipal.restar_vidas()
            try:
                entorno.lista_disparos.remove(item)
            except ValueError:
                print("ahi fallo")


def manejar_moviimento_enemigos(lista_enemigos: list, pantalla):
    for item in lista_enemigos:
        item.generar_coordenadas(LARGO_VENTANA, ANCHO_VENTANA)
        item.mover(pantalla)
        item.comprobar_coordenada()


def manejar_teclas(pg, personajePrincipal):
    lista_teclas = pg.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pg.K_UP]:
            personajePrincipal.moverAriiba()
        if lista_teclas[pg.K_DOWN]:
            personajePrincipal.moverAbajo(LARGO_VENTANA)


def manejar_movimiento_pantalla(background, pantalla, x):
    x_relativa = x % background.get_rect().width
    pantalla.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa < ANCHO_VENTANA:
        pantalla.blit(background, (x_relativa, 0))
    # x -= 10


def resetear_juego(NavePrincipal, fuente, NaveEnemiga, Score, Contadores):
    global puntaje
    global lista_disparos
    global lista_enemigos
    global contadores
    global personajePrincipal

    personajePrincipal = NavePrincipal(NAVE["vida"], NAVE["daño"], NAVE["velocidad"],
                                       NAVE["velocidadTiro"], NAVE["imagen"], NAVE["imagen_disparo"], NAVE["imagen_corazon"], NAVE["imagen_corazon_vacio"], NAVE["x"], NAVE["y"], NAVE["modificador_h"], NAVE["vidas"])
    lista_disparos = []
    lista_enemigos = []
    puntaje.resetear_score(fuente)
    contadores.resetear_contadores(
        lista_disparos, personajePrincipal, lista_enemigos)

    # background = pg.image.load("galaxian/images/background.jpg").convert()
    # background = pg.transform.scale(background, (ANCHO_VENTANA, LARGO_VENTANA))

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

    # segundos = 1
    # medio_Segundos = 0.5
