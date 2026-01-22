import sqlite3

conexion = sqlite3.connect("Prueba.db")

cursor = conexion.cursor()

sql =  """INSERT INTO clientes (nombre, direccion) VALUES (?,?)"""
val = ("jorge","murcia")

cursor.execute(sql, val)
conexion.commit()
conexion.close()