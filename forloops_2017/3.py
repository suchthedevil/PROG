"""
Program prečíta dve celé čísla od a do a vypíše tabuľku druhých
a tretích mocnín všetkých čísel z intervalu <od, do
"""

od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))

for i in range(od,do+1):
    print(str(i) + " " + str(i**2) + " " + str(i**3))

