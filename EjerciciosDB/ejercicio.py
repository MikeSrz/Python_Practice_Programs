import sqlite3
from enum import Enum
from pathlib import Path

"""
    pedir continente.
    
"""
DB_PATH = Path("databases/world.db")

class Continentes(Enum):
    AFRICA = 'AFRICA'
    EUROPE = 'EUROPE'
    NOAMERICA = 'NORTH AMERICA'
    SUAMERICA = 'SOUTH AMERICA'
    ASIA = 'ASIA'
    OCEANIA = 'OCEANIA'

def main():
    if not DB_PATH.exists():
        print("[ERROR] La base de datos no existe.")
        return 1
    else:
        print("Conectado a la base de datos.")

    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    sql = """
    SELECT CI.Name, CI.Population
    FROM COUNTRY AS C
        JOIN CITY AS CI
        ON C.Code = CI.CountryCode
        WHERE C.Name = ? and (CI.Population > ? and CI.Population < ?)
    ORDER BY CI.Population DESC;
    """
    #Ejercicio 3.a
    while True:
        try:
            options = []
            print("\"Recuerda que los nombres deben estar en inglés\"")
            options.append(Continentes(input("Introduce el nombre de un continente: ").upper()).value)
            options.append(int(input("Introduce el límite inferior de población: ")))
            options.append(int((input("Introduce un límite superior de población: "))))
            break
        except ValueError as e:
            print(f"[ERROR] Algún dato introducido tiene")

    cursor.execute(sql,tuple(options))
    data = cursor.fetchall()


    db.close()

if __name__ == "__main__":
    main()