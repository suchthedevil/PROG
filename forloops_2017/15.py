"""
Program prečíta celé číslo n a vypíše tabuľku n x n čísel 
od 1 do n**2, ktoré sú usporiadané do stĺpcov.
"""

n = int(input("Zadaj n: "))
s = 1

for i in range(1,n+1):
    for k in range(n):
        print(i,end=" ")
        i+=5
    print()

