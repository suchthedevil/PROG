import random

spz_DK = "DK"
spz_ZA = "ZA"
spz_MT = "MT"
pismena = "ABCDEF"

for okres in spz_DK, spz_ZA, spz_MT:
    for i in range(3):
        for i in range(4):
            v = (okres + "-")
            for i in range(3):
                num = str(random.randrange(0,10))
                v += num
            v += random.choice(pismena) + random.choice(pismena)
            print(v,end=" ")
        c = (okres + "-")
        for i in range(3):
            num = str(random.randrange(0,10))
            c += num
        c += random.choice(pismena) + random.choice(pismena)
        print(c,end="\n")
    print()




"""
            print(okres + "-" + str(random.randrange(100,1000)) + random.choice(pismena) + random.choice(pismena), end=" ")
        print(okres + "-" + str(random.randrange(100,1000)) + random.choice(pismena) + random.choice(pismena), end="\n")
    print()
"""