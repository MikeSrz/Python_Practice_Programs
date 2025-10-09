#Autor: Michael
#
#Descripción: Calculando valor de X en ecuación de segundo grado.

print("""   
    CALCULADORA
Usando la expresión: [ Ax^2 + Bx + c ]
-------------------------------------------""")
import math

while True:
    try:
        #si a es positivo y b es mayor que -4ac => CASO A
        #para manejar 0s seguirá otro flujo de cálculo. => CASO C, despejamos la ecuacion y calculamos
        #si b^2 es menor que -4ac => CASO B

        a = int(input("introduzca el valor del coeficiente A: "))
        b = int(input("Introduzca el valor del coeficiente B: "))
        c = int(input("Introduzca el valor del coeficiente C: "))
         
        if (pow(b, 2)) < ((4) * a * c) and 0 > ((-4)*a*c):
            #CASO B 
            print("La solución involucra números imaginarios.")
            break;

        elif c == 0 or a == 0:
            #CASO C
            print(f"valor x = {(-c)/b} " if a == 0 else f"Valor x_1 = {-b/a} | Valor x_2 = 0")
            break;
   
        else:
            #CASO A: 
            partial_result = ((-4)*a*c)
            partial_result = float(math.sqrt(pow(b,2)+partial_result))
            positive_result = (-b + partial_result)/(2*a)
            negative_result = (-b - partial_result)/(2*a)
            print(f"Valor x_1 = {positive_result} | Valor x_2 = {negative_result}" )
            break;

    except ValueError:
        print("Los valores introducidos para los coeficientes deben ser enteros.")

    except ZeroDivisionError:
        print("valor x = 0.0")
        break;
