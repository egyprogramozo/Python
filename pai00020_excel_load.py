# Adatok betöltése, Excel fájl beolvasása

import pandas as pd

# Excel fájl beolvasása
file_name = "pai00020_test.xlsx"
sheet_name = "Lista"

# Az oszlopok beolvasása
df = pd.read_excel(file_name, sheet_name=sheet_name)

#A Pandas DataFrame kiírása
print(df)

#A Pandas DataFrame adott elemének kiírása (sor, oszlop)
print(df.iloc[0, 0])

# Adatok listába konvertálása (első oszlop)
lista1 = df.iloc[:, 0].tolist()
print(lista1)

# Adatok listába konvertálása (második oszlop)
lista2 = df.iloc[:, 1].tolist()
print(lista2)

# Adatok listába konvertálása (első sor)
lista3 = df.iloc[0, :].astype(str).tolist()
print(lista3)

