import sqlite3

db = sqlite3.connect("prueba.db")

cursor =  db.cursor()
sql =  "DELETE FROM clientes WHERE nombre=?"
cursor.execute(sql)

val=  ("Paco",)
cursor.execute()