import random

from typing_extensions import overload

from Empleado import Empleado
from enum import Enum
class Categoria(Enum):
    CTO = "CTO"
    CFO = "CFO"
    CEO = "CEO"

class Directivo(Empleado):
    def __init__(self, dni, nombre, fechaNacimiento, idEmpleado, salarioMensual, bonusAnual, categoria):
        super().__init__(dni, nombre, fechaNacimiento, idEmpleado, salarioMensual)

        if bonusAnual >= 0:
            self.bonusAnual = bonusAnual
        else:
            raise ValueError("El valor del bonus no puede ser negativo.")
        try:
            self.categoria =  Categoria(categoria)
        except:
            ValueError(f"La categoria {categoria} no existe.")

    @classmethod
    def aleatorio(cls):
        directivo = super().aleatorio()
        bonusAnual = random.randint(0, 100000)
        categoria = random.choice(list(Categoria))
        return cls(directivo.dni, directivo.nombre, directivo.fechaNacimiento, directivo.idEmpleado, directivo.salarioMensual, bonusAnual, categoria)

    @overload
    def calcularCosteMensual(self, bonusAnual):
        return self.salarioMensual + bonusAnual/12

    def __str__(self):
        return f"{super().__str__()}, Bonus Anual: {self.bonusAnual}, Categoría: {self.categoria}"

