import random

count = 0
money = 10

while count < 1000 and money != 0:
    count += 1
    n1, n2, n3 = random.randrange(1,21), random.randrange(1,21), random.randrange(1,21)
    if n1 == n2 == n3:
        money += 100
        print("+100", end="")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        money += 5
        print("+5", end="")
    else:
        money -= 1
        print("-1", end="")

print(f"\nZostalo mi {money} Eur")

