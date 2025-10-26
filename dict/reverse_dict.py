#Autor: Michael
#
#Descripción: Invirtiendo llave valor en python

def rev_dict(dct):
    reversed_dct = {}
    for key, value in dct.items():
        reversed_dct[value] = key
    return reversed_dct

character_points = {
    "Mario": 1,
    "Link": 2,
    "Luigi": 3,
    "Falcon": 4,
    "GanonDorf": 5
    }

rev_character_points = rev_dict(character_points)
print(character_points)
print(rev_character_points)
