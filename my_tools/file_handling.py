#Autor: MikeSrz
#
#Descripción: Módulo de manejo de ficheros; Rutas, lectura y escritura.

from pathlib import Path

def comprobate_dir(dir_pth):

	if not dir_pth.exists():
		exit = False
		while (not exit):
				print("El directorio padre no existe.")
				option = input(f"¿Quieres crear el directorio padre {dir_pth}? S/N")
				option = option.upper()
				match option:
					case "S":
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
		comprobate_dir(Path("C:\\users\\sasuk\\minijuegos"))	


if __name__ == "__main__":
	main()

