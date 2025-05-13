print(type("Helló, Világ!"))
print(type(17))
print(type(3.2))
print(type("17"))
print(type('17'))
print(type('''17'''))
print(type("""17"""))
print('''"Adjon Isten!" - mondta Pista bá' az embernek.''')
print()

message = """Ez a szöveg
több sorban
jelenik meg."""
print(message)
print()

uzenet = 'Szép napunk van!'
n = 15
pi = 3.14159
nap = "Péntek"
print(uzenet, '\n', n, '\n', pi, '\n', nap)
print()

print(1+1)
print("Varázslatos este volt!","karakterek száma: ",len("Varázslatos este volt!"))
print(pi*10)
print(((3+2)*(5/2))**3)
print(120/60)
print()

print(int(3.14))
print(int(-3.999))
print(int(360/60))
print(int("321567"))
print(int(123))
#print(int("123dd")))
print('szoveg '*5)
print()

szoveg1 = "Első része a szövegnek,"
szoveg2 = " de van tovább is."
szoveg3 = szoveg1 + szoveg2
print(szoveg3)
print()

#n = "Gergely"
n = input("Kérem, adja meg a nevét: ")
n_szoveg = "Kedves " + n + ", ez egy Python lecke."
print (n_szoveg)
print()

#szam1 = 2
szam1 = input("Adj meg egy egész számot: ")
#szam2 = 10
szam2 = input("Adj meg egy másik egész számot: ")
print("A két szám összege: ", int(szam1) + int(szam2))
print()

print("7 / 3: ", 7/3)
print("7 // 3: ", 7//3)
print("7 % 3: ",  7%3)
print()

"""
    Copilot megoldotta másodpercek alatt:
    Írj programot, amely meghatározza, mennyi lesz egy betét értéke a futamid˝o végén, ha 10000 Ft-t helyezünk
    betétbe 8%-os névleges kamatláb mellett. Az évközi kamatozások száma (m) 12. Az évek számát, vagyis a
    t értékét a felhasználótól kérje be a program. A futamid˝o végén nézett értéket (FV) az alábbi képlet alapján
    számold:
"""
# Felhasználótól bekérjük a futamidő (t) értékét
#t = 10
t = int(input("Add meg a futamidő években: "))

# Képlet változói
P = 10000  # Kezdőtőke Ft-ban
r = 0.08  # Névleges kamatláb
m = 12  # Évközi kamatozások száma

# Jövőbeni érték számítása
FV = P * (1 + r / m) ** (m * t)

# Eredmény kiírása
print(f"A betét értéke {t} év után: {FV:.2f} Ft")
print()

"""
    Jelenleg pontosan 14 óra van. Beállítunk egy ébreszt˝oórát úgy, hogy 51 órával kés˝obb csörögjön. Hány órakor
    fog az ébreszt˝oóra megszólalni?
"""
akt_ido = 14
n_oraval_kesobb = 51
napok_vege =  (akt_ido + n_oraval_kesobb) // 24
uj_akt_ido = (akt_ido + n_oraval_kesobb) - (24 * napok_vege)
print("Az új aktuális idő: " , uj_akt_ido)
print()

"""
    Copilot megoldása: 
    Ez egy klasszikus maradékos osztás probléma! Az ébresztőóra 51 óra múlva fog csörögni, tehát az aktuális időhöz hozzá kell adnunk ezt, majd figyelembe kell vennünk, hogy az idő 24 órás ciklusokban telik. Azaz:
    [ Ébresztési Idő = (Jelenlegi Idő + Előreállított Idő) % 24 ]
    Íme egy Python program, amely kiszámítja az ébresztési időt:
"""
# Jelenlegi idő órában
jelenlegi_ido = 14

# Előreállított idő órában
eloreallitott_ido = 51

# Ébresztési idő számítása
ebresztesi_ido = (jelenlegi_ido + eloreallitott_ido) % 24

# Eredmény kiírása
print(f"Az ébresztőóra {ebresztesi_ido}:00 órakor fog csörögni.")
print()

"""
    Írj egy Python programot az el˝oz˝o feladat általános megoldására. Kérd be a felhasználótól az aktuális id˝ot (csak
    az órákat) és azt, hogy hány órával kés˝obb szólaljon meg az ébreszt˝oóra, majd jelenítsd meg a képerny˝on, hogy
    hány órakor fog megszólalni az ébreszt˝oóra.
"""
jelenlegi_ido = int(input("Jelenlegi idő órában: "))
eloreallitott_ido = int(input("Előreállított idő órában: "))
ebresztesi_ido = (jelenlegi_ido + eloreallitott_ido) % 24
print("Ébresztési idő: ", ebresztesi_ido)
print()

"""
    Copilot megoldása:
    Írj egy Python programot az el˝oz˝o feladat általános megoldására. Kérd be a felhasználótól az aktuális id˝ot (csak
    az órákat) és azt, hogy hány órával kés˝obb szólaljon meg az ébreszt˝oóra, majd jelenítsd meg a képerny˝on, hogy
    hány órakor fog megszólalni az ébreszt˝oóra.
"""
# Felhasználótól bekérjük az aktuális időt (órákban)
aktualis_ido = int(input("Add meg az aktuális időt (órában, 0-23): "))

# Felhasználótól bekérjük az eltolást (hány órával később szólaljon meg)
eltolas = int(input("Hány órával később szeretnéd, hogy csörögjön az ébresztőóra? "))

# Ébresztési idő számítása
ebresztesi_ido = (aktualis_ido + eltolas) % 24

# Eredmény kiírása
print(f"Az ébresztőóra {ebresztesi_ido}:00 órakor fog csörögni.")
print()