#Autor: Michael
#
#Descripción: Programa que averigua si un número es positivo o negativo.

print("""
AVERIGUA SI TU NÚMERO(Sólo enteros) ES POSITIVO O NEGATIVO
""")

try:
    number = int(input("Introduce un número: "))
    print("El número es positivo.") if number >= 0 else print("El número es negativo.") 

except ValueError:
    print("El valor introducido no es un número entero.")

