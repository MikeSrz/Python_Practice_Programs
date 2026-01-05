from POO.Baraja import Baraja
import time
mi_baraja = Baraja()
mi_baraja2 = Baraja()

print("""-------------------------------
    Baraja Española
--------------------------------
        
        Baraja 1:   """)

print(mi_baraja.mazo)
print("Barajando...")
time.sleep(0.5)
print(mi_baraja.barajar())
print("--------------------------------------")
input("Pulsa Enter para continuar...")
print("Baraja 2: ")
print(mi_baraja2)
print("barajando...")
time.sleep(0.5)
print(mi_baraja2.barajar())