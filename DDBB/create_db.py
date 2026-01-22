from conectar import conectar as con
import mysql.connector
db = con();
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS PRUEBA")
cursor.close()
db.close()
print("DDB PRUEBA Creada con éxito")

