"""
Program prečíta celé číslo (maximálne 8-ciferné) a potom v cykle 
(8-krát) postupne toto číslo skracuje o poslednú cifru, zároveň 
vypisuje skrátené číslo aj poslednú cifru, o ktorú bolo skrátené.
"""

n = int(input("Zadaj cislo: "))

for i in str(n):
    digit = n%10
    n = n//10
    print(str(n) + " " + str(digit))

