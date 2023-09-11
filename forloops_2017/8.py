"""
Program prečíta číslo n a potom do jedného riadka postupne vypisuje 
n čísel tak, aby sa stále striedalo týchto sedem čísel: 0 1 2 3 4 5 6
"""

n = int(input("Zadaj n: "))

for i in range(n//7):
    print("0 1 2 3 4 5 6", end=" ")
for i in range(n%7):
    print(i, end=" ")
