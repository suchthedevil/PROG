count = 1
spravne = 1
vyska = 0

while True:
    predosla = int(vyska)
    vyska = input(f"Zadaj {count}. vysku: ")
    if vyska == "":
        break
    elif predosla < int(vyska):
        spravne += 1
    else: 
        pass
    count += 1

if spravne == count:
    print("Zoradeni spravne")
else:
    print("Zoradeni nespravne")
