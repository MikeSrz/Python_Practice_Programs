from random import randint

stock  = {
        "frutas" : 5,
        "peras" : 6,
        "manzanas": 7,
        "Guisantes": 8,
        "Párragos" : 9
        }

my_cart = {}

for i in range(5):
    pick = randint(0,4)
    #Elección de producto.
    product = stock.values()[pick]
    stock[product] = stock.get(product) -1
    my_cart[product] = my_cart.get(product, 0)+1

print("Carrito de Compra")
count = 1
for k,v in my_cart.items():
    print(f"Item_{count} {k} | Cantidad: {v}")
    count += 1
