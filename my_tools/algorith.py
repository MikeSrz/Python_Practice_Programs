#Autor: MikeSrz
#
#Descripción: Módulo de algoritmos.

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
        #El último elemento (extraido con un pop) lo insertamos en la posición 0
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

#Velocidad: Olog(n)
def binary_srch(lst, element):
    minor = 0
    mayor = len(lst)-1
    while minor <= mayor:
        mid = (mayor+minor)//2
        nu = lst[mid]
        if nu == element:
            return True
        elif element > nu:
            minor = mid+1
        else:
            mayor = mid-1

    return False

def search_min_index(lst):
    minor = lst[0] 
    minor_index = 0
    for i in range(1,len(lst)):
       if lst[i] < minor:
        minor_index = i
        minor = lst[i]
    return minor_index 

#Velocidad: O n^2
def selection_sort(lst):
    sorted_lst = []
    for i in range (len(lst)):
        minor_index = search_min_index(lst)
        sorted_lst.append(lst.pop(minor_index))
    return sorted_lst

#Velocidad: O n*log(n)
def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        minors = [i for i in lst[1:] if i <= pivot]
        mayors = [i for i in lst[1:] if i > pivot ]
        return quicksort(minors)+[pivot]+quicksort(mayors) #Jugada Magistral: pivot "arreglado" o sea, pasado a lista.

def main():
    my_list = [1,2,3,4,5,6,7]
    print(binary_srch(my_list, 3))

    my_list = [2,3,4,5,6,10,7,8]
    print(selection_sort(my_list))
    print(my_list)  #Sus elementos han desaparecido porque los he ido eliminado al ordenarla

    my_list = [2,3,4,5,6,10,7,8]
    print(selection_sort(my_list[:])) #Con el truco de la copia funcionará sin borrar nada...
    print(my_list) #Funcionó

    my_list = [2,3,4,5,6,10,7,8]
    print(quicksort(my_list[:])) 

if __name__ == "__main__":
    main()
