n = int(input("Zadaj n: "))
pi = 0

for i in range(1,n,4):
    pi += (4/i)
for k in range(3,n,4):
    pi -= (4/k)
print(pi)

