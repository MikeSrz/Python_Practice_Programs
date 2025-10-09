#Autor: Michael
#
#Descripción: Programa que calcula la longitud de una circunferencia.

PI=3.1514
print("""
      CALCULAR LONGITUD DE LA CIRCUNFERENCIA
      """)
try:
    radius = float(input("Ingrese el radio de su círculo: "))
    longCircle = 2*PI*radius
    print(f"El valor de la longitud es: {longCircle}")
except ValueError:
    print("El valor introducido no era válido, inténtelo de nuevo.")



