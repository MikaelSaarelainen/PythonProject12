import math

def hinta(halkaisija, eurot):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade * sade
    return eurot / pinta_ala

h1 = float(input("Pizza 1 halkaisija: "))
e1 = float(input("Pizza 1 hinta: "))

h2 = float(input("Pizza 2 halkaisija: "))
e2 = float(input("Pizza 2 hinta: "))

y1 = hinta(h1, e1)
y2 = hinta(h2, e2)

if y1 < y2:
    print("Pizza 1 on parempi")
else:
    print("Pizza 2 on parempi")