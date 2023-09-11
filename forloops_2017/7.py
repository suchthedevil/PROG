"""
Program prečíta slovo (znakový reťazec) a vytvorí z neho nový reťazec.
Tento bude mať pred každým znakom číslo vyjadrujúce jeho pozíciu v 
pôvodnom reťazci, teda postupne pre každý znak pridá reťazce '0', 
'1', '2', …

"""

word = input("Zadaj slovo: ")
n = 0
vysledok = ""
for i in word:
    vysledok = (str(n)+i)
    n += 1
    print(vysledok, end="")

