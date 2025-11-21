#Descripción: Escribir los 100 primeros primos en un fichero.
#
#Autor: Michael

from pathlib import Path
import math as mth

def detectPrime(n):
    if (n % 2 == 0):
        return False
    for i in range(2, int(mth.sqrt(n)), 1):
        if (n%i == 0):
            return False
    return True

with open('primos.txt', 'w', encoding='utf-8') as f:
    num = 2
    cont = 0
    completed = False
    while (not completed):
        if(detectPrime(num)):
            f.write(f"{num}\n")
            cont +=1
        num+=2
        if (cont == 100):
            completed = True

with open('primos.txt', 'r' , encoding='utf-8') as f:
    for linea in f:
        print(linea.rstrip())
