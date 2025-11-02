#Autor: Michael
#
#Descripción: Invirtiendo llave valor en python

def rev_dict(dct):
    reversed_dct = {}
    for key, value in dct.items():
        if value not in reversed_dct:
            #Creamos una lista, así podemos añadirle un valor siempre que queramos
            reversed_dct[value] = []
        reversed_dct[value].append(key)

    return reversed_dct

               
character_points = {
    "Mario": 1,
    "Link": 2,
    "Luigi": 2,
    "Falcon": 4,
    "GanonDorf": 5
    }

rev_character_points = rev_dict(character_points)
print(character_points)
print(rev_character_points)

