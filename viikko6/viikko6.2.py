import random

def heita(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Montako tahkoa nopassa: "))
max_luku = int(input("Mikä maksimi pitää tulla: "))

while True:
    luku = heita(tahkot)
    print(luku)
    if luku == max_luku:
        break