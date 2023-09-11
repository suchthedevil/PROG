"""
Pomocou tohto programu vieme zaplniť štvorcovú tabuľku n x n 
číslami od 1 do n**2
Oprav tento program tak, aby vypísal túto tabuľku trikrát vedľa seba

n = int(input('zadaj n: '))
for i in range(n):
    for j in range(n):
        print(f'{i*n + j + 1:2}', end=' ')
    print()

"""

n = int(input('zadaj n: '))
for i in range(n):
    for l in range(3):
        for j in range(n):
            print(f'{i*n + j + 1:2}', end=' ')
        print("   ",end='')
    print()

