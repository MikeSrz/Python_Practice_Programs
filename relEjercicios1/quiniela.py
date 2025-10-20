#Autor: MikeSrz
#Fecha: 16/10/2025
#Descripción: generando combinaciones de quiniela
import random

def generateCombination(repetitions):
    combinations = []
    for i in range (repetitions):
        result = random.randint(1,3)
        match result:
            case 1:
                combinations.append("1")
            case 2:
                combinations.append("X")
            case 3:
                combinations.append("2")
    return combinations

print(f"resultados de quiniela: {generateCombination(14)}")

