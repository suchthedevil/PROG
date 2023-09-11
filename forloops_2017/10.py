q = int(input("Zadaj pocet cisel: "))

sum = 0
for i in range(1,q+1):
    num = float(input(f"Zadaj {i} cislo: "))
    sum += num
    
print(f"Sucet je: {sum}")
print(f"Priemer je: {sum/q}")