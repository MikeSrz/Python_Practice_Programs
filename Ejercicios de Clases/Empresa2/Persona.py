import csv
import random
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

class Persona():
    def __init__(self, dni, nombre, fechaNacimiento):
        if fechaNacimiento is None or fechaNacimiento == "":
            raise ValueError("No se puede generar Persona sin fecha de Nacimiento")
        elif dni is None or dni == "" or len(dni) != 9:
            raise ValueError("No se puede generar Persona sin dni")
        else:
            self.dni = dni
            self.nombre = nombre
            self.fechaNacimiento = fechaNacimiento

    @classmethod
    def aleatorio(cls):
        fichero_personas = Path("../Datos_CSV_exportables/E2_Persona.csv")
        datos = cls.dni_apellido_rand(fichero_personas)
        dni = datos.get("dni")
        nombre = datos.get("nombre")
        fechaNacimiento = cls.fecha_aleatoria()
        return Persona(dni, nombre, fechaNacimiento)

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_fechaNacmiento(self):
        return self.fechaNacimiento

    def set_fechaNacimiento(self, fecha):
        self.fechaNacimiento = fecha

    def get_nombre(self):
        return self.nombre

    @classmethod
    def fecha_aleatoria(cls):
        limite_inicial = datetime(1980, 1, 1)
        diferencia = datetime(2013, 12, 31) - limite_inicial
        fecha_aleatoria = limite_inicial + timedelta(days=random.randint(0, diferencia.days))
        return fecha_aleatoria.date()

    @classmethod
    def dni_apellido_rand(cls, path):
        dnis = set()
        nombres = set()
        with path.open("r", encoding="utf-8") as f:
            datos = csv.DictReader(f)
            for fila in datos:
                dnis.add(fila["dni"])
                nombres.add(fila["nombre"])
        return {"dni": random.choice(list(dnis)), "nombre": random.choice(list(nombres))}

    def __eq__(self, other):
        if not isinstance(other, Persona):
            return False
        return self.dni == other.dni

    def __hash__(self):
        return hash(self.dni)

    def __str__(self):
        return f"Dni: {self.dni} | Nombre: {self.nombre} | Fecha Nacimiento: {self.fechaNacimiento}"


def main():
    persona = Persona.aleatorio()
    print(persona)

if __name__ == "__main__":
    main()




