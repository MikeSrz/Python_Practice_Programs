#Autor: Michael
#
#Descripción: Programa que compara en tamaño un par de números.

print("""
    COMPARADOR DE NÚMEROS
------------------------------
      """)
try:
    number = int(input("Introduzca un número: "))
    number2 = int(input("Introduzca otro número: "))

    if number == number2:
        print(f"{number} y {number2} son iguales.")

    elif number > number2:
        print(f"{number} es mayor que {number2}.")

    else:
        print(f"{number2} es mayor que {number}.")
except ValueError:
    print("El valor introducido no es entero.")
