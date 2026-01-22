import mysql.connector
def conectar(db_name):
    try:
        db = mysql.connector.connect(
            host="localhost",
            port=7777,
            user="root",
            password="",
            database = db_name
        )
        if db.is_connected():
            print("Conexion con exito a la BBDD")
            return db;
        else:
            print("No conectado")
    except Exception as e:
        print(f"No conectado: {e}")
if __name__ == "__main__":
    db = conectar()
    db.close()