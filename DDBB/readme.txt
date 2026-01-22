#####################################################
#########INSTALAR VENV CON DRIVER MYSQL##############
#####################################################
1. Instalación de dependencias para utilizar mysql.connector:
2. $sudo apt update
3. $sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config

CREACIÓN DEL VENV
4. python3 -m venv .venv


#############################
#####PARA ACTIVAR VENV:######
#############################
source .venv/bin/activate
pip install mysql-connector-python
pip install mysqlclient