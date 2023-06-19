from constantes import *
# from main import *


def setear_personaje(NavePrincipal):
    personajePrincipal = NavePrincipal(NAVE["vida"], NAVE["daño"], NAVE["velocidad"],
                                       NAVE["velocidadTiro"], NAVE["imagen"], NAVE["imagen_disparo"], NAVE["imagen_corazon"], NAVE["imagen_corazon_vacio"], NAVE["x"], NAVE["y"], NAVE["modificador_h"], NAVE["vidas"])
    return personajePrincipal


def setear_personaje_enemigo(NaveEnemiga):
    enemigo = NaveEnemiga(NAVE_E["vida"], NAVE_E["daño"], NAVE_E["velocidad"],
                          NAVE_E["velocidadTiro"], NAVE_E["imagen"], NAVE_E["imagen_disparo"], NAVE_E["x"], NAVE_E["y"], NAVE["modificador_h"], NAVE_E["moviendose"], NAVE_E["coordenada_x_final"], NAVE_E["coordenada_y_final"])
    return enemigo


def manejar_disparos(lista_disparos: list, pantalla, lista_enemigos: list, personajePrincipal, puntaje, NaveEnemiga, fuente):
    for item in lista_disparos:
        item.mover()
        item.dibujar(pantalla)
        if item.checkear_visibilidad(ANCHO_VENTANA) == False:
            lista_disparos.remove(item)
        flag = True
        for enemigo in lista_enemigos:

            if enemigo.comprobar_colision(item.rect) and flag and item.es_enemigo == False:
                lista_disparos.remove(item)
                enemigo.restar_vida(personajePrincipal.daño)
                enemigo.actualizar_rectangulo_vida(pantalla)
                flag = False
                if enemigo.vida < 1:
                    lista_enemigos.remove(enemigo)
                    lista_enemigos.append(NaveEnemiga(NAVE_E["vida"], NAVE_E["daño"], NAVE_E["velocidad"],
                                                      NAVE_E["velocidadTiro"], NAVE_E["imagen"], NAVE_E["imagen_disparo"], NAVE_E["x"], NAVE_E["y"], NAVE["modificador_h"], NAVE_E["moviendose"], NAVE_E["coordenada_x_final"], NAVE_E["coordenada_y_final"]))
                    puntaje.sumar_bonus_enemigo()
                    puntaje.actualizar_texto(fuente)

        if personajePrincipal.comprobar_colision(item.rect) and item.es_enemigo == True:
            personajePrincipal.restar_vidas()
            try:
                lista_disparos.remove(item)
            except ValueError:
                print("ahi fallo")
            if personajePrincipal.vida < 1:
                personajePrincipal.x = 0
                # personajePrincipal.y = 100


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
