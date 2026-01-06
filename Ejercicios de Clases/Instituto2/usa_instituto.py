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

print("""
-----------------------------------------------
Probando Generación de Personal de Instituto
-----------------------------------------------""")

instituto = Instituto("IES Manolo Manolez", "C/ Eustaquio Habichuela", 100)
print(instituto)
for persona in instituto.personal:
    print(persona)

