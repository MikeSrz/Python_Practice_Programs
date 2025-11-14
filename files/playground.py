from pathlib import Path
import os
import sys

print(Path.home())
#Dirección home
home = Path.home()/"onryos"
#DIRECCION Destino
dstFile = Path.home()/prueba_ficheros/logs/log.txt

p = Path(.)
[x for x in p.iterdir() if x.is_dir()]


