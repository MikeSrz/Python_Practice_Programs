#Autor: Michael
#
#Descripción: Programa que procesa fechas.

from datetime import datetime

print("""
    PROGRAMA DE HORA
------------------------
    """)
#GUARDAMOS FECHA EN STRING
time_string = input("Introduzca la hora en el formato [H:M:S]: ")

try:
    #PARSEO DE STRING A DATETIME OBJECT (STRING, FORMATO)
    time_string = datetime.strptime(time_string, "%H:%M:%S")
    #IMPRIMIMOS EN EL FORMATO H:M:S
    print(f"HORA: {time_string:%H:%M:%S}")

except ValueError:
    print("Formato introducido incorrecto.")
