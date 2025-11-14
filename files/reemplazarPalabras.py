from pathlib import Path
base = Path.home() / "chiquito_malaga"
dst_file = base / "chiquito_malaga.txt"
src_file = "quijote.txt"

if not file.parent.exists():
    file.parent.mkdir(parents=True, exist_ok=True)

words_to_replace = {"Quijote":"Chiquito", "Mancha":"Málaga"}

text = Path("src_file").read_text(encoding="utf-8")
text.count(words_to_replace.get("Quijote"))
print(text)
    


