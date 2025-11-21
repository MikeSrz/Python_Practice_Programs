#Autor: MikeSrz
#
#Descripción: Módulo de manejo de ficheros; Rutas, lectura y escritura.

from pathlib import Path
import os

def comprobate_dir(dir_pth):

	if not dir_pth.exists():
		exit = False
		while (not exit):
				print("El directorio padre no existe.")
				option = input(f"¿Quieres crear el directorio padre {dir_pth}? S/N")
				option = option.upper()
				match option:
					case "S":
						#Parents=True permite crear dirs intermedios si no existen. Exists=ok hace que no se lance un error si ya existiera
						dir_pth.mkdir(parents=True, exist_ok=True)
						print(f"Carpeta {dir_pth} creada.")
						exit = True
					case "N":
						print("Ok")
						exit = True
					case _:
						print("Opción Inválida")
	else:
		print("La carpeta ya existe.")

def csv_to_dict(dct, file_path):
    with open(file_path, encoding='utf-8') as text:
        for linea in text:
            linea = linea.strip().lower()
            key = linea.split(",")[0]
            value = linea.split(",")[1]
            dct[key] = value


def main():
	"""
		comprobate_dir(Path("C:\\users\\sasuk\\minijuegos"))	
		if (os.path.exists("demofile.txt")):
			os.remove("demofile.txt")
			print("demofile borrado")

		f = open("demofile.txt", "x") #creará un archivo
		f = open("demofile.txt", "a") #Si existe pues no lo crea
		try:
			f = open("demofile.txt", "x") #Este da un error porque existe ya.
		except FileExistsError:
			print("Esto es un mensaje error de 'x' porque 'demofile.txt' ya había sido creado.")
		f.close()

		input("Pulsa [ENTER] para continuar.")
		os.remove("demofile.txt") #Borra demofile.txt
		dir = Path("myfolder")
		if not dir.exists():
			dir.mkdir()
			print("Creando my folder")
		os.rmdir("myfolder") #Borra la carpeta myfolder
		print("myfolder borrado")

		f = open("demofile.txt", "wt")
		f.write("awooooga!\n¿Quieres saber cuánto vale tu coche?")
		f.close()
		f = open("demofile.txt", "rt") #Realmente "t" se pone por defecto si no pones nada.
									   # En caso de querer jugar con bytes sí -
									   # tienes que poner b
		
		print(f.readline()) #Leo una linea
		print(f.read(1))#Leo un caracter y si lo meto en un bucle leo muchos caracteres consecutivamente

		for i in range(7):
			print(f.read(1), end="") #Así imprimimos todo en linea
		f.close()

		with open("demofile.txt", "r", encoding="latin-1") as f:
			for linea in f:
				print("hola")
		print(Path(__file__))
		print(Path(__file__).resolve().parent)
		print(Path(__file__).resolve().parent / "..")
		texto = Path("demofile.txt").read_text(encoding="utf-8") #Todo lo mete en un texto
	"""	
	base = Path(__file__).parent
	src_path = base / "biblia.txt"
	dst_path = base / "modificado.txt"
	
	with src_path.open("r", encoding='latin-1') as fout, dst_path.open("w", encoding="latin-1") as fin:
		for line in fout:
			mod_line = line.replace("Dios","El Fary")
			fin.write(mod_line)
	txt = dst_path.read_text(encoding="latin-1")
	print(txt)


if __name__ == "__main__":
	main()

