import json

# Textdatei einlesen
with open("fragen.txt", "r", encoding="utf-8") as f:
    text = f.read()

quiz = []

# Fragen trennen
blocks = text.split("+ Zum Quiz hinzufügen")

for block in blocks:
    lines = [line.strip() for line in block.strip().splitlines() if line.strip()]

    if len(lines) >= 2:
        frage = lines[0]
        optionen = lines[1:]

        # Erste Antwort als richtige Antwort
        antwort = optionen[0]

        quiz.append({
            "frage": frage,
            "optionen": optionen,
            "antwort": antwort
        })

# JSON speichern
with open("quiz.json", "w", encoding="utf-8") as f:
    json.dump(quiz, f, ensure_ascii=False, indent=2)

print("quiz.json wurde erstellt!")

