import random

s = random.randrange(2,15)
r = random.randrange(2,15)

print("+" + s*"-" + "+")

for i in range(r):
    print("|" + s*" " + "|")

print("+" + s*"-" + "+")

