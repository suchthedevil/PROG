"""
Program prečíta celé číslo a vypíše počet cifier a tiež ciferný 
súčet tohto čísla. Číslo preveďte na znakový reťazec (resp. ho po 
prečítaní neprevádzajte na číslo) a potom postupne pomocou for-cyklu 
prechádzajte jeho cifry (jednoznakové reťazce), každú preveďte na 
číslo a pripočítajte k výslednému súčtu.
"""

n = input("Zadaj cislo: ")
cifry = 0
sucet = 0

for i in n:
    cifry +=1 
    sucet += int(i)

print(f"pocet cifier = {cifry}")
print("ciferny sucet = " + str(sucet))


