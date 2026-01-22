import mysql.connector

"""
CONEXION CON BASE DE DATOS, EDITA LOS PARÁMETROS DE CONEXIÓN.
"""
def conectar(db_name):
    config = {
        'host':'localhost',
        'port':777,
        'user':'root',
        'password':'',
        'database':'db_name'
    }

    try:
        db = mysql.connector.connect(**config) #    ** sirve para pasar parametros como: host=tikitiki, port=rikiriki...
        if db.is_connected():
            print("Conexion con exito a la BBDD")
            return db;
        else:
            print("No conectado")
    except Exception as e:
        print(f"No conectado: {e}")
if __name__ == "__main__":
    db = conectar("world")
    db.close()