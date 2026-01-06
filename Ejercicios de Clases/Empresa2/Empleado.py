import csv
import random
import uuid
from pathlib import Path

from Persona import Persona
class Empleado(Persona):
    def __init__(self, dni, nombre, fechaNacimiento, idEmpleado, salarioMensual):
        super().__init__(dni, nombre, fechaNacimiento)
        self.idEmpleado = idEmpleado
        if salarioMensual <= 0:
            raise ValueError(f"El salario introducido '{salarioMensual}' no puede ser inferior a 0")
        else:
            self.salarioMensual = salarioMensual

    @classmethod
    def aleatorio(cls):
        path = Path("../Datos_CSV_exportables/E1_Empleado.csv")
        persona = super().aleatorio()
        idEmpleado = uuid.uuid4().hex
        salarioMensual = cls.generaSalarioAleatorio(path)
        return Empleado(persona.dni, persona.nombre, persona.fechaNacimiento, idEmpleado, salarioMensual)

    @classmethod
    def generaSalarioAleatorio(self, file_path):
        salarios = set()
        with file_path.open("r", encoding="utf-8") as f:
            empleados = csv.DictReader(f)
            for empleado in empleados:
                salarios.add(empleado.get("salarioBaseMensual"))

            return int(random.choice(list(salarios)))


    def getSalarioMensual(self):
        return self.salarioMensual

    def setSalarioMensual(self, salarioMensual):
        if salarioMensual >= 0:
            self.salarioMensual = salarioMensual
        else:
            raise ValueError(f"El salario introducido '{salarioMensual} no puede ser inferior a 0")

    def calcularCosteMensual(self):
        return self.salarioMensual

    def __str__(self):
        return f"{super().__str__()}, IdEmpleado: {self.idEmpleado}, Salario Mensual: {self.salarioMensual}"

def main():
    empleado = Empleado.aleatorio()
    print(empleado)

if __name__ == "__main__":
    main()