#Autor: Michael
#
#Descripción: Aplanar una lista con listas anidadas.

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
                flat_lst += elements[i]

            else:
                flat_lst.append(elements[i])

        if not has_sublists(flat_lst):
            elements = flat_lst
            flat_lst = []
        else:
            flat = True

    return flat_lst

numbers = [1,3,4,5,[1,88,3,[1,2,3]],8]
print(flatten_list(numbers))
