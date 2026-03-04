palkka = float(input("tuntipalkkasi", ))
tunnit = float(input("tehdyt tunnit", ))
viikonpaiva =input("viikonpäivä:", )
while viikonpaiva != "sunnuntai":
    print("päivänpalkkasi on", palkka * tunnit, "euroa")
    break
if viikonpaiva == "sunnuntai":
    print ("päivänpalkkasi on", palkka * 2 * tunnit, "euroa")
