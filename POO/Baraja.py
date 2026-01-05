"""
clase baraja y clase carta.
Carta: valor, palo(tipo)
Baraja: lista o Conjunto de Cartas(coleccion de cartas).
 Un metodo de barajar y creo que no dijo nada más (shuffle)
"""
import random

from POO.Carta import Carta


class Baraja():
    def __init__(self):
        conjunto_cartas = set()
        while len(conjunto_cartas) != 40:
            conjunto_cartas.add(Carta())
        self.mazo = list(conjunto_cartas)

    def barajar(self):
        random.shuffle(self.mazo)
        return self.mazo

    def __str__(self):
        return f"{self.mazo} | "

    def __repr__(self):
        return f"{self.mazo}"



