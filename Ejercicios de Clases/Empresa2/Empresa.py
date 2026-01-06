import random
from Empleado import Empleado
from Directivo import Directivo
from Persona import Persona
from Departamento import Departamento
from enum import Enum

class TipoDepartamento(Enum):
    ATENCION_CLIENTE = "ATENCION_CLIENTE"
    INFORMATICA = "INFORMATICA"
    MARKETING = "MARKETING"
    CONTABILIDAD = "CONTABILIDAD"

class Empresa():
    def __init__(self, nombre, cif = "", num = 0, proEm = 60, proDi = 25, proPe = 15):
        if proEm + proDi + proPe != 100:
            raise ValueError(f"Suma de probabilidades incorrecta")
        self.nombre = nombre
        self.cif = cif
        personal = []
        self.genPersonalAleatorio(personal, num, proEm, proDi, proPe)
        self.personal = personal
        self.departamentos = []

    def genPersonalAleatorio(self, lst_personal, numero, pcjEm, pcjDi, pcjPe):
        for i in range (numero):
            rand = random.randint(1,100)
            if rand <= pcjEm:
                lst_personal.append(Empleado.aleatorio())
            elif rand <= pcjEm + pcjDi:
                lst_personal.append(Directivo.aleatorio())
            else:
                lst_personal.append(Persona.aleatorio())

    def añadirPersona(self, persona):
        if persona in self.personal:
            raise ValueError(f"El empleado ya existe.")
        self.personal.append(persona)

    def añadirDepartamento(self, departamento):
        if departamento in self.departamentos:
            raise ValueError(f"El departamento ya existe.")
        self.departamentos.append(departamento)

    def buscarDepartamento(self, miDepartamento):
        for departamento in self.departamentos:
            if miDepartamento == departamento:
                return departamento

    def costeMensualTotal(self):
        costeTotal = 0
        for departamento in self.departamentos:
            costeTotal += departamento.costeMensual()

    def __str__(self):
        return f"Nombre: {self.nombre}, cif: {self.cif}, cantidad Empleados: {self.personal.count()}"


def main():
    empresa = Empresa("ENCOM SOFTWARE", "En efecto", 100)

    #relleno con departamentos
    for nom_departamento in list(TipoDepartamento):
        empresa.añadirDepartamento(Departamento(nom_departamento.value))

    for departamento in empresa.departamentos:
        print(departamento)

    #Además de recorrer los empleados relleno tambien los departamentos:
    for empleado in empresa.personal:
        departamento = random.choice(empresa.departamentos)
        print(empleado)

    print(empresa.costeMensualTotal())

if __name__ == "__main__":
    main()