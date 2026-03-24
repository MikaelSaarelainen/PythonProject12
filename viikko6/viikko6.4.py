def summa(lista):
    s = 0
    for luku in lista:
        s += luku
    return s

lista = [1, 2, 3, 4, 5]
print("Summa:", summa(lista))