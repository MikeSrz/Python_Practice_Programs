import pprint
import random
from conectar import conectar
from config import config

db = conectar(**config)

def game_loop(list):
    print("""
    //////////////////////////////////////
    Bienvenido al juego de las capitales
    /////////////////////////////////////""")
    pais_info = random.choice(list)
    while True:
        print("Dale a [ENTER] para jugar...")
        input()
        user_choice = input(f"En qué pais está '{pais_info[1]}'(Escribe 'Fin' para salir): ").upper()
        if user_choice == "FIN":
            return;

        elif user_choice == pais_info[0].upper():
            print(f"¡Acertaste! Pues su población es {pais_info[2]} personas así como dato.")
            pais_info = random.choice(list)

        else:
            print("Fallaste, inténtalo de nuevo.")


cursor = db.cursor()
sql = """SELECT C.name, CI.name, C.Population
                    FROM country AS C
                    JOIN city AS CI 
                ON C.capital = CI.ID"""

try:
    cursor.execute(sql)

except Exception as e:
    print(e)
data = cursor.fetchall()

#Creación de diccionario e impresión pant.
capitales_poblacion = {}
for country_row in data:
    capitales_poblacion[country_row[0]] = ({country_row[1]}, {country_row[2]})

pprint.pprint(capitales_poblacion)

game_loop(data)
db.close()
