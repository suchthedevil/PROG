"""
Napíš program, ktorý z hviezdičiek vytvorí takúto pyramídu:

v prvom riadku je najprv n-1 medzier a potom jedna 
hviezdička

v každom ďalšom riadku je o jednu medzeru menej a o dve 
hviezdičky viac
"""
n = 7

for i in range(n):
    print((n-i)*" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()
