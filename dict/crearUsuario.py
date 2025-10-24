import pprint

def createProfile():
    perfil = {
        "user" : input("Inserte su nombre: "),
        "age" : input("Inserte su edad: "),
        "degree" : input("Inserte su especialidad: "),
        "contact" : {
            "Tfno" : input("Inserte su teléfono: "),
            "email" : input("Inserte su email: "),
        }
    }
    return perfil

#todas las max, todas las min(), cual es la frecuencia de la palabra max y la min
pprint.pprint(createProfile())


