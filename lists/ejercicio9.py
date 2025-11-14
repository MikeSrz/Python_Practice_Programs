#Autor: MikeSrz
#
#Descripcición: Invertir una lista con variable temporal
lst = [1, 2, 3, 4, 5, 6,]
cont = 1
for i in range (0,len(lst)//2):
    tmp = lst[i]
    lst[i] = lst[len(lst)-cont]
    lst[len(lst)-cont] = tmp
    cont += 1

print(lst)


