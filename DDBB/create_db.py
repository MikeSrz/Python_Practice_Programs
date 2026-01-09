import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin"
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS PRUEBA")
    cursor.close()
    db.close()
    print("DDB PRUEBA Creada con éxito")
except Exception as e:
    print(f"Error: {e}")
