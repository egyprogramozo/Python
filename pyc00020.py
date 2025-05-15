gyumolcs1 = "alma"
gyumolcs2 = "körte"
print(gyumolcs1 + " " + gyumolcs2)
gyumolcsok = gyumolcs1 + ", " + gyumolcs2
print(gyumolcsok)
print(type(gyumolcsok))

szam1 = 10
szam2 = 4
szam3 = 5
print(szam1 - (szam2 * szam3))
print(type(szam1))

pi = 3.14159265358979
fSzam1 = 0.8515
print(pi)
print(type(pi))

igazHamis = True
print(igazHamis)
print(8>10)
print(len("Szöveg szöveg szöveg")>10)
print(type(igazHamis))

semmi = None
print(semmi)
print(type(semmi))

print("Egyszerű print.")
print(gyumolcs1, " ", szam1)
print(gyumolcs1 + " " + gyumolcs2)
print(gyumolcs1 + str(szam1))
print("2025", "01", "15", sep="-")
print("Első sor", end=" ")
print("és második sor ugyanabba.")
print("Több soros\nszöveg.")
print(f"Gyümölcs: {gyumolcs1}, Ár: {szam1}Ft")
print(f"Számok összege: {szam1+szam2+szam3}")
print(r"Nem értelmezi a \nkaraktereket.")
print(f"formázások: {pi:.0f} {fSzam1:.0f} {fSzam1:.2%}")