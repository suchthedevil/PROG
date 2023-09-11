"""
Celé číslo môžeme rozobrať na jednotlivé cifry tak, 
že ho najprv prevedieme na reťazec a potom vo for-cykle 
každú cifru (ako znak) zvlášť prevedieme na číslo. 
Napíš program, ktorý prečíta celé číslo, rozoberie 
ho na cifry, tieto vypíše aj s poradovým číslom a zistí 
ich súčet. Takýto súčet voláme ciferný súčet.
"""

cislo = "52478"
n = 1
sucet = 0
for i in cislo:
    print(f"{n}. cifra: {i}")
    n += 1
    sucet += int(i)
print("Ciferny sucet je:", sucet)

