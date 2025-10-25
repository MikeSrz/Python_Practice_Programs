#Autor: Michael
#
#Descripción: Crear una lista donde se encuentran los elementos que están en la primera y no en la segunda.
numbers1 = [1,3,4,5,88,5,7]
numbers2 = [2,2,3,4,5,8,99]
difference = []

"""El primer bucle indica la lista de la que queremos obtener los únicos."""
for i in range(0, len(numbers1)):
    equal = False
    for j in range (0, len(numbers2)):
        if numbers1[i] == numbers2[j]:
            equal=True
    if not equal:
        difference.append(numbers1[i])
        
print(f"La diferencia es: {difference}.")
