#Autor:Michael
#
#Descripción: Averiguar si una lista es un palíndromo

elements =  [1,2,5,2,1]
reversed_elements = elements[::-1]

if elements == reversed_elements:
    print("Es palíndromo.")
else:
    print("No es palíndromo.")

