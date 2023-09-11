"""
Napíš program, ktorý zadané číslo rozloží na prvočinitele 
(vyjadrí ho ako súčin prvočísel).
"""

n = 264
div = 2

rozklad = f"{n} ="
while n>1:
    if n % div == 0:
        rozklad += f" {div} *"
        n /= div
    else: div += 1
rozklad = rozklad[:-1]
print(rozklad)
