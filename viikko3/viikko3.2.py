hyttiluokka = input("ilmoita hyttiluokka:", )
if hyttiluokka == "lux":
    print("lux parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("ikkunaton hytti autokannen alapuolella.")
else: print("virheellinen hyttiluokka")