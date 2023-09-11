import tkinter
c = tkinter.Canvas(width=300, height=800)
c.pack()

def je_prvo(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    if count == 2:
        return True
    return False
    
def kresli(prime,y):
    c.create_text(150,y, text=str(prime), font="Arial 20")
   
def cisla(cislo,pocet):
    y = 400
    p = 0
    kresli(cislo,y)
    for i in reversed(range(cislo)):
        if je_prvo(i):
            y -= 30
            kresli(i,y)
            p += 1
        if p == pocet:
            break
    p = 0
    y = 400
    while p < pocet:
        cislo += 1
        if je_prvo(cislo):
            y += 30
            kresli(cislo,y)
            p += 1
cisla(2023, 3)
c.mainloop()