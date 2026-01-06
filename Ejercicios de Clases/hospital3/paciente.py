import csv
import random
from persona import Persona
from time import time
from datetime import datetime
from pathlib import Path

class Paciente(Persona):
    def __init__(self, dni, nombre, fechaNacimiento, numHistoria, gravedad, fechaIngreso):
        super().__init__(dni, nombre, fechaNacimiento, )
        self.numHistoria = numHistoria
        if 0 > gravedad > 5:
            raise ValueError(f"Has introducido una gravedad fuera del rango.")
        else:
            self.gravedad = gravedad
        self.fechaIngreso = fechaIngreso

    @classmethod
    def aleatorio(cls):
        paciente = super().aleatorio()
        path = Path("../Datos_CSV_exportables/E2_Paciente.csv")
        gravedades = set()
        fechas = set()
        num_hists = set()
        with path.open("r", encoding="utf-8") as f:
            data = csv.DictReader(f)
            for fila in data:
                gravedades.add(fila.get("gravedad"))
                fechas.add(fila.get("fechaIngreso"))
                num_hists.add(fila.get("numHistoria"))

        return Paciente(paciente.dni, paciente.nombre, paciente.fechaNacimiento, random.choice(list(num_hists)), int(random.choice(list(gravedades))), random.choice(list(fechas)))

    def getNumHistoria(self):
        return self.numHistoria

    def setNumHistoria(self, numHistoria):
        self.numHistoria = numHistoria

    def setGravedad(self, gravedad):
        if not 0 > gravedad > 5:
            self.gravedad = gravedad
        else:
            raise ValueError(f"Has introducido una gravedad fuera del rango.")

    def esCritico(self):
        return True if self.gravedad >= 4 else False

    def __str__(self):
        return f"{super().__str__()}, Gravedad: {self.gravedad}, Fecha Ingreso: {self.fechaIngreso}"


def main():
    pacientes = []
    for i in range(50):
        pacientes.append(Paciente.aleatorio())

    for paciente in pacientes:
        print(paciente)
if __name__ == "__main__":
    main()