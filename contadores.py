import math
from disapro import Disparo


class Contadores:  # clase con la que se manejan todos los contadores del juego
    def __init__(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.segundos = 0
        self.tiempo_enemigo1 = 0
        self.tiempo_enemigo2 = 0
        self.tiempo_enemigo3 = 0
        self.lista_disparos = lista_disparos
        self.personajePrincipal = personajePrincipal
        self.lista_enemigos = lista_enemigos
        self.cooldown_nave_principal = 0
        self.poder_disparar = True
        self.delay_musica = 0
        self.seguir_ejecucion = True
        self.poder_recibir_disparos = True
        self.delay_recibir_disparos = 0

    # eb este ciclo de un segundo se suman puntajes y actualiza el texto
    def ciclo_segundos(self, puntaje, fuentes):
        self.segundos
        puntaje.sumar_bonus_tiempo()
        print(puntaje.puntuacion)
        puntaje.actualizar_texto(fuentes)

    # se sete el cooldown de disparo cada vez que el personaje principal dispara
    def cooldown_disparos(self, tiempo_actual, cooldown_de_nave_principal):
        self.cooldown_nave_principal = tiempo_actual + cooldown_de_nave_principal
        self.poder_disparar = False

    # se sete el cooldown de recibir disparo cada vez que el personaje principal recibe un disparo
    def no_recibir_disparos(self, tiempo_actual, tiempo_a_esperar):
        self.delay_recibir_disparos = tiempo_actual + tiempo_a_esperar
        self.poder_recibir_disparos = False

    def disparo_enemigo1(self):  # se maneja los tiempos de disparo de el enemigo 1
        enemigo1 = self.lista_enemigos[0]
        disparo_enemigo = Disparo(
            enemigo1.x, enemigo1.y, True, enemigo1.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def disparo_enemigo2(self):  # se maneja los tiempos de disparo de el enemigo 2
        enemigo2 = self.lista_enemigos[1]
        disparo_enemigo = Disparo(
            enemigo2.x, enemigo2.y, True, enemigo2.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def disparo_enemigo3(self):  # se maneja los tiempos de disparo de el enemigo 3
        enemigo3 = self.lista_enemigos[2]
        disparo_enemigo = Disparo(
            enemigo3.x, enemigo3.y, True, enemigo3.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def ciclos(self, ciclo, puntaje, fuentes):  # aca se manejan en tiempo todos los ciclos
        segundos_value = math.floor(ciclo / 1000)
        enemigo1_value = math.floor(
            ciclo / self.lista_enemigos[0].velocidad_tiro)
        enemigo2_value = math.floor(
            ciclo / self.lista_enemigos[1].velocidad_tiro)
        enemigo3_value = math.floor(
            ciclo / self.lista_enemigos[2].velocidad_tiro)

        if segundos_value != self.segundos:
            self.segundos = segundos_value
            self.ciclo_segundos(puntaje, fuentes)
        if enemigo1_value != self.tiempo_enemigo1:
            self.tiempo_enemigo1 = enemigo1_value
            self.disparo_enemigo1()

        if enemigo2_value != self.tiempo_enemigo2:
            self.tiempo_enemigo2 = enemigo2_value
            self.disparo_enemigo2()

        if enemigo3_value != self.tiempo_enemigo3:
            self.tiempo_enemigo3 = enemigo3_value
            self.disparo_enemigo3()

        if ciclo >= self.cooldown_nave_principal:
            self.poder_disparar = True
        if ciclo >= self.delay_musica:
            self.seguir_ejecucion = True
        if ciclo >= self.delay_recibir_disparos:
            self.poder_recibir_disparos = True

    # este metodo se usa para resetear los contadores cuando se quiere volver a jugar
    def resetear_contadores(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.segundos = 0
        self.lista_disparos = lista_disparos
        self.personajePrincipal = personajePrincipal
        self.lista_enemigos = lista_enemigos
        self.cooldown_nave_principal = 0
        self.poder_disparar = True
