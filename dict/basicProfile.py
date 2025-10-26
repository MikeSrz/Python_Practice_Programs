#Autor: Michael
#
#Descripción: Crear un perfil básico con los campos 'nombre' 'edad' 'ciudad'.
import time
from pprint import pprint

def create_profile(n, a, c):
    dict_profile = {
        "name": n,
        "age": a,
        "city": c,
    }
    return dict_profile

print("""CREACIÓN DE PERFIL
-------------------""")
while True:
    try: 
        name = input("Nombre: ")
        age = int(input("Edad: "))
        city = input("Ciudad: ")
        break
    except Exception:
        print("El valor introducido no es válido.")


user = create_profile(name, age, city)
print (f"El nombre del usuario creado es: \"{user.get("name")}\"")
print(f"Incrementando su edad en 1...")
user["age"] +=1
time.sleep(1)

print(f"Ahora su edad es {user["age"]}")
print (f"Borrando su ciudad...")
user.pop("city")
time.sleep(1)
print("Listo.")

#Añadir un "Desea consultar su ciudad" controlado por ENUMS
print(f"Consultando ciudad... ")
print(f"Ciudad: {user.get('city','No tiene')}")


