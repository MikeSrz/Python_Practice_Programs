def count_ocurrencies(lst, my_element):
    count = 0
    for element in lst:
        if element == my_element:
            count+=1
    return count

def removeRepeated(lst):
    uniques = []
    for i in range(0,len(elements)):
        is_unique = True
        for j in range(0, len(uniques)):
            if elements[i] == uniques[j]:
                is_unique=False
                break
        if is_unique:
            uniques.append(elements[i])
    return uniques

def reverse_list(lst):
    cont = 1
    for i in range (0,len(lst)//2):
        tmp = lst[i]
        lst[i] = lst[len(lst)-cont]
        lst[len(lst)-cont] = tmp
        cont += 1

def list_intersection(lst_1, lst_2):
    intersection = []
    for i in range(0, len(numbers1)):
        for j in range(0, len(numbers2)):
            if numbers1[i] == numbers2[j]:
                intersection.append(numbers1[i])
    return intersection

    def difference(lst_1, lst_2):
        difference = []
        for i in range(0, len(numbers1)):
            equal = False
            for j in range (0, len(numbers2)):
                if numbers1[i] == numbers2[j]:
                    equal=True
            if not equal:
                difference.append(numbers1[i])
        return difference

 def shift_list(elements, n):
    for i in range (0,n):
        #El último elemento(extraido con un pop) lo insertamos en la posición 0
        elements.insert(0, elements.pop(len(elements)-1))
    return elements


#APLANAR LISTAS

def has_sublists(lst):
    for i in range (0, len(lst)):
        if type(lst[i]) == list:
            return False
    return True

def flatten_list(elements):
    flat_lst = [] 
    flat = False
    while (not flat):
        for i in range(0, len(elements)):
            if type(elements[i]) == list:
                """concatenar 2 listas = aplanar"""
                flat_lst += elements[i]

            else:
                flat_lst.append(elements[i])

        if not has_sublists(flat_lst):
            elements = flat_lst
            flat_lst = []
        else:
            flat = True

    return flat_lst


def rev_dict(dct):
    reversed_dct = {}
    for key, value in dct.items():
        if value not in reversed_dct:
            #Creamos una lista, así podemos añadirle un valor siempre que queramos
            reversed_dct[value] = []
        reversed_dct[value].append(key)

    return reversed_dct


def encrypt_ROT13(src_file, dst_file):
    with open (src_file, 'rb') as fin, open (dst_file, 'w', encoding="utf-8") as fout:
        ended = False
        while (not ended):
            byte =  fin.read(1)
            if not byte:
                ended = True
            else:
                character = byte[0]
                if character >= 110:
                    offset = character - 110
                    character = 97 + offset
                elif character >= 97:
                    character = character + 13
                elif character >= 78 and character <= 90:
                    offset = character - 78
                    character = 65 + offset
                elif character >= 65:
                    character = character + 13
                character = chr(character)
                fout.write(character)
