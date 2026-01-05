import csv
import pprint
from pathlib import Path
from Persona import Persona
from Instituto import Instituto
personas = set()
for i in range(20):
    personas.add(Persona.aleatorio())
for persona in personas:
    print(persona)

Instituto("IES Raymond", "Avenida Galáctica", 50)