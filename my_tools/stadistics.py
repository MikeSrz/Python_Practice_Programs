#Autor: MikeSrz
#
#Descripción: Módulo de estadística, muestreos, análisis de datos.

def dict_counter(dct, key):
    return dct.get(key, 0)+1

def gen_frequency(lst):
    ltr_frequency = {}
    for elem in lst:
       for i in range (len(elem)):
            ltr_frequency[elem[i]] = ltr_frequency.get(elem[i], 0) +1
    return ltr_frequency


def freq_max(dct):
    max_list = []
    #Cogemos un valor aleatorio de los que ya hay
    max_value = dct.get(list(dct.keys())[0])
    for value in dct.values():
        if value > max_value:
            max_value = value

    for key, value in dct.items():
        if max_value == value:
            max_list.append(key)

    return max_list

def freq_to_percentage(freq):
    total = sum(freq.values())
    for k, v in freq.items():
        freq[k]= (v/total)*100


def freq_min(dct):
    min_list = []
    #Cogemos un valor de los que ya hay
    min_value = dct.get(list(dct.keys())[0])
    for value in dct.values():
        min_value = value
        break

    for value in dct.values():
        if value < min_value:
            min_value = value

    for key, value in dct.items():
        if min_value == value:
            min_list.append(key)
    return min_list
