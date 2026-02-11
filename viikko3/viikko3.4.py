vuosi=float(input("vuosi:"))
if (vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0):
    print("vuosi", vuosi, "on karkausvuosi")
else:
    print("vuosi", vuosi, "ei ole karkausvuosi")