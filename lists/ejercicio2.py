#Autor: Michael
#
#Descripción: Dada una lista,crea una nueva lista que contenga los mismos elementos pero sin duplicados.

elements = [3,3,4,5,3,2,10, "hola"]
uniques = []

for i in range(0,len(elements)):
    is_unique = True
    for j in range(0, len(uniques)):
        if elements[i] == uniques[j]:
           is_unique=False
           break
    if is_unique:
        uniques.append(elements[i])


        



print(f"La lista sin repetidos es: {uniques}")
