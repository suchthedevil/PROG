"""
Aj v tejto úlohe treba napísať program, ktorý vytvorí 
pyramídu z hviezdičiek, len z hviezdičiek bude len obvod 
trojuholníka, vnútro trojuholníka bude zo znakov mínus 
('-'). Môžeš dostať takýto výstup
"""

n = 7
print(n*" " + "*")
for i in range(1,n):
    print((n-i)*" " + "*", end="")
    for k in range(2*i-1):
        print("-", end="")
    print("*")
print("*"*(2*i+3))



