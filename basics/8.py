
n = int(input("Zadajte n: "))
"""
for i in range(n//7):
    for i in range(7):
        print(i, end=" ")

for i in range(n%7):
    print(i, end=" ")
"""

#better
for i in range(n):
    print(i%7, end=" ")

