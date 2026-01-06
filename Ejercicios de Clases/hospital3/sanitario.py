import csv
import random
from pathlib import Path
from persona import Persona
from enum import Enum
from enum import Enum

class Area_hospital(Enum):
    UCI = "UCI"
    URGENCIAS = "URGENCIAS"
    RADIOLOGIA = "RADIOLOGIA"
    QUIROFANO = "QUIROFANO"

class Sanitario(Persona):
    def __init__(self, dni, nombre, fechaNacimiento, numColegiado, area):
        super().__init__(dni, nombre, fechaNacimiento)
        self.numColegiado = numColegiado
        self.area = area

    @classmethod
    def aleatorio(cls):
        persona = super().aleatorio()
        path = Path("../Datos_CSV_exportables/E2_Sanitario.csv")
        lst_numColegiado = set()

        with path.open("r", encoding="utf-8") as f:
            data = csv.DictReader(f)
            for fila in data:
                lst_numColegiado.add(fila.get("numColegiado"))

        return Sanitario(persona.dni,
                  persona.nombre,
                  persona.fechaNacimiento,
                  random.choice(list(lst_numColegiado)),
                  random.choice(list(Area_hospital)).value)

    def __str__(self):
        return f"{super().__str__()}, Número de Colegiado: {self.numColegiado}, Área: {self.area}"

def main():
    sanitario = Sanitario.aleatorio()
    print(sanitario)

if __name__ == "__main__":
    main()