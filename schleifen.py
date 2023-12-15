# Es gibt zwei Arten von Schleifen, die "for" und die "while" Schleife

# for Schleifen werden verwendet, um eine Aktion für jedes Element in einer 
# Sequenz (wie einer Liste oder Zeichenkette) auszuführen:

print("\nFor Schleife zum durchlaufen einer Liste")

früchte = ["Apfel", "Banane", "Orange"]

for frucht in früchte:
    print(frucht)

# Wenn man spezifische Anzahl an Durchläufen erzeugen möchte, kann man die 
# Funktion range() verwenden um eine Sequenz mit entsprechender größe zu erzeugen

print("\nFor Schleife zum durchlaufen einer numerischen Sequenz")    
for i in range(5):
    print(i)


# while Schleifen werden verwendet, um eine Aktion so lange auszuführen, wie eine Bedingung wahr ist

print("\nWhile Schleife")   
zahl = 1

while zahl <= 5:
    print(zahl)
    zahl += 1

# Du kannst eine Schleife auch vorzeitig beenden, wenn der Befehl "break" verwendet wird
print("\nWhile Schleife mit break")
zahl = 1
print(zahl)
while zahl <= 5:
    zahl += 1

    if zahl == 3: 
        print("Zahl ist 3!! Break!!!")
        break

    print(zahl)

# Auch wenn zahl noch nicht 5 ist, wird die Schleife bei 3 beendet und das letzte "print(zahl)" wird nicht mehr ausgeführt
    
# Mit dem Befehl "continue" kannst du den aktuellen Durchlauf der Schleife beenden und zum nächsten übergehen
print("\nWhile Schleife mit continue")    
zahl = 1
print(zahl)
while zahl <= 5:
    zahl += 1 

    if zahl == 3: 
        print("Zahl ist 3!! Continue!!!")
        continue  

    print(zahl)

# print(zahl) wird nicht für den Durchlauf mit der zahl = 3 ausgeführt und die SChleife geht bei 4 weiter