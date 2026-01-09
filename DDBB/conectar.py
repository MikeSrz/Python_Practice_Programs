import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin"
    )
    if db.is_connected():
        print("Conexion con exito a la BBDD")
    else:
        print("No conectado")
except Exception as e:
    print(f"No conectado: {e}")

if 'db' in locals() and db.is_connected():
    db.close()
