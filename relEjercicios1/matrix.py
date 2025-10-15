#CREAMOS MATRIZ vacía
matrix = []
"""Se le añade a la matriz primero una fila vacía y luego elementos(columnas) dentro del j"""
rows = 5
cols = 5

for i in range (rows):
    matrix.append([])
    for j in range (cols):
       matrix[i].append(j)

print(matrix)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end =" ")
    print()
    

