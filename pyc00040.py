szoveg = "    sZovEg amiBen veGyeSEn van MinDen, például szám: 2583   "
print(szoveg.upper())
print(szoveg.lower())
print("A nem angol betűknél is kisbetűsít: ", "ß".casefold())
print(szoveg.capitalize())
print(szoveg.title())
print(szoveg.swapcase())
print(szoveg.strip())
print(szoveg.lstrip())
print(szoveg.rstrip())
print(len("Hány karakter vagyok?"))

lista = "első szoveg-második szoveg-harmadik szöveg".split("-")
print("A generált lista: ",lista)

csakSzamok = "1234567xy890".isnumeric()
print(csakSzamok)

szoveg = "1234567890abcdefg"
print(szoveg[2])
print(szoveg[2:5])
print(szoveg[2:12:2])

szoveg = "Cserebere"
print("replace: ", szoveg.replace("re","__"))

import random
randomSzam = random.randint(1,10)
print("Ez egy random generált szám:", randomSzam)