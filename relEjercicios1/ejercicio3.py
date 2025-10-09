#Autor: Michael
#
#Descripción: Programa que compara dos números.

print("""
COMPARACION DE DOS NÚMEROS
     """)

try:
    number1 = int(input("Introduzca el primer número: "))
    number2 = int(input("Introduzca el segundo número: "))

    if number1 > number2:
        print(f"El número más grande era {number1}.")
    
    elif number1 == number2:
        print("Los dos números introducidos son iguales.")

    else:
        print(f"El número {number2} es el mayor.")

except ValueError:
    print("El valor introducido no es un número entero.")



