#Autor:Onryos
#
#Descripción: Programa que pide al usuario una temperatura y la puede convertir a la que quiera.

def printMenu():
    print("""OPCIONES 
            1) Convertir a Celsius.
            2) Convertir a Farenheit.
            3) Convertir a Kelvin.
            4) Salir del programa.
            """)

def toCelsius(temp, u):
    match u:
        case "C":
            return temp
        case "F":
            return (temp-32) * 5/9
        case "K":
            return (temp - 273.15)

def toKelvin(temp, u):
    match u:
        case "C":
            return temp + 273

        case "F": 
            return 5/9*(temp -32)+273.15

        case "K":
            return temp
    
def toFarenheit(temp, u):
    match u:
        case "C":
            return temp * 9/5 +32 

        case "F":
            return temp

        case "K":
            return 9/5 * (temp - 273.15) + 32
        

#FUNCIÓN PRINCIPAL
ERROR_MESSAGE = "La opción elegida no es válida."

input_temperature = True
terminate=False
while(True):
    try:
        #
        while (input_temperature):
            unit = input("Introduzca la UNIDAD de su temperatura [K, F, C]: ").upper()
            temperature = float(input("Introduzca la temperatura: "))
            if unit in {"K", "F", "C"}:
                input_temperature = False

        printMenu()
        option = int(input("Introduzca una opción de conversión [1, 2, 3, 4]: "))
        match option:
            case 1:
                u_symbol = "C"
                conv_temperature = toCelsius(temperature, unit)

            case 2:
                u_symbol = "F"
                conv_temperature = toFarenheit(temperature, unit)

            case 3:
                u_symbol = "K"
                conv_temperature = toKelvin(temperature, unit)

            case 4:
                terminate = True 

            case _:
                print(ERROR_MESSAGE)

        if not terminate:
            print(f"Resultado de la conversión: {conv_temperature} {u_symbol}")
        else:
            break
        
        option = input("¿Desea introducir una nueva temperatura? Y/N[default=NO]: ").upper()
        if option == 'Y':
            input_temperature = True


    except ValueError:
        print(ERROR_MESSAGE)





