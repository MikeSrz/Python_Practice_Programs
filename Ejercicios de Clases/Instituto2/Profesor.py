import random
from Persona import Persona
from enum import Enum

class Departamento(Enum):
    INFORMATICA = "INFORMATICA"
    MATEMATICAS = "MATEMATICAS"
    BIOLOGIA = "BIOLOGIA"
    FISICA = "FISICA"
    MUSICA = "MUSICA"

class Profesor(Persona):
    def __init__(self, dni, nombre, fechaNacimiento, departamento, salarioMensual):
        super.__init__(dni, nombre, fechaNacimiento)
        if  salarioMensual > 0:
            self.salarioMensual = salarioMensual
        else:
            raise ValueError(f"El salario no puede ser 0 o negativo")
        try:
            self.departamento = Departamento(departamento.capitalize())
        except ValueError:
            raise ValueError(f"No se introdujo un departamento posible")

    @classmethod
    def aleatorio(cls):
        super().aleatorio()
        departamento = random.choice(list(Departamento))
        salarioMensual = random.randint(1000, 3000)
        return cls(
            Persona.dni,
            Persona.nombre,
            Persona.fechaNacimiento,
            departamento,  # Enum
            salarioMensual
        )

    def getDepartamento(self):
        return self.departamento

    def getSalarioMensual(self):
        return self.salarioMensual

    def __str__(self):
        return f"{super().__str__()}, Departamento: {self.departamento}, Salario Mensual: {self.salarioMensual}"

