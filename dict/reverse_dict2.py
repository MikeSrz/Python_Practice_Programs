#Autor: Michael
#
#Descripción: Invirtiendo llave valor en python

def rev_dict(dct):
    reversed_dct = {}
    list_of_repeated = []
    list_of_values = []
    for key, value in dct.items():
        if value in list_of_values:
            list_of_repeated.append(value)
        else:
            reversed_dct[value] = key
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
