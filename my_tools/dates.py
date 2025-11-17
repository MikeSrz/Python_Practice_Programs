def input_date():
    while True:
        try:
            date_string = input("Introduzca la fecha en el formato [d/m/A] : ")
            date_string = datetime.strptime(date_string, "%d/%m/%Y")
            print(f"Fecha: {date_string:%d/%m/%Y}")
            break
        except ValueError:
            print("El formato introducido es incorrecto")
    return date_string
