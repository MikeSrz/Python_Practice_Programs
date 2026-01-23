import sqlite3
from enum import Enum
from pathlib import Path

"""

    • Pedir al usuario que introduzca un país.

    • Consultar la base de datos y devolver todas las ciudades de ese país ordenadas
    de mayor a menor población.

    • Permitir al usuario establecer un rango de población mínima y máxima para
    filtrar los resultados.

    • Si el usuario introduce un país inexistente, mostrar un mensaje de error y
    permitirle intentarlo de nuevo.

"""
DB_PATH = Path("databases/world.db")



def main():
    if not DB_PATH.exists():
        print("[ERROR] La base de datos no existe.")
        return 1

    print("Conectado a la base de datos.")
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()

    sql1 = """
        SELECT CI.Name, CI.Population
            FROM COUNTRY AS C
        JOIN CITY AS CI
              ON C.Code = CI.CountryCode
        WHERE UPPER(C.Name) = %s
        ORDER BY CI.population DESC;            
          """

    sql2 = """
      SELECT CI.Name, CI.Population
      FROM COUNTRY AS C
          JOIN CITY AS CI
          ON C.Code = CI.CountryCode
          WHERE UPPER(C.Name) = %s and (CI.Population > %s and CI.Population < %s)
      ORDER BY CI.Population DESC;
      """

    # Ejercicio 3.a
    while True:
        pais = input("Introduce el nombre de un pais: ").upper()
        cursor.execute(sql1, (pais,))
        data = cursor.fetchall()

        if data:
            print("En orden de poblacion:")
            for ciudad_info in data:
                pais = ciudad_info[0]
                print(f"{pais} ")
        else:
            print("No existe el país.")
            continue

    #Ejercicio 3.b
        try:
            options = []
            print("\"Recuerda que los nombres deben estar en inglés\"")
            options.append(pais)
            options.append(int((input("Introduce un límite superior de población: "))))
            options.append(int(input("Introduce el límite inferior de población: ")))
            break
        except ValueError as e:
            print(f"[ERROR] Algún dato introducido tiene")
    print(tuple(options))
    cursor.execute(sql2, tuple(options))
    data = cursor.fetchall()
    if data:
        for ciudad_info in data:
            print(f"{ciudad_info[0]} | Población: {ciudad_info[1]}")
    else:
        print("No hay ninguna ciudad con ese rango de poblaciones.")

    db.close()


if __name__ == "__main__":
    main()