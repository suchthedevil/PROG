"""
Dostali sme správu od mimozemšťanov, ktorá je zložená zo znakov 'O' 
a '-'. Správa obsahuje istý počet riadkov a stĺpcov takýchto znakov. 
Napíš program, ktorým náhodne vygeneruješ podobnú správu. 
"""
import random

row = int(input("Zadaj pocet riadkov: "))
col = int(input("Zadaj pocet stlpcov: "))
signs = "O-"

for i in range(row):
    for i in range(col):
        print(random.choice(signs), end="")
    print()

