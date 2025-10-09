#Autor: Michael
#
#Descripción: Programa que cuenta cifras.

print("""
   CONTADOR DE CIFRAS
--------------------------
      """)

#EN CASO DE QUE SEA DECIMAL RESTAREMOS 1, LA COMA
dot_Decimal = 1

try:
    number = float(input("Ingrese un número del intervalo[0, 9,999]: "))

    if 9.999 >= number and 0 <= number:
        if float(int(number)) - number != 0:
            number_Length = len(str(number)) - dot_Decimal
            print(f"El número tiene {number_Length} cifras.")

        else:
            number = len(str(int(number)))
            print(f"El número tiene {number} cifra." if number == 1 else f"El número tiene {number} cifras.")

    else:
        print("El número no está en el intervalo.")

except ValueError:
    print("El valor introducido no era flotante o entero.")



    



