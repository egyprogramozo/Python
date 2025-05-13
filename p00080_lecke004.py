def min_max_adatok(lista):
    return min(lista), max(lista)

lista = [1,5,12,66,45,23,44]
print("A teljes lista: ", lista)

print("A min. és max. értékek:", min_max_adatok(lista))

lista_min, lista_max = min_max_adatok(lista)
print("A min. érték: ", (lista_min))
print("A max. érték: ", (lista_max))