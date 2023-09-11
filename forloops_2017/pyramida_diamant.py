n = int(input("Zadaj pocet: "))


for i in reversed(range(n)):
    print((i)*" ", end="")
    for k in range(1,n-i+1):
        print("O", end=" ")
    print()

for i in range(n):
    print((i)*" ", end="")
    for k in range(1,n-i+1):
        print("O",end=" ")
    print()

