from pathlib import Path

from POO.Song import Song

file_path = Path("canciones.txt")
if not file_path.exists():
    print("No existe el fichero")
else:
    song_list = []
    with file_path.open("r", encoding="utf-8") as fout:
        for line in fout:
            song_name = line.split(":")[0].strip()
            artist = line.split(":")[1].strip()
            song_list.append(Song(song_name, artist))

    for song in song_list.sort(key=lambda c:(c.title, c.author)):
        print(song)

