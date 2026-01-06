import random
from enum import Enum
from Persona import Persona
class Grupo(Enum):
    _1A = "1A"
    _1B = "1B"
    _1C = "1C"
    _2A = "2A"
    _2B = "2B"
    _2C = "2C"
    _3A = "3A"
    _3B = "3B"
    _3C = "3C"
    _4A = "4A"
    _4B = "4B"
    _4C = "4C"
    _1A_Bach = "1A_BACH"
    _1B_Bach = "1B_BACH"
    _1C_Bach = "1C_BACH"
    _2A_Bach = "2A_BACH"
    _2B_Bach = "2B_BACH"
    _2C_Bach = "2C_BACH"

class Alumno(Persona):
    def __init__(self, dni, nombre, fechaNacimiento, grupo, notaMedia):
        super().__init__(dni, nombre, fechaNacimiento)
        try:
            self.grupo = Grupo(grupo)
        except ValueError:
            raise ValueError(f"El grupo {grupo} no existe")

        if not 10.0 >= notaMedia >= 0.0:
            raise ValueError(f"La nota media {notaMedia} está fuera de rango.")
        else:
            self.notaMedia = notaMedia

    @classmethod
    def aleatorio(cls):
        persona = super().aleatorio()
        grupo = random.choice(list(Grupo))
        notaMedia = random.randint(0, 10)
        return Alumno(persona.dni, persona.nombre, persona.fechaNacimiento, grupo, notaMedia)

    def getGrupo(self):
        return self.grupo

    def getNotaMedia(self):
        return self.notaMedia

    def __str__(self):
        return f"{super().__str__()}, Grupo: {self.grupo}, Nota Media: {self.notaMedia}"


def main():
    alumno = Alumno.aleatorio()
    print(alumno)
if __name__ == "__main__":
    main()