#Autor: Michael
#Fecha:
#Descripción: Calcular Factorial.
def calculateFactorial(n): 
    if n == 0:
        return 1
    return n*calculateFactorial(n-1)

print("""CALCULAR FACTORIAL""")
while (True):
    try:
        number = int(input("Introduce un número: "))
        if number > 0:
            break
        print("El número introducido debe ser 0 o positivo.")


    except ValueError:
            print("El valor introducido no es válido.")

print(f"El factorial de {number} es {calculateFactorial(number)}")
