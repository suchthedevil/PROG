import tkinter
from random import randint
c = tkinter.Canvas(height="300", width="500")
c.pack()
r = 10
for i in range (3000):
    y,x = randint(0,300), randint(0,500)
    if y < 150 and x>y:
        c.create_oval(x-r,y-r,x+r,y+r, fill="white", outline="")
    elif y < 150 and x<=y:
        c.create_oval(x-r,y-r,x+r,y+r, fill="blue", outline="")
    elif y >= 150 and x+y<=300:
        c.create_oval(x-r,y-r,x+r,y+r, fill="blue", outline="")
    else:
        c.create_oval(x-r,y-r,x+r,y+r, fill="red", outline="")

tkinter.mainloop()