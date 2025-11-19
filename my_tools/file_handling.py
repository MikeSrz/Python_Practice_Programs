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
		print("La carpeta existe.")

def main():
		comprobate_dir(Path("C:\\users\\sasuk\\minijuegos"))	
		
if __name__ == "__main__":
	main()

