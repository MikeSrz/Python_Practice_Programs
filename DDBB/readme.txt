Instalación de dependencias para utilizar mysql.connector:
$sudo apt update
$sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
crear:
python3 -m venv .venv
Para utilizar:

source .venv/bin/activate

pip install mysql-connector-python

pip install mysqlclient