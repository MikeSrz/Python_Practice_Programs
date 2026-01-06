import random

from Alumno import Alumno
class AlumnoDelegado(Alumno):
    def __init__(self, dni, nombre, fechaNacimiento, grupo, notaMedia, votos, cantPalmaditasEspalda):
        super().__init__(dni, nombre, fechaNacimiento, grupo, notaMedia)
        self.votos = votos
        self.cantPalmaditasEspalda = cantPalmaditasEspalda

    @classmethod
    def aleatorio(cls):
        alumno = super().aleatorio()
        votos = random.randint(0,30)
        cantPalmaditasEspalda = random.randint(0,1)

        return AlumnoDelegado(alumno.dni, alumno.nombre, alumno.fechaNacimiento, alumno.grupo, alumno.notaMedia, votos, cantPalmaditasEspalda)

    def __str__(self):
        return f"{super().__str__()}, Votos: {self.votos}, Palmaditas: {self.cantPalmaditasEspalda}"

def main():
    delegado= AlumnoDelegado.aleatorio()
    print(delegado)
if __name__ == "__main__":
    main()