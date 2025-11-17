from pathlib import Path

def comprobate_dir(dir_pth):
	if not dir_pth.exists():
		dir_pth.mkdir(parents=True, exist_ok=True)
		print(f"Carpeta {dir_pth.parent} creada.")
	print("La carpeta existe.")
