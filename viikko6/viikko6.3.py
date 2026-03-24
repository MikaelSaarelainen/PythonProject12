def muunna(gallonit):
    return gallonit * 3.785

while True:
    g = float(input("Anna gallonit: "))
    if g < 0:
        break
    print("Litraa:", muunna(g))