"""
Program prečíta celé číslo n a vypíše tabuľku čísel s n 
riadkami, pričom v prvom sú čísla od 1 do n, každý ďalší 
riadok je o 1 kratší (bez posledného čísla), v poslednom 
je 1.
"""
n = int(input("Zadaj pocet: "))

for i in range(n):
    for k in range(1,n+1):
        print(k,end=" ")
    print()
    n-=1
