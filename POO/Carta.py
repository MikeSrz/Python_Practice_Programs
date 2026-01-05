from enum import Enum
import random

#40 cartas, 7*4(tipos) => 12/40 => 30% de que salga figura
#Figuras => [10,12]
#El resto normales con valores => [1,7]
class TipoCarta(Enum):
    ORO = 0
    COPAS = 1
    ESPADAS = 2
    BASTOS = 3

class Carta:
    def __init__(self):
        if random.random() < 0.7:
            self.figura = False
        else:
            self.figura = True

        if self.figura:
                self.valor = random.randint(10,12)
                self.tipo = TipoCarta(random.randint(0,3))
        else:
                self.valor = random.randint(1,7)
                self.tipo = TipoCarta(random.randint(0,3))

    def __str__(self):
        return f"{self.tipo} = {self.valor}"

    def __repr__(self):
        return f"{self.tipo} = {self.valor}"

    def __hash__(self):
        return hash((self.tipo, self.valor))

    def __eq__(self, other):
        if not isinstance(other, Carta):
            return False
        return self.tipo == other.tipo and self.valor == other.valor

