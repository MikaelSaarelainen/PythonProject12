luku = int(input("Anna kokonaisluku: "))

Alkuluku = True

if luku < 2:
    Alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            Alkuluku = False
            break

if Alkuluku:
    print("Alkuluku")
else:
    print("Ei alkuluku")