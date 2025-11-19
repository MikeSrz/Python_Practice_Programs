#Autor: MikeSrz
#
#Descripción: Cifrado ROT13 que reciba como argumentos de línea de comandos la ruta del fichero de entrada 
#			   y de salida. El programa debe verificar que el fichero de entrada existe antes de procesar.
from pathlib import Path

def encrypt_ROT13(src_file, dst_file):
	with open (src_file, 'rb') as fin, open (dst_file, 'w', encoding="utf-8") as fout:
		ended = False
		while (not ended):
			byte =  fin.read(1)
			if not byte:
				ended = True
			else:
				character = byte[0]
				if character >= 110:
					offset = character - 110
					character = 97 + offset
				elif character >= 97:
					character = character + 13
				elif character >= 78 and character <= 90:
					offset = character - 78
					character = 65 + offset
				elif character >= 65:
					character = character + 13
				character = chr(character)
				fout.write(character)

DST_DIR = Path("data/txt")
DST_FILE = DST_DIR/"cifrado.txt"
SRC_FILE = Path("data/notes/hola_mundo.txt")
encrypt_ROT13(SRC_FILE,DST_FILE)



