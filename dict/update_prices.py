#Autor: Michael
#
#Descripción: Actualizando diccionario salvando los datos modificados.

prices = {
    "camiseta": 15,
    "calcetines": 10,
    "chaqueta": 30,
    "zapatos": 30
}
prices_discount = {
    "camiseta": 10,
    "calcetines": 5,
    "chaqueta": 30,
    "zapatos": 20
}

old_prices = []
for value in prices.values():
   old_prices.append(value) 

cont=0
products_discounted = []
for key, value in prices_discount.items():
   if value != old_prices[cont]:
       products_discounted.append(key) 
   cont+=1
prices.update(prices_discount)

print(f"PRODUCTOS:\n{prices}")
print(f"Productos rebajados: {products_discounted}")
