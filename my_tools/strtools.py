#Autor:MikeSrz
#
#Descripción: Funciones de manejo de Strings.

def extract_words(txt):
    sp_chars = [",",".","\"","?","!","“","”","-","_","}",")","ª","…",":",";","—","0","1","2","3","4","5","6","7","8","9"]
    ac_chars = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u","ü":"u"}
    apert_chars = ["¿","¡","(", "{"]
    txt = txt.strip().lower()
    for c in sp_chars:
        txt = txt.replace(c,"")

    for c in apert_chars:
        txt = txt.replace(c," ")

    for k, v in ac_chars.items():
        txt = txt.replace(k,v)
        
    words = txt.split()
    return words

def main():
    text = "En un lugar de McDonnald's de cuyo nombre no puedo acordarme(uaoiuoái)"
    lst = extract_words(text)
    print(lst)


if __name__ == "__main__":
    main()