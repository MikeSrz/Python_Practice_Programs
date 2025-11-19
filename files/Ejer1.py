#Autor: Michael
#
#Descripción: Escriba un programa que escriba los 100 primeros números primos
#			  Desde primos.txt calculará la suma de todos.

from pathlib import Path
import math

def comprobate_dir(dir_pth):
	if not dir_pth.exists():
		dir_pth.mkdir(parents=True, exist_ok=True)
		print(f"Carpeta {dir_pth.parent} creada.")
	print("La carpeta existe.")

def is_prime(n):
	if n <= 0:
		return False
	elif n <= 3:
		return True
	elif (n % 2 == 0):
		return False
	else:
		for i in range(3, int(math.sqrt(n)), 2):
			if n % i == 0:
				return False
		return True


DST_DIR = Path("data/txt")
comprobate_dir(DST_DIR)
DST_FILE = DST_DIR / "primos.txt"

number = 0
count = 0
LIMIT = 100
finish = False
list_of_primes = []
while(not finish):
	number = number + 1
	if count == LIMIT:
		finish = True
	elif (is_prime(number)):
			count += 1
			list_of_primes.append(number)


with open(DST_FILE, 'w', encoding='utf-8') as f:
	for number in list_of_primes:
		f.write(f"{number}\n")
ac = 0
print("Leyendo Fichero...")
with open(DST_FILE, 'r', encoding='utf-8') as f:
	for line in f:
		number = int(line)
		ac = ac+number
print(f"La suma de los 1000 primeros primos es {ac}")
