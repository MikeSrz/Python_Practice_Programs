import sqlite3
from pathlib import Path
from config import config

"""
    EJERCICIO 2
    • Consultar la base de datos para obtener los idiomas más hablados en cada país
        (el idioma con mayor porcentaje de hablantes).
    • Crear un diccionario `idioma_por_pais` donde la clave es el nombre del país y el
        valor el idioma más hablado en ese país.
    • Permitir al usuario introducir el nombre de un país y devolverle el idioma
    principal hablado en ese país.
    • Permitirle al usuario buscar por idioma y devolverle una lista de países donde
        ese idioma es el más hablado.
"""


DB_PATH = Path("databases/world.db")

def main():
    if not DB_PATH.exists():
        print("La ruta de la base de datos es incorrecta.")
        return 1

    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    datos_país = ()
    sql = """
            SELECT C.Name, L.Language
            FROM COUNTRY AS C 
            JOIN COUNTRYLANGUAGE AS L
            ON C.Code = L.countryCode
            WHERE L.Percentage = (SELECT MAX(Percentage) FROM countrylanguage WHERE CountryCode = C.Code);
            """
    cursor.execute(sql)

    # Ejercicio 2.a y 2.b
    data = cursor.fetchall()
    pais_idioma = {}
    for datos_pais in data:
        pais = datos_pais[0].upper()
        idioma = datos_pais[1].upper()
        pais_idioma[pais] = idioma
        print(f"El idioma más hablado en {pais.title()} es {idioma.title()}")

    # Ejercicio 2.c
    print("""
    ---------------------------------------------
            EL MUESTRA IDIOMAS 9000
    ----------------------------------------------
    """)
    exit = False
    while not exit:
        try:
            pais = input(
                "Introduce el nombre de un país y te diré su idioma más hablado(Introduce 'q' para salir): ").upper()
            if pais == 'Q':
                print("Adiós :)")
                exit = True
            else:
                print(f"Su idioma más hablado es: {pais_idioma[pais].title()}")
        except  Exception:
            print("[ERROR] El país introducido no está bien escrito.")

    # Ejercicio 3.c

    print("""
    -----------------------------------------------
            EL MUESTRA PAISES 3000
    ------------------------------------------------""")
    exit = False
    while not exit:
        try:
            idioma = input(
                "Introduce un idioma y te mostraré todos los paises donde se habla(Introduzca 'q' para salir): ").upper()
            if idioma == 'Q':
                print('Adiós :)')
                exit = True
            else:
                for pais in pais_idioma.keys():
                    if pais_idioma[pais] == idioma:
                        print(pais)
        except Exception:
            print("[ERROR] El idioma introducido no está bien escrito.")
    db.close()

if __name__ == "__main__":
    main()