#Descripcion: Juego de adivinar la capital
#
#Autor: MikeSrz

from pathlib import Path
def text_to_array(txt):
    espChars = [",", ".", "-", "_","+","`","|", "!", "$", "/","&",")","(","=","?","¿","%", "—","❝","❞"]
    for char in espChars:
        lst = txt.replace(char, "")
    return lst

def json_to_array(txt, file_path):
    with open (file_path, encoding='utf-8') as text:
        for linea in text:
            print(linea)


SRC_FILE = "capitalPaises.txt"
txt = Path(SRC_FILE).read_text(encoding='utf-8')
#capitals_dict = text_to_dictionary(txt)

print(txt)
player_attempts = 0
player_points = 0
finished = True

list_of_capitals = json_to_array(txt, SRC_FILE)
print(list_of_capitals)
#while (not finished):
    




