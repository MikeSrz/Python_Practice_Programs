import csv
import random
from pathlib import Path
from sanitario import Sanitario

class Medico(Sanitario):
    def __init__(self, dni, nombre, fechaNacimiento, numColegiado, area, especialidad = "", anyosExperiencia = 0):
        super().__init__(dni, nombre, fechaNacimiento, numColegiado, area)
        self.especialidad = especialidad
        if anyosExperiencia >= 0:
            self.anyosExperiencia = anyosExperiencia
        else:
            raise ValueError(f"Los años de experiencia no pueden ser negativos.")

    @classmethod
    def aleatorio(cls):
        sanitario = super().aleatorio()
        #el límite superior del ramdom => Edad(años) - 20 (años)
        path = Path("../Datos_CSV_exportables/E2_Sanitario.csv")
        especialidades = set()
        with path.open("r", encoding="utf-8") as f:
            data = csv.DictReader(f)
            for fila in data:
                especialidades.add(fila.get("especialidad"))

        especialidad = random.choice(list(especialidades))
        anyosExperiencia = random.randint(1,20)

        return Medico(sanitario.dni,
               sanitario.nombre,
               sanitario.fechaNacimiento,
               sanitario.numColegiado,
               sanitario.area,
                especialidad,
                anyosExperiencia)

    def puedeAtenderCriticos(self):
        return self.anyosExperiencia >= 5

    def __str__(self):
        return f"{super().aleatorio()}, Especialidad: {self.especialidad}, Años de Experiencia: {self.anyosExperiencia}"

def main():
    medico = Medico.aleatorio()
    print(medico)

if __name__ == "__main__":
    main()


