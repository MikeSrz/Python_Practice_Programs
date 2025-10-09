#Autor: Michael
#
#Descripción: Programa que ordena un trío de números.

print("""
      ORDENACION DE NÚMEROS
----------------------------------
""")
try:
    number = int(input("Ingrese un número: "))
    number1 = int(input("Ingrese un número: "))
    number2 = int(input("Ingrese un número: "))

#ORDENACION
    if number >= number1 and number > number2:
        print(f"{number}, {number1}, {number2}") if number1 >= number2 else print(f"{number}, {number2}, {number1}")

    elif number1 > number and number1 > number2:
        print(f"{number1}, {number}, {number2}") if number >= number2 else print(f"{number1}, {number2}, {number}")

    else:
        print(f"{number2}, {number}, {number1}") if number >= number1 else print(f"{number2}, {number1}, {number}")

except ValueError:
    print("El valor introducido no es un número entero.")
