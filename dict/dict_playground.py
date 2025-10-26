dict_vacío= {} #Dicionario vacío
dict_vacío2 = dict()

persona = {"nombre": "Ana",
            "edad": 52,
            "ciudad": "Málaga",
            "casado": True,
            "contacto": {
                    "tfno": "+34 653297707",
                }
            }

persona["edad"] = 53 
print(persona["edad"])

persona["edad"] = persona.get("edad",0)-20

print(f"{persona["nombre"]} tiene {persona["edad"]} y su email {persona["contacto"].get("email", "No lo tenemos")}")


