
class Departamento():
    def __init__(self, nombre):
        self.nombre = nombre
        self.plantilla = []

    def añadirEmpleado(self, empleado):
        if empleado in self.plantilla:
            raise ValueError("El empleado ya existe")
        self.plantilla.append(empleado)

    def buscarPorId(self, idEmpleado):
        for empleado in self.plantilla:
            if empleado.idEmpleado == idEmpleado:
                return empleado

        return None

    def costeMensual(self):
        costeTotal = 0
        for empleado in self.plantilla:
            costeTotal += empleado.salarioMensual

        return costeTotal

    def __eq__(self, other):
        return other.nombre == self.nombre

    def __str__(self):
        return f"Nombre Departamento: {self.nombre}, Cantidad_Personal: {len(self.plantilla)}"

def main():
    departamento = Departamento("INFORMÁTICA")
    print(departamento)

if __name__ == "__main__":
    main()