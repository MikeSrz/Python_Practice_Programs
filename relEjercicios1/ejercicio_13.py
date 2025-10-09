#Autor: Michael
#
#Descripción: Programa que procesa fechas.

from datetime import datetime
print("""
        COMPROBACION DE FECHA
------------------------------------------
""")
date_string = input("Introduzca la fecha en el formato [d/m/A] : ")

try:
    date_string = datetime.strptime(date_string, "%d/%m/%Y")
    print(f"Fecha: {date_string:%d/%m/%Y}")

except ValueError:
    print("El formato introducido es incorrecto")

