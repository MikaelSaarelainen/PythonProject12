def parilliset(lista):
    uusi = []
    for luku in lista:
        if luku % 2 == 0:
            uusi.append(luku)
    return uusi

lista = [1, 2, 3, 4, 5, 6]
print("Alkuperäinen:", lista)
print("Parilliset:", parilliset(lista))