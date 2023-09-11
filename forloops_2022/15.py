"""
Napíš program, ktorý vygeneruje na číselnej osi dva náhodné body 
(v intervale <0, 100>) a vypočíta ich vzdialenosť.
"""
import random

n =  int(input("Zadaj n: "))

for i in range(n):
    p1 = random.randrange(0,101)
    p2 = random.randrange(0,101)
    print(f"Prvy bod na priamke je {p1}, druhy bod je {p2}. Vzdialenost je {abs(p1-p2)}")

    