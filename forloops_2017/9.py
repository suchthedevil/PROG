"""
Program prečíta celé číslo n a potom do n riadkov postupne na
striedačku vypíše texty 'cervena' a 'modra'
"""

n = int(input("Zadaj n: "))
c1 = "cervena"
c2 = "modra" 

for i in range(n):
    print(c1)
    c1, c2 = c2, c1

