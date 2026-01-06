import random


class Urgencia():
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []

    def añadirPaciente(self, paciente):
        self.pacientes.append(paciente)

    def getMasGrave(self):
        maxGravedad = random.choice(self.pacientes).gravedad
        for paciente in self.pacientes:
            if paciente.gravedad > maxGravedad:
                maxGravedad = paciente
        return maxGravedad

    def contarCriticos(self):
        return sum(1 for paciente in self.pacientes if paciente.esCritico())

    def __str__(self):
        return f"{super().__str__()}, Nombre: {self.nombre}"

    def __eq__(self, other):
        if isinstance(other, Urgencia):
            return other.nombre == self.nombre
        else:
            return False
