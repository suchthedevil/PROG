"""
Vo vlaku sa vezie 100 cestujúcich. V každej stanici, v ktorej 
zastane, niekoľko ľudí vystúpi a niekoľko nastúpi. Napíš program, 
ktorý odsimuluje n takýchto staníc s vystupovaním a nastupovaním 
cestujúcich. Predpokladáme, že v každej stanici vystúpi aj nastúpi 
náhodný počet cestujúcich z intervalu <0, 9>. 
"""
import random

n = int(input("Zadaj n: "))

c = 100

for i in range(n):
    print(f"Vo vlaku bolo {c} ludi,",end=" ")
    nas = random.randrange(0,10)
    vys = random.randrange(0,10)
    c += (nas-vys)
    print(f"{nas} nastupilo, {vys} vystupilo. Zostalo {c}.")

