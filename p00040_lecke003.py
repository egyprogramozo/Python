"""
    Turtle
"""
import turtle                   # Lehet˝ové teszi a tekn˝oc használatát

ablak = turtle.Screen()         # Hozz létre egy játszóteret a tekn˝ocnek!
ablak.bgcolor("blue")           # Állítsd be az ablak háttérszínét!
ablak.title("Hello, Gergely!")  # Állítsd be az ablak címét!

Gergely = turtle.Turtle()       # Hozz létre egy tekn˝ocöt Sanyi néven!

Gergely.pensize(3)              # Mond meg Gergelynek, hogy változtassa meg a tolla vastagságát!  

Gergely.forward(50)             # Sanyi menjen 50 egységet el˝ore!
Gergely.left(110)               # Sanyi forduljon 90 fokot!
Gergely.forward(30)             # Rajzold meg a téglalap második oldalát!


bgColor = str(input("A lehetséges háttérszínek: \nhttps://www.tcl-lang.org/man/tcl8.4/TkCmd/colors.htm \nA választott háttérszín: "))

ablak.bgcolor(bgColor)          # Állítsd be az ablak háttérszínét!

ablak.mainloop()                # Várj, amíg a felhasználó bezárja az ablakot!