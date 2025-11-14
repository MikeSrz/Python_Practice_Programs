#[ <expresion(i)> for i in list if <condición> ]
import random
numeros = [num for num in range(random.randint(0, 1000))]
pares = [num for num in numeros if num % 2 == 0]
print(pares)
