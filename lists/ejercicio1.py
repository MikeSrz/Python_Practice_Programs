#Autor: Michael
#
#Descripción: Contar cuántas veces aparece ese elemento en la lista.

elements = [1,2,34,5,6,2] 

my_element = 2
count= 0
for element in elements:
    if element == my_element:
        count+=1

print(f"El número de {my_element} es {count}.")

    
