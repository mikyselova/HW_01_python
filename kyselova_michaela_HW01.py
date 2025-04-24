import json

with open("alice.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")

cetnost_znaku = {}
for znak in text:
    if znak not in cetnost_znaku:
        cetnost_znaku[znak] = 1
    else:
        cetnost_znaku[znak] += 1

cetnost_znaku = dict(sorted(cetnost_znaku.items()))

with open("hw01_output.json", "w", encoding="utf-8") as file:
    json.dump(cetnost_znaku, file, indent=4, ensure_ascii=False)
