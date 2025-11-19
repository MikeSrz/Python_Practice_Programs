#Autor: Michael
#
#Descripción: Contar cuántas veces aparece ese elemento en la lista.

def count_ocurrencies(lst, my_element):
    count = 0
    for element in lst:
        if element == my_element:
            count+=1
    return count

my_list = [1,1,2,34,5,6,1,2] 
choice = 1
ocurrencies = count_ocurrencies(my_list, choice)
print(f"El número de {choice} es {ocurrencies}.")

    
