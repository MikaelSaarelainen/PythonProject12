lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Lisää lentoasema")
    print("2 = Hae lentoasema")
    print("3 = Lopeta")

    valinta = input("Valinta: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Ei löytynyt")

    elif valinta == "3":
        print("Ohjelma lopetettu")
        break

    else:
        print("Virheellinen valinta")