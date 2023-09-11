"""
Program prečíta nejaké slovo a jedno celé číslo n, potom vypíše 
n-riadkov, pričom v každom bude niekoľko znakov bodka a toto zadané 
slovo: v prvom riadku výpisu bude pred slovom n-1 znakov '.',
v každom ďalšom bude o bodku menej
"""

word = input("Zadaj slovo: ")
n = int(input("Zadaj cislo: "))

for i in range(n):
    print((n-i)*"."+ word)


