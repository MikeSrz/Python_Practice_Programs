from Alumno import Alumno
from Profesor import Profesor
from Persona import Persona
import random
class Instituto():
    def __init__(self, nombre, direccion, num_personal):
        self.nombre = nombre
        self.direccion = direccion
        personal = []
        for i in range(num_personal):
            rand = random.randint(0,100)
            if rand < 70:
                personal.append(Alumno.aleatorio())
            if rand < 90:
                personal.append(Profesor.aleatorio())
            else:
                personal.append(Persona().aleatorio())
        self.personal.copy(personal)

    def añadirAlumno(self, alumno):
        if alumno in self.personal:
            raise ValueError(f"El alumno ya está en la lista")
        else:
            self.personal.append(alumno)

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.personal}"

