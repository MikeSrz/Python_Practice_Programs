#Autor: Michael
#
#Descripción: Programa que detecta capicuas

print("""
 DETECTOR DE CAPICUA
----------------------""")
try:
    number=float(input("Introduzca un número en el intervalo [0, 0.999]: "))
    if 0 <= number and 9.999 >= number:
        number = str(number)
        if number[:1:1] == number[:len(number)-2:-1]:
            print("Es capicua")

        else:
            print("No es capicua.")

    else:
        print("Has introducido un valor fuera del intervalo.")

except  ValueError:
    print("No has introducido un valor numérico")
