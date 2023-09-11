n = int(input("Zadaj pocet: "))

for i in reversed(range(n)):
    print((i)*" ", end="")
    for k in range(1,n-i+1):
        print(k, end=" ")
    print()

