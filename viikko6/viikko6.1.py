import random

def heita():
    return random.randint(1, 6)

while True:
    luku = heita()
    print(luku)
    if luku == 6:
        break