#Autor: Michael
#
#Descripción: Crear la interseción entre dos listas.

numbers1 = [1,2,3,3,4,5,9]
numbers2 = [2,3,7,3,19,888]
intersection = []

for i in range(0, len(numbers1)):
    for j in range(0, len(numbers2)):
        if numbers1[i] == numbers2[j]:
            intersection.append(numbers1[i])

print(f"La intersección entre las dos listas es: {intersection}")



