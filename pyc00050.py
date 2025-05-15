lista = list(range(0,15))
print(lista)

print ("\nif:")
#eletkor = int(input("Hány éves vagy? >"))
eletkor = 19
if eletkor < 18:
  print("Túl fiatal vagy a dohányzáshoz!")
elif (eletkor >= 18 and eletkor <= 45):
  print("Már dohányozhatsz!")
else:
  print("Egyre nagyobb kockázatot jelent számodra a dohányzás!")

print ("\nfor:")
gyumolcsok = ["alma","körte","banán"]
for gyumolcs in gyumolcsok:
  print(f"Szeretm a(z) {gyumolcs}-t!")

print ("\nfor (enumerate):")
gyumolcsok = ["alma","körte","banán"]
for i, gyumolcs in enumerate(gyumolcsok):
  print(f"{i}. elem: {gyumolcs}")

print ("\nfor (enumerate és start):")
gyumolcsok = ["alma","körte","banán"]
for i, gyumolcs in enumerate(gyumolcsok, start = 1):
  print(f"{i}. elem: {gyumolcs}")

print ("\nfor (range):")
for szam in range(5, 15)  :
  print(szam)

print ("\nfor (range és léptetés):")
for szam in range(5, 15, 2)  :
  print(szam)

print ("\nfor (beágyazott):")
for i in range (8, 12):
  for j in range (8, 12):
    print(f"{i:02d} X {j:02d} = {(i*j):03d}")

print ("\nfor (zip):")
nev = ["Péter","Zoltán","Anita"]
kor = ["18","31","23"]
for nev, kor in zip(nev, kor):
  print(f"{nev} {kor} éves.")

print ("\nfor (break, continue):")
for szam in range (1, 10):
  if szam == 5:
    break
  if (szam % 2) == 0:
    continue
  print(szam)

print ("\nwhile:")
szam = 30
while szam > 10:
  print(szam)
  szam-=5