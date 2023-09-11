"""
Program dá rovnaký výsledok ako v úlohe (3), ale najprv pripraví
celý výstup (všetky riadky s trojicami čísel) do jedného znakového 
reťazca (aj so znakmi '\n') a až po skončení cyklu tento reťazec 
vypíše.
"""

od = int(input("Zadaj od: "))
do = int(input("Zadaj do: "))

a = str()

for i in range(od,do+1):
    c = (str(i) + " " + str(i**2) + " " + str(i**3)) + "\n"
    a += c
print(a)
