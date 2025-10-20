#Autor: MikeSrz
#Fecha: 16/10/2025
#Descripción: generando combinaciones de quiniela
import random

def generateCombination(repetitions):
    combinations = []
    for i in range (repetitions):
        result = random.randint(0,100)
        if (result < 60):
            combinations.append("1")
        elif (result > 60 and result < 90):
            combinations.append("X")
        else:
            combinations.append("2")
    return combinations

print(f"resultados de quiniela: {generateCombination(14)}")

