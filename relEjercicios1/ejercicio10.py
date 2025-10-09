#Autor: Michael
#
#Descripcion: Programa que invierte números.

print(""" 
      REVEVERSE STRINGS
----------------------------""")

try:
    number = float(input("Introduzca un número en el intervalo [0, 9.999]: "))
    
    if 0 <= number and number <= 9.999:
        number = str(number)
        #fUNCIÓN REVERSE
        print(number[::-1]) 
        
    else:
        print("El valor introducido no está en el intervalo.")

except ValueError:
    print("El valor introducido no es un número.")

