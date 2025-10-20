#Autor: MikeSrz
#Fecha: 16/10/2025
#Descripción: generando combinaciones de quiniela
import random

def generateDistribuition(combinations):
    distribution = []
    distribution.append(combinations.count('1'))
    distribution.append(combinations.count('2'))
    distribution.append(combinations.count('x'))
    for i in range len(distribution):
        total = sum(distribution)
        distribution[i] = distribution[i]/total
    return distribution 

def generateStatistic(distribution):
    total = sum(distribution)
    for n in range (0, len(distribution)):
        distribution[n] = (distribution[n]/total)*100
    return distribution

def printStatistic (statistic):
    for i in range (0, len(statistic)):
        graph = f"{i}: "
        for j in range (0, round(statistic[i])):
            graph+="#"
        print (graph)

def generateCombination(repetitions, percx, percy, percz):
    combinations = []
    if percx+percz+percy == 100:
        for i in range (repetitions):
            result = random.randint(0,100)
            if (result < percx):
                combinations.append("1")
            elif (result < percx + percy):
                combinations.append("X")
            else:
                combinations.append("2")

        return combinations
    else:
        return "Porcentajes introducidos no válidos."

for i in range (1,300):
    print(f"{generateCombination(14,20,30,50))}")

