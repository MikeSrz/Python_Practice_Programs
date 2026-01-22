import mysql.connector
from config import config

def conectar(config):
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
    db = conectar(config)
    db.close()