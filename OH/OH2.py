word = input("Zadaj slovo: ")
n = int(input("Zadaj pocet riadkov: "))

for k in range(n//4):
    for i in range(4):
        print(4*i*" " + word)
for i in range(n%4):
    print(4*i*" " + word)
