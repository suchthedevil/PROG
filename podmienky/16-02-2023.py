# spravit odrazajucu gulicku s odpocitavanim
"""
#13
import tkinter, random
from math import sqrt, sin, cos, radians

c = tkinter.Canvas(height=600, width=600)
c.pack()

def farebne_bodky(r, x1,y1, x2,y2, x3,y3):
    for i in range(5000):
        x, y = random.randrange(600), random.randrange(600)
        r1 = x1-x #preorobit na kruh 
        r2 = x2-x
        r3 = x3-x
        if abs(r1) <= r or abs(r2) <= r or abs(r3) <= r:
            c.create_oval(x-5,y-5,x+5,y+5, fill="yellow")
            
farebne_bodky(80, 120, 120, 180, 110, 160, 170)

tkinter.mainloop()
"""
"""
#podmienky na zaklade datoveho typu:

if type(i) == str:
    ...
"""

#funkcia vypise delitele cisla
def vypis_delitele(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)

#funkcia vrati sucet delitelov cisla
def sucet_delitele(n):
    sucet = 0
    for i in range(1,n+1): 
        if n%i == 0:
            sucet += i
    return sucet
# ak sucet delitelov cisla sa rovna cislu, cislo je dokonale
def je_dokonale(n):
    if n == sucet_delitele(n)-n:
        return True
    else:
        return False

# vypise vsetky dokonale cisla v danom intervale

def vsetky_dokonale(od,do):
    for i in range(od,do+1):
        if je_dokonale(i):
            print(f"Cislo {i} je dokonale")
vsetky_dokonale(1,10000)
        
    
    
    
    
    