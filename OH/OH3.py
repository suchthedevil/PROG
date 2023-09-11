import random

spz_DK = "DK"
spz_ZA = "ZA"
spz_MT = "MT"
pismena = "ABCDEF"

for okres in spz_DK, spz_ZA, spz_MT:
    for i in range(3):
        for i in range(4):
            print(okres + "-" + str(random.randrange(100,1000)) + random.choice(pismena) + random.choice(pismena), end=" ")
        print(okres + "-" + str(random.randrange(100,1000)) + random.choice(pismena) + random.choice(pismena), end="\n")
    print("")
