from Alumno import Alumno
from Profesor import Profesor
from Persona import Persona
import random
class Instituto():
    def __init__(self, nombre = "", direccion = "", num_personal = 0, proAl = 70, proPr = 20, proPe = 10):
        self.nombre = nombre
        self.direccion = direccion
        self.num_personal = num_personal
        if num_personal != 0:
            personal = []
            self.genPersonalAleatorio(personal, num_personal, proAl, proPr, proPe)
            self.personal = personal


    @classmethod
    def genPersonalAleatorio(self, lst_personal, num, pcj1, pcj2, pcj3):
        if pcj1 + pcj2 + pcj3 != 100:
            raise ValueError(f"Los porcentajes introducidos no suman 100")

        for i in range(num):
            rand = random.randint(0, 100)
            if rand <= pcj1:
                lst_personal.append(Alumno.aleatorio())
            elif rand <= pcj1 + pcj2:
                lst_personal.append(Profesor.aleatorio())
            else:
                lst_personal.append(Persona.aleatorio())


    def añadirAlumno(self, alumno):
        if alumno in self.personal:
            raise ValueError(f"El alumno ya está en la lista")
        else:
            self.personal.append(alumno)

    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.num_personal}"



def main():
    instituto = Instituto("Raymond", "Calle Wallaby Sydney", 100)

    for persona in instituto.personal:
        print(persona)
if __name__ == "__main__":
    main()
