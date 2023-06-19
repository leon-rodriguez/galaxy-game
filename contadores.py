import math
from disapro import Disparo


class Contadores:
    def __init__(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.secconds = 0
        self.half_secconds = 0
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

    def ciclo_segundos(self, puntaje, fuentes):
        self.secconds
        # for item in self.lista_enemigos:
        #     disparo_enemigo = Disparo(
        #         item.x, item.y, True, item.imagen_disparo)
        #     self.lista_disparos.append(disparo_enemigo)
        puntaje.sumar_bonus_tiempo()
        print(puntaje.puntuacion)
        puntaje.actualizar_texto(fuentes)

    def ciclo_500_ms(self):
        self.half_secconds
        disparo = Disparo(self.personajePrincipal.x, self.personajePrincipal.y,
                          False, self.personajePrincipal.imagen_disparo)
        self.lista_disparos.append(disparo)

    def cooldown_disparos(self, tiempo_actual, cooldown_de_nave_principal):
        self.cooldown_nave_principal = tiempo_actual + cooldown_de_nave_principal
        self.poder_disparar = False

    def delay_para_musica(self, tiempo_actual, tiempo_a_esperar):
        self.delay_musica = tiempo_actual + tiempo_a_esperar
        self.seguir_ejecucion = False

    def no_recibir_disparos(self, tiempo_actual, tiempo_a_esperar):
        self.delay_recibir_disparos = tiempo_actual + tiempo_a_esperar
        self.poder_recibir_disparos = False

    def disparo_enemigo1(self):
        enemigo1 = self.lista_enemigos[0]
        disparo_enemigo = Disparo(
            enemigo1.x, enemigo1.y, True, enemigo1.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def disparo_enemigo2(self):
        enemigo2 = self.lista_enemigos[1]
        disparo_enemigo = Disparo(
            enemigo2.x, enemigo2.y, True, enemigo2.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def disparo_enemigo3(self):
        enemigo3 = self.lista_enemigos[2]
        disparo_enemigo = Disparo(
            enemigo3.x, enemigo3.y, True, enemigo3.imagen_disparo)
        self.lista_disparos.append(disparo_enemigo)

    def ciclos(self, cicle, puntaje, fuentes):
        secconds_value = math.floor(cicle / 1000)
        ml_500_value = math.floor(cicle / 500)
        enemigo1_value = math.floor(
            cicle / self.lista_enemigos[0].velocidad_tiro)
        enemigo2_value = math.floor(
            cicle / self.lista_enemigos[1].velocidad_tiro)
        enemigo3_value = math.floor(
            cicle / self.lista_enemigos[2].velocidad_tiro)
        if secconds_value != self.secconds:
            self.secconds = secconds_value
            self.ciclo_segundos(puntaje, fuentes)
        # if ml_500_value != self.half_secconds:
            # self.half_secconds = ml_500_value
            # self.ciclo_800_ms()
        if enemigo1_value != self.tiempo_enemigo1:
            self.tiempo_enemigo1 = enemigo1_value
            self.disparo_enemigo1()

        if enemigo2_value != self.tiempo_enemigo2:
            self.tiempo_enemigo2 = enemigo2_value
            self.disparo_enemigo2()

        if enemigo3_value != self.tiempo_enemigo3:
            self.tiempo_enemigo3 = enemigo3_value
            self.disparo_enemigo3()

        if cicle >= self.cooldown_nave_principal:
            self.poder_disparar = True
        if cicle >= self.delay_musica:
            self.seguir_ejecucion = True
        if cicle >= self.delay_recibir_disparos:
            self.poder_recibir_disparos = True

    def resetear_contadores(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.secconds = 0
        self.half_secconds = 0
        self.lista_disparos = lista_disparos
        self.personajePrincipal = personajePrincipal
        self.lista_enemigos = lista_enemigos
        self.cooldown_nave_principal = 0
        self.poder_disparar = True
