from datetime import datetime

def input_date():
    validated = False
    while not validated:
        try:
            date_string = input("Introduzca la fecha en el formato [d/m/A] : ")
            date_string = datetime.strptime(date_string, "%d/%m/%Y")
            print(f"Fecha: {date_string:%d/%m/%Y}")
            validated = True
        except ValueError:
            print("El formato introducido es incorrecto")
    return date_string

def main():
    input_date()

if __name__ == "__main__":
    main()