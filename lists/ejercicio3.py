#Autor: Michael
#
#Description: Dada una lista inviértela.
numbers = [1,2,3,4,5,6]
reversed_numbers = []

"""Recordemos que range funciona así: [x,y)"""
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])

print (f"La lista invertida numbers es {reversed_numbers}.")
    

