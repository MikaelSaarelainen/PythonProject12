sukupuoli = input("sukupuolesi")
hemoglobiiniarvo= float(input("hemoglobiini g/l:",))
if sukupuoli== "nainen" and 117 <= hemoglobiiniarvo <= 175:
    print("hemoblobiiniarvo on normaali")
elif sukupuoli == "nainen" and hemoglobiiniarvo > 175:
    print("hemoblobiiniarvo on normaali")
elif sukupuoli =="nainen" and hemoglobiiniarvo < 117:
    print("hemoglobiini arvo on matala")
if sukupuoli =="mies" and  134 <= hemoglobiiniarvo <= 195:
    print("hemoglobiini arvo on normaali")
elif sukupuoli =="mies" and hemoglobiiniarvo > 195:
    print("hemoglobiini arvo on korkea")
elif sukupuoli == "mies" and hemoglobiiniarvo < 134:
    print("hemoglobiini arvo on matala")


