#Autor: Michael
#
#Descripción: Diccionarios de usuarios con mismas características

import pprint

dict_marks = {
    "Rigoberto": 4/10,
    "Gaspar": 3/10,
    "Fausto": 7/10,
    "Agustina": 9/10,
    "Delfina": 3/10,
    "Méjico": 10/10,
    "Jarripoter": 70/100
}

dict_passers = {}

for key, value in dict_marks.items():

    if value >= 5:
        dict_passers[key] = value*10

pprint.pprint(dict_passers)
