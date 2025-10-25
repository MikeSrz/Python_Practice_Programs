#Autor: Michael
#
#Descripción: Desplaza todos los elementos de una lista un número de posiciones.

def shift_list(elements, n):
    for i in range (0,n):
        elements.insert(0, elements.pop(len(elements)-1))
    return elements
    

elements = [1,2,3,4,5,6,7]
n = int(input("¿Cuántas posiciones quieres desplazar la lista?: "))

print(shift_list(elements, n))
