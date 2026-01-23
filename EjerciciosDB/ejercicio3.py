import pprint
import time
from enum import Enum
from conectar import conectar
from config import config
"""
    • Consultar la base de datos y obtener los tres países con mayor población en cada
        continente.
    • Mostrar un menú donde el usuario puede elegir un continente y ver los tres
        países más poblados de esa región.
    • Permitir al usuario introducir un país y devolver la población de dicho país.
    • Agregar la opción de ver el país más poblado del mundo.
"""
class Continentes(Enum):
    AFRICA = 'AFRICA'
    EUROPE = 'EUROPE'
    NOAMERICA = 'NORTH AMERICA'
    SUAMERICA = 'SOUTH AMERICA'
    ASIA = 'ASIA'
    OCEANIA = 'OCEANIA'

def mostrar_ranking(continente, datos_continentes):
    counter = 1
    for datos_pais in datos_continentes.get(continente):
        nombre = datos_pais[0]
        poblacion = datos_pais[1]
        print(f"{counter}º {nombre.title()} | Población: {poblacion}")
        counter += 1
        time.sleep(0.5)
    time.sleep(1)


db = conectar(config)
cursor = db.cursor()
sql = """
    SELECT C1.Continent, C1.Name, C1.Population
    FROM COUNTRY AS C1
    WHERE 
        (SELECT COUNT(*) FROM COUNTRY as C2
            WHERE
                C1.Population < C2.Population
                and C1.Continent = C2.Continent ) < 3
        AND C1.Continent NOT LIKE ("Antarctica")
    ORDER BY C1.Continent;
"""
cursor.execute(sql)
data = cursor.fetchall()

dict_continentes = {}
for row in data:
    continente = row[0]
    nombre = row[1]
    poblacion =row[2]
    print( f"Continente: {continente}, Pais: {nombre}, Población: {poblacion}")

    dict_continentes[continente.upper()]= dict_continentes.get(continente.upper(), [])
    dict_continentes[continente.upper()].append((nombre.upper(), poblacion))

pprint.pprint(dict_continentes)

#Ejercicio 3.b Menú
exit = False
while not exit:
    print("""
    MENÚ DE USUARIO 
    ---------------------
        1. Africa
        2. Europa
        3. Norte América
        4. Sudamérica
        5. Asia
        6. Oceanía
        7. Salir
    ---------------------""")
    option = int(input("Escoge un continente: "))
    match(option):
        case 1: mostrar_ranking(Continentes.AFRICA.value, dict_continentes)
        case 2: mostrar_ranking(Continentes.EUROPE.value, dict_continentes)
        case 3: mostrar_ranking(Continentes.NOAMERICA.value, dict_continentes)
        case 4: mostrar_ranking(Continentes.SUAMERICA.value, dict_continentes)
        case 5: mostrar_ranking(Continentes.ASIA.value, dict_continentes)
        case 6: mostrar_ranking(Continentes.OCEANIA.value, dict_continentes)
        case 7: exit = True
        case _:
            print("[ERROR] La opción escogida no es válida")
            continue

#Ejercicios 3.c y 3.d
print("""


---------------------------
 VER POBLACIÓN DE UN PAÍS  
---------------------------""")
db = conectar(config)
cursor = db.cursor()
while True:
    print("(Escriba 'MAX' si quieres averiguar el país más poblado.)")
    pais = input("Escribe el nombre de un país(Introduzca 'q' para salir): ").upper()
    match pais:
        case 'Q':
            break
        case 'MAX':
            sql = """
            SELECT Name, Population
            FROM COUNTRY
            ORDER BY Population DESC LIMIT 1
            """
            cursor.execute(sql)
        case _:
            sql = """
            SELECT Name, Population 
            FROM COUNTRY
            WHERE UPPER(Name) = %s 
            """
            cursor.execute(sql,(pais,))

    datos = cursor.fetchone()

    if datos:
        nombre, poblacion = datos
        print(f"{nombre} | {poblacion}")
    else:
        print("El país no existe o lo has escrito mal.")

db.close()

