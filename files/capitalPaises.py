#Descripcion: Juego de adivinar la capital
#
#Autor: MikeSrz

import random
from pathlib import Path


def text_to_array(txt):
    espChars = [",", ".", "-", "_", "+", "`", "|", "!", "$",
                "/", "&", ")", "(", "=", "?", "¿", "%", "—", "❝", "❞"]
    for char in espChars:
        lst = txt.replace(char, "")
    return lst


def csv_to_dict(dct, file_path):
    with open(file_path, encoding='utf-8') as text:
        for linea in text:
            linea = linea.strip().lower()
            key = linea.split(",")[0]
            value = linea.split(",")[1]
            dct[key] = value


def update_screen(points, attempts):
    print(f"LLevas //{points} {'punto' if points == 1 else 'puntos'}")
    print(f"Llevas //{attempts} {'ronda' if attempts == 1 else 'rondas'}.")


SRC_FILE = "capitalPaises.txt"

countries = {}
csv_to_dict(countries, SRC_FILE)
#
#Esto nos ayudará a escoger una llave aleatoria entre las keys.
#
capitals = list(countries.keys())

player_attempts = 0
player_points = 0
finished = False
while (not finished):
    rand = random.randint(0, len(capitals)-1)
    country = capitals[rand]
    capital = countries.get(country).lower()
    capital = capital.strip().lower()
    print("Pulsa 'Q' para salir...")
    player_answer = input(f"Introduce la capital de {country.title()}: ")
    player_answer = player_answer.lower().strip()
    player_attempts += 1

    if player_answer == "q":
        print("Adiós :)")
        finished = True
    elif player_answer == capital:
        player_points += 1
        print("¡HACERTASTE!")
    else:
        print("FALLASTE..")

    update_screen(player_points, player_attempts)


