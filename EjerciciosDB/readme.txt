#########################################################
#########  INSTALAR VENV CON DRIVER MYSQL  ##############
#########################################################

Sólo se ejecuta una vez por sistema:

Instalación de dependencias para utilizar mysql.connector:
2. $sudo apt update
3. $sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config

CREACIÓN DEL VENV (Este se ejecuta una vez por cada Proyecto que lo necesite)
4. python3 -m venv .venv


################################
#####  PARA ACTIVAR VENV  ######
################################
1. source .venv/bin/activate

Si es la primera vez en ese venv:
2. pip install mysql-connector-python
3. pip install

##################################
#####  PARA SALIR DEL VENV  ######
##################################

deactivate