# Initialisiere die Einkaufsliste
einkaufsliste = []

# Schleife für die Eingabe der Einkaufsartikel
while True:
    artikel = input("Gib einen Einkaufsartikel ein (oder 'fertig' zum Beenden): ")

    # Überprüfe, ob der Benutzer fertig ist
    if artikel.lower() == 'fertig':
        break  # Beende die Schleife, wenn der Benutzer 'fertig' eingibt

    # Füge den Artikel zur Einkaufsliste hinzu
    einkaufsliste.append(artikel)

# Gib die Einkaufsliste aus
print("\nDeine Einkaufsliste:")
for item in einkaufsliste:
    print("- " + item)