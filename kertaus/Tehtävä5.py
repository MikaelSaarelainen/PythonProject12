while True:
    print("LASKIN")
    print("1 yhteenlasku")
    print("2 vähennyslasku")
    print("3 kertolasku")
    print("4 jakolasku")
    print("0 Lopeta")
    valinta = input ("valitse toiminto:")
    if valinta == "0":
        print("Ohjelma lopetetaan")
        break
    elif valinta in ("1", "2", "3", "4",):
        luku1 = float(input("anna ensimmäinen luku: "))
        luku2 = float(input("anna toinen luku:"))
        if valinta == "1":
            tulos = luku1 + luku2
            print("tulo:", tulos)
        elif valinta == "2":
            tulos = luku1 - luku2
            print("tulos:", tulos)
        elif valinta == "3":
            tulos = luku1 * luku2
            print("tulos:", tulos)
        elif valinta == "4":
            if luku2 == 0:
                print("ei voi jakaa nollalla!")
            else:
                tulos = luku1 / luku2
                print("tulos:", tulos)
        else:
            print("Virheellinen valinta, yritä uudelleen.")


