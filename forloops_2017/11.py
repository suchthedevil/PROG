"""
Program prečíta dve celé čísla a zo znakov '+', '-' a '|' 
vypíše obdĺžnik veľkosti podľa zadaných čísel.
"""
import random
col = random.randint(1,20)
row = random.randint(1,20)

print("+" + col*"-" + "+")
for i in range(row):
    print("|" + (col)*" " + "|")
print("+" + col*"-" + "+")

