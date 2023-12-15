# Wir legen eine Liste mit drei Objekten an
früchte = ["Apfel", "Banane", "Orange"]

# Eine Liste kann Eintrag für Eintrag durchlaufen werden, für jeden Eintrag in der Liste
# wird die Schleife einmal durchlaufen.
# Die Schleife zerlegt die Liste in seine Einträge und legt den aktuellen Eintrag in die Variable "frucht"
# Im ersten Durchlauf der Schleife wird der Text "Apfel" in die Variable Frucht gespeichert und über print(frucht) ausgegeben.
# Im zweiten Durchlauf wird "Banane" in die Variable Frucht gespeichert und geprintet
# Im dritten Durchlauf wird "Orange" in die Variable Frucht gespeichert, geprintet und die Schleife wird beendet 
# weil alle Elemente von früchte durchlaufen wurden
for frucht in früchte:
    print(frucht)


# Jeder Datentyp der Sequenzierbar ist, kann durchlaufen und in seine Elemente zerlegt werden  
wort = "wort"

# Hierbei wird jeder Buchstabe von "wort" einzeln durchlaufen und über print(buchstabe) ausgegeben
for buchstabe in wort:
    print(buchstabe)
