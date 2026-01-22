import sqlite3

conexion = sqlite3.connect("Prueba.db")

cursor = conexion.cursor()

sql =  """UPDATE Clientes SET nombre=? WHERE nombre=?"""
val = ("manolo","jorge")
cursor.execute(sql, val)
cursor.execute(sql, val)
conexion.commit()
print()

conexion.close()