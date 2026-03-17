luvut = []

while True:
    x = input("Anna luku: ")
    if x == "":
        break
    luvut.append(float(x))

luvut.sort(reverse=True)
print("Viisi suurinta:", luvut[:5])