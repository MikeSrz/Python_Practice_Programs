#Autor: Michael
#
#Descripción: Probando un diccionario de conteo en una partida.

import random
import time

def dict_counter(dct, key):
    dct[key] = dct.get(key, 0)+1

smash_winners = {
    "Mario": 2,
    "Link": 3,
    "Kirby": 5
}

current_players = ["Mario", "Luigi", "Kirby", "Donkey_Kong", "Sonic", "Link", "Falcon", "Pikachu"]

"""Simulamos que hay una partida"""
game_finished = False
games = 3
while(not game_finished):
    print(f"Marcador: {smash_winners}")
    
    print("La partida está en curso.")
    time.sleep(3)
    winner = current_players[random.randint(0, 7)]
    print (f"El ganador es {winner}")

    dict_counter(smash_winners, winner)
    time.sleep(3)
    
    games -= 1
    if games == 0:
        game_finished = True

print(f"Ganadores: {smash_winners}")
