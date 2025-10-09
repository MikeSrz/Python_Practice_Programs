#Autor: Michael
#
#Descripción: Programa que comprueba sin un número es múltiplo de otro.

print("""
COMPROBACIÓN DE MÚLTIPLOS 
-------------------------
""")
try:
    number = int(input("Introduzca un número: "))
    number2 = int(input("Introduzca su múltiplo: "))

    if number <= number2 or number2 == 0:
        print("El número es múltiplo.") if number2 % number == 0 else print("El número no es múltiplo.")

    else:
        print("El número no es múltiplo.")

except ValueError:
    print("El valor introducido no es entero.") 

except ZeroDivisionError:
    print("El número es múltiplo.")
