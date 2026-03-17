import random

n = int(input("Montako noppaa heitetään: "))
summa = 0

for i in range(n):
    summa += random.randint(1,6)

print("Silmälukujen summa:", summa)