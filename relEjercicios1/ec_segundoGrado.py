#Autor: Michael
#
#Descripción: Calculando valor de X en ecuación de segundo grado.

print("""   
    CALCULADORA
Usando la expresión: [ Ax^2 + Bx + c ]
-------------------------------------------""")
import math


#si a es positivo y b es mayor que -4ac => CASO A
#para manejar 0s seguirá otro flujo de cálculo. => CASO C, despejamos la ecuacion y calculamos
#si b^2 es menor que -4ac => CASO B

def calc_2grade_ec(a, b, c):

    if (pow(b, 2)) < ((4) * a * c) and 0 > ((-4)*a*c):
        #CASO B 
        return None, None

    elif c == 0 or a == 0:
        #CASO C
        if a == 0:
            x1 = (-c)/b  
            x2 = None
            return x1, x2
        else: 
            x1 = {-b/a} 
            x2 = 0
            return x1, x2

    else:
        #CASO A: 
        partial_result = ((-4)*a*c)
        partial_result = float(math.sqrt(pow(b,2)+partial_result))
        x1 = (-b + partial_result)/(2*a)
        x2 = (-b - partial_result)/(2*a)
        return x1, x2

try:
    while True:

        a = float(input("introduzca el valor del coeficiente A: "))
        b = float(input("Introduzca el valor del coeficiente B: "))
        c = float(input("Introduzca el valor del coeficiente C: "))
        
        x1, x2 = calc_2grade_ec(a, b, c) 

        if x1 is None and x2 is None:
            print ("El resultado es imaginario.")
        else:
            print(f"valor x1: ${x1} valor x2: ${x2}")
except ValueError:
    print("No se han introducido números")

except ZeroDivisionError:
    print("El valor de x es 0")


