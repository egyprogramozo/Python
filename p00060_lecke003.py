#1. Egyszerű iteráció egy listán
for nev in ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]:
    meghivas = "Szia, " + nev + "! Kérlek gyere el a bulimba szombaton!"
    print(meghivas)

#2. Számok bejárása range() segítségével
for szam in range(-3, 4):  # -2-től 4-ig iterálunk
    print(f"Szám: {szam}")

for szam in range(-3, 4, 2):
    print(szam)    

#3. Lista elemeinek sorszámozása
"""
    Az enumerate() függvény egy praktikus eszköz Pythonban, amely lehetővé teszi, hogy egy iterálható objektum
    (például lista vagy sztring) elemei mellett azok indexét is elérd egy for ciklusban. Ez különösen hasznos,
    amikor nem csak az értékekkel, hanem a pozíciójukkal is dolgozni szeretnél.
"""
nevek = ["Anna", "Béla", "Csaba"]
for i, nev in enumerate(nevek):
    print(f"{i}. név: {nev}")

for i, nev in enumerate(nevek):
    print(f"{i+1}. név: {nev}")

for i, nev in enumerate(nevek, start=1):
    print(f"{i}. név: {nev}")


#4. Két lista párhuzamos bejárása
nevek = ["Anna", "Béla", "Csaba"]
korok = [25, 30, 35]
for nev, kor in zip(nevek, korok):
    print(f"{nev} {kor} éves.")

#5. String karaktereinek bejárása
szoveg = "Python"
for karakter in szoveg:
    print(f"Karakter: {karakter}")

#6. For ciklus break és continue használatával
for szam in range(1, 10):
    if szam == 5:
        print("Megtaláltuk az 5-öst, kilépünk!")
        break  # Kilép a ciklusból
    elif szam % 2 == 0:
        continue  # A páros számokat kihagyja a kiírásból
    print(f"Feldolgozott szám: {szam}")

#7. Fordított iteráció (reversed())
szamok = [1, 2, 3, 4, 5]
for szam in reversed(szamok):
    print(szam)