try:
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin"
    )

except Exception as e:
    print(f"Error: {e}")