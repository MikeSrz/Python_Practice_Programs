import sqlite3

conexion = sqlite3.connect("prueba.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
cliente_id INTEGER AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(255),
direccion VARCHAR(255)
)""")

conexion.commit()
conexion.close()