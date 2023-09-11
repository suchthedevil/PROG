"""
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
    sum += int(vyska)
    count += 1

if spravne == count:
    print("Zoradeni spravne")
else:
    print("Zoradeni nespravne")

print(f"Priemer ziakov je: {sum/count}")
"""
"""
def nsn(a,b):
    an = a
    bn = b
    count_a = 2
    count_b = 2
    if a < b:
        while an != bn:
            while an < bn:
                an = a*count_a
                count_a += 1
            if an == bn:
                print(an)
                break
            else:
                bn = b*count_b
                count_b += 1
    else:
        while an != bn:
            while an > bn:
                bn = b*count_b
                count_b += 1
            if an == bn:
                print(an)
                break
            else:
                an = a*count_a
                count_a += 1
nsn(4,3)
"""
"""
def riadok(n, text=''):
    print("*"*(int(n)-int(len(text))//2), end=" ")
    print(text, end=" ")
    print("*"*(int(n)-int(len(text))//2))
riadok(20, 'Jan Botto')
"""
"""
import tkinter, math, random

canvas = tkinter.Canvas(height="500", width="500")
canvas.pack()

suma = int(input("Zadaj pociatocnu sumu: "))
pocet = 1000

while suma > 0 and pocet > 0:
    prve = random.randrange(1,21)
    druhe = random.randrange(1,21)
    tretie = random.randrange(1,21)
    
    if prve == druhe and druhe == tretie:
        suma += 100
        print("+100", end =" ")
    elif prve==druhe or druhe==tretie or prve==tretie:
        suma += 5
        print("+5", end =" ")
    else:
        suma -= 1
        print("-1", end =" ")
    pocet -= 1
print()
print(suma)
print(pocet)
        
tkinter.mainloop()
"""
"""
#log2

cislo = 1000
od, do = 0, cislo
x = cislo

while abs(2**x-cislo) > 0.001:
    x = (od+do)/2
    if 2**x > cislo:
        do = x
    else:
        od = x
print(x)
"""
#ceska vlajka

import tkinter, math, random

canvas = tkinter.Canvas(height="500", width="500")
canvas.pack()

for i in range(3000):
    x, y = random.randrange()
        
tkinter.mainloop()


