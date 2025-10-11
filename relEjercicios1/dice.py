#Autor: MikeSrz
#
#Descripción: Realizar una distribución de probabilidad de los resultados tras lanzar dos dados.
#Sum de una lista te devuelve el sumatorio de la cadena entera.
import random

def throwPairDice(times):
    list_of_results = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for n in range(0, times):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        result = dice1 + dice2
        list_of_results[result] += 1
    print (list_of_results)
    return list_of_results

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

n = int(input("Rango de tirada de dados: "))
muestreo = throwPairDice(n)
statistic = generateStatistic(muestreo)
printStatistic(muestreo)




