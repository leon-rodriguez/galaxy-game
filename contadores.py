import math
from disapro import Disparo


class Contadores:
    def __init__(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.secconds = 0
        self.half_secconds = 0
        self.lista_disparos = lista_disparos
        self.personajePrincipal = personajePrincipal
        self.lista_enemigos = lista_enemigos
        self.cooldown = 0
        self.poder_disparar = True

    def ciclo_segundos(self, puntaje, fuentes):
        self.secconds
        for item in self.lista_enemigos:
            disparo_enemigo = Disparo(
                item.x, item.y, True, item.imagen_disparo)
            self.lista_disparos.append(disparo_enemigo)
        puntaje.sumar_bonus_tiempo()
        print(puntaje.puntuacion)
        puntaje.actualizar_texto(fuentes)

    def ciclo_500_ms(self):
        self.half_secconds
        disparo = Disparo(self.personajePrincipal.x, self.personajePrincipal.y,
                          False, self.personajePrincipal.imagen_disparo)
        self.lista_disparos.append(disparo)

    def cooldown_disparos(self, tiempo_actual, cooldown_de_nave_principal):
        self.cooldown = tiempo_actual + cooldown_de_nave_principal
        self.poder_disparar = False

    def ciclos(self, cicle, puntaje, fuentes):
        secconds_value = math.floor(cicle / 1000)
        # ml_500_value = math.floor(cicle / 500)
        if secconds_value != self.secconds:
            self.secconds = secconds_value
            self.ciclo_segundos(puntaje, fuentes)
        # if ml_500_value != self.half_secconds:
        #     self.half_secconds = ml_500_value
            # self.ciclo_800_ms()
        if cicle >= self.cooldown:
            self.poder_disparar = True

    def resetear_contadores(self, lista_disparos, personajePrincipal, lista_enemigos):
        self.secconds = 0
        self.half_secconds = 0
        self.lista_disparos = lista_disparos
        self.personajePrincipal = personajePrincipal
        self.lista_enemigos = lista_enemigos
        self.cooldown = 0
        self.poder_disparar = True
