import statistics

def min_max_adatok(min_szam, max_szam):
    print(f"A legkisebb szám: {min_szam}")
    print(f"A legnagyobb szám: {max_szam}")
    max_min_atlag = statistics.mean([min_szam, max_szam])
    print(f"A legkisebb és legnagyobb számok átlaga: {max_min_atlag}")

def lista_adatok(lista):
    lista_rendezve = lista.copy()
    lista_rendezve.sort()
    print("Az eredeti lista: ", lista)
    print("A lista rendezve: ", lista_rendezve)
    min_max_adatok(min(lista), max(lista))

lista = []
while True:
    print ("\n------------------------------\n")
    bemenet = input("(kilépés: x) Adj meg egy számot: ")
    if bemenet.strip() == "":  # Ha üres vagy csak szóköz, kérjük újra
        print("Nem adhatsz meg üres értéket!")
        continue
    if (bemenet == "x" or bemenet == "X"):
        break
    try:
        szam = int(bemenet)
        lista.append(szam)
        lista_adatok(lista)
    except ValueError:
        print("Hibás bevitel! Kérlek, adj meg egy egész számot.")

print("\nA program véget ért!")        