import random

from persona import Persona
from paciente import Paciente
from sanitario import Sanitario
from medico import Medico
from urgencia import Urgencia

class Hospital():
    def __init__(self, nombre, direccion = "", num = 0, proPa = 50, proSa = 35, proPe = 15):
        if proPa + proSa + proPe != 100:
            raise ValueError(f"Los porcentajes introducidos son incorrectos.")

        self.nombre = nombre
        self.direccion = direccion
        personas = []
        if num > 0:
            self.genPersonas(personas, num, proPa, proSa, proPe)

        self.personas = personas
        self.urgencias = []

    def genPersonas(self, personas, cantidad, pcjPa, pcjSa, pcjPe):
        for i in range(cantidad):
            rand = random.randint(0,100)
            if  rand < pcjPa:
                personas.append(Paciente.aleatorio())
            elif rand < pcjPa + pcjSa:
                personas.append(Sanitario.aleatorio())
            else:
                personas.append(Persona.aleatorio())

    def añadirPersona(self, persona):
        if isinstance(persona, Persona):
            self.personas.append(persona)
        else:
            raise ValueError(f"{persona} no es una persona")
    def añadirUrgencia(self, urgencia):
        if isinstance(urgencia, Urgencia):
            self.urgencias.append(urgencia)
        else:
            raise ValueError(f"{urgencia} no es una urgencia")

    def buscarUrgencia(self, nom_urgencia):
        for urgencia in self.urgencias:
            if urgencia.nombre == nom_urgencia:
                return urgencia
    def contarCriticosTotal(self):
        return sum(urgencia.contarCriticos() for urgencia in self.urgencias)

    def __str__(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}"
def main():
    hospital = Hospital("Manolo Hospital", "Calle Manolo Manolez", 50)
    for persona in hospital.personas:
        print(persona)

if __name__ == "__main__":
    main()