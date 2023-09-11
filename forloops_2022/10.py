"""
Napíš program, ktorý vypíše naformátovanú tabuľku mocnín 
celých čísel z nejakého daného intervalu. Prvý stĺpec 
tabuľky obsahuje číslo, v druhom je druhá mocnina tohto 
čísla, v treťom tretia, vo štvrtom štvrtá.
"""

od = int(input("Zadaj od: "))
do = int(input('Zadaj do: '))

for i in range(od,do+1):
    for k in range(1,5):
        """
        lr = len(str(do**k))
        cr = len(str(i**k))
        """
        print(str(i**k) +"\t", end="")
    print()
