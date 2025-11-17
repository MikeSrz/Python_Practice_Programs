def extract_words(txt):
    spChars = [",",".","\"","?","¿","!","¡","“","”","-","_","{","}","(",")","@","ª","…",":",";","—","0","1","2","3","4","5","6","7","8","9"]
    acChars = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u","ü":"u"}
    txt = txt.strip().lower()
    for c in spChars:
        txt = txt.replace(c,"")
    for k, v in acChars.items():
        txt = txt.replace(k,v)
    words = txt.split()
    return words

