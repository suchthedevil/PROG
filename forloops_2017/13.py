"""
Program prečíta celé číslo n a vypíše výpočet faktoriálu 
tohto čísla v tvare n! = 1*2*...*n = číslo.
"""

n = int(input("Zadaj n: "))

f = 1
print(f"{n}! =", end=" ")
for i in range(1,n):
    f *= i
    print(str(i)+"*",end="")
print(str(n) + " = " + str(f*n))

