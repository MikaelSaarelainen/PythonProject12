tarina = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu":
        print(tarina.strip())
        break
    else:
        tarina += sana + " "