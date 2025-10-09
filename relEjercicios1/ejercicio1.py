#Autor: Michael
#
#Descripción: Programa que calcula el área de un círculo.

#PEDIR ENTRADA DE DATOS A USUARIO
PI = 3.1455

try:
    radius = float(input("Ingrese el radio de su círculo: "))
    
    #CALCULAR AREA
    area = (radius**2)*3.1455

except ValueError:
    print("Valor introducido incorrecto. \nVuelva a intentarlo")
    print(f"EL área de su círculo es: {area}")


