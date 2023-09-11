"""
Budeme simulovať hádzanie dvomi hracími kockami. 
Zakaždým vypíšeme aj ich súčet. Napíš program, ktorý to 
simuluje n-krát.
"""
import random

n = int(input('Zadaj n: '))
sum = 0

for k in range(n):
    for i in range(1,3):
        d = random.randrange(1,7)
        sum += d
        print(f"Na {i} kocke padla {d}")
    print(f"Ich sucet je {sum}")
    sum = 0
    print("=====================")
