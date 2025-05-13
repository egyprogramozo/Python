"""
    Turtle - egyéni gyakorlás Copilot segítségével
"""

import turtle

def menu():
    print ("\n------------------------------\n")
    print("Menü (használd a NumPad-ot):")
    print("8 - Haladj előre")
    print("4 - Fordulj balra")
    print("6 - Fordulj jobbra")
    print("2 - Utolsó művelet visszavonása")
    print("5 - Toll felemelése")
    print("0 - Kilépés a játékból")

def toll_fel_le(teki):
    if teki.isdown():
        teki.shape("turtle")
        teki.penup()
    else:
        teki.shape("classic")
        teki.pendown()

def muveletek(szam, teki):
    match szam:
        case 8:
            teki.forward(50)
            return
        case 4:
            teki.left(90)
            return
        case 6:
            teki.right(90)
            return
        case 2:
            teki.undo()
            return
        case 5:
            toll_fel_le(teki)
            return
        case _:
            return
        
ablak = turtle.Screen()
ablak.title("Rajztábla")
ablak.bgcolor("white")

teki = turtle.Turtle()
teki.color("black","black")
teki.speed(1)

while True:
    menu()
    bemenet = input("\nAdj meg egy számot: ")
    if bemenet.strip() == "":  # Ha üres vagy csak szóköz, kérjük újra
        print("Nem adhatsz meg üres értéket!")
        continue
    try:
        szam = int(bemenet)
        muveletek(szam, teki)
        if szam == 0:
            break
    except ValueError:
        print("Hibás bevitel! Kérlek, adj meg egy egész számot.")

print("\nJátszunk máskor is!")


