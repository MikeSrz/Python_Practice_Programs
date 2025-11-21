#Autor: MikeSrz
#
#Descripción: Analizador de CSV
def remove_repeated(lst):
    uniques = []
    for i in range(0,len(lst)):
        is_unique = True
        for j in range(0, len(uniques)):
            if lst[i] == uniques[j]:
                is_unique=False
                break
        if is_unique:
            uniques.append(lst[i])
    return uniques

def tran_mtrx(mtrx):
    res = []  
    for i in range(len(mtrx[0])):
        tr_row = []
        for row in mtrx:
            tr_row.append(row[i])
        res.append(tr_row)
    return res
 


import json, csv
from pathlib import Path

base = Path(__file__).parent
src_fl = base / "magical_pets.csv"

rows = []
with src_fl.open(newline="",encoding="utf-8") as f:
	reader = csv.DictReader(f) #Pasa a diccionario
	for row in reader:
		rows.append(row)

print(f"El total de filas es: {len(rows)+1}")
print(f"El número de columnas es: {len(list(rows[0].keys()))}")

matrix = []
for row in rows:
	vct = []
	for v in row.values():
		vct.append(v)
	matrix.append(vct)
tran_mtrx(matrix)

cont = 0

uniques_per_col = []
for i in range(len(matrix[0])):
	 row = matrix[i]
	 uniques_per_col.append(len(remove_repeated(row)))

print(f"Lista de únicos por columna {uniques_per_col}")



