"""
Program prečíta nejaké slovo a jedno celé číslo n, potom vypíše 
n-riadkov: v prvom je zadané slovo raz, v druhom je 2-krát 
(slová sú oddelené medzerou), v treťom 3-krát (tiež s medzerou 
medzi slovami), atď. Použite len jeden cyklus.
"""

word = input("Zadaj slovo: ")
n = int(input("Zadaj cislo: "))

for i in range(1,n+1):
    print(i*(word+" "))
