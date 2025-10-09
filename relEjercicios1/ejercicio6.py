#Autor: Michael
#
#Descripción: Programa que ordena un par de números.

print("""
ORDENACIÓN
---------------------
      """)
try:
    number1 = int(input("Introduzca un número: "))
    number2 = int(input("Introduzca otro número: "))

    if number1 == number2:
        print(f"{number1} y {number2} son iguales.")

    elif number1 > number2:
        print(f"Lista ordenada: {number1}, {number2}.")

    else:
        print(f"Lista ordenada: {number2}, {number1}.")

except ValueError:
    print("El valor introducido no es un número entero.")

