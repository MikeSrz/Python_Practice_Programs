#Autor: Michael
#
#Descripción: El programa recibe una nota y devuelve Insuficiente, bien, notable...
print("""
    CALIFICACIÓN
 -------------------
 """)
try:
    mark = int(input("Introduce tu nota: "))
    if 5 > mark:
        print("Insuficiente")
    elif 6 == mark:
        print("bien")
    elif 8 >= mark and 6 < mark:
        print("Notable")
    elif 10 >= mark and 8 < mark:
        print("Sobresaliente")
except (ValueError, TypeError):
    print("El valor introducido no es numérico.")


