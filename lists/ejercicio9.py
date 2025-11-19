#Autor: MikeSrz
#
#Descripcición: Invertir una lista con variable temporal
def reverse_list(lst):
    cont = 1
    for i in range (0,len(lst)//2):
        tmp = lst[i]
        lst[i] = lst[len(lst)-cont]
        lst[len(lst)-cont] = tmp
        cont += 1

my_lst = [1, 2, 3, 4, 5, 6,]
reverse_list(my_lst)
print(my_lst)


