"""
Program vypíše tabuľku výpočtu prvých 10 faktoriálov 
(vo formáte z predchádzajúceho príkladu). Použite vnorené 
cykly.
"""

n = int(input("Zadaj n: "))
for k in range(1,n+1):
    f = 1
    print(f"{k}! =", end=" ")
    for i in range(1,k):
        f *= i
        print(str(i)+"*",end="")
    print(str(k) + " = " + str(f*k))

