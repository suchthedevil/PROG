"""
Upravte riešenie predchádzajúceho príkladu tak, že výpis 
každého riadku (okrem prvého) bude o 1 posunutý vpravo 
oproti predchádzajúcemu.
"""

n = int(input("Zadaj pocet: "))

for i in range(n):
    print((i)*" ",end="")
    for k in range(1,n+1):
        print(k,end=" ")
    print()
    n-=1

