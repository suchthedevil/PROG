
n = input("")
v = input("")
vysky = (list(map(int, v.split())))

for i in range(0,len(vysky)-1):
    if i == len(vysky)-2 and len(vysky) != 2:
        lava = vysky[i]
        stred = vysky[i+1]
        prava = vysky[0]
        case = 1
    elif i == len(vysky)-1 and len(vysky) != 2:
        lava = vysky[i]
        stred = vysky[0]
        prava = vysky[1]
        case = 2         
    elif len(vysky) == 2:
        case = 3
        lava = vysky[i]
        prava = vysky[i]
        stred = vysky[i+1]
    else:
        lava = vysky[i]
        stred = vysky[i+1]
        prava = vysky[i+2]
        case = 4

    if lava < stred and prava < stred:
        if case == 1:
            solution = f"{i} {i+1} {0}"
        elif case == 2:
            solution = f"{i} 0 1"
        elif case == 3 and lava < stred:
            solution = "0 1 0"
        elif case == 4:
            solution = f"{i} {i+1} {i+2}"
        break
    elif case == 3 and stred < lava:
            solution = "1 0 1"
    else:
        stred = 0
        for i in range(len(vysky)):
            if vysky[i] > stred:
                stred = vysky[i]
                index = i
        lava, prava = index, index

if not solution:
    while stred:
        lava -= 1
        if vysky[lava] < vysky[index]:
            while vysky[prava] >= vysky[index]:
                prava += 1
            solution = f"{lava} {index} {prava}"
            stred = 0

print(solution)


#ALT 2

"""
Funkcia zoberie postupne kazde n, pojde cez list kym nenajde vacsie cislo ako je ono,
zapamata si vzdialenost. Potom bude hladat zase mensie cislo a vznikne pozadovana trojica, 
vzdialenosti sa budu pamatat a scitaju sa na konci, tak zistime vzdialenost lavej od pravej, 
program printne cisla ktore maju medzi sebou najmensiu vzdialenost.


min = 10**5
for j in range(len(vysky)):
    for i in range(j,len(vysky)):
        if vysky[i] > vysky[j]:
            mid = i
            for k in range(mid,len(vysky)):
                if vysky[k] < vysky[mid]:
                    right = k
                    dist = abs(right-j)
                    if dist < min:
                        min = dist
                        solution = f"{j} {mid} {right}"
print(solution)
"""

#ALT 3

#najdeme si najvacsie cislo v liste a potom incrementujeme az kym nenajdeme zlava a sprava mensie cisla
"""
stred = 0
for i in range(len(vysky)):
    if vysky[i] > stred:
        stred = vysky[i]
        index = i
lava, prava = index, index
while stred:
    lava -= 1
    if vysky[lava] < vysky[index]:
        while vysky[prava] >= vysky[index]:
            prava += 1
        print(f"{lava} {index} {prava}")
        stred = 0
"""