import tkinter
from math import *
canvas = tkinter.Canvas(height=600, width=600)
canvas.pack()

x, y = 300, 300
r = 200
l = r-r/7-40

for i in range(1,13):
    canvas.create_text(x+(r+30)*sin(radians(30*i)),y-(r+30)*cos(radians(30*i)), text=str(i), font="arial 30 bold") 
canvas.create_oval(x+r,y+r, x-r,y-r, width=5)
canvas.create_oval(x+r/8,y+r/8, x-r/8,y-r/8, width=5)

for i in range(1,61):
    a, b = x+(r/8)*sin(radians(6*i)), y-(r/8)*cos(radians(6*i))
    canvas.create_line(a,b, a+(l)*sin(radians(6*i)), b-(l)*cos(radians(6*i)), arrow=tkinter.LAST, width=5, tags=f"s{i}")
    canvas.delete(f"s{i-1}")
    canvas.after(1000)
    canvas.update()

tkinter.mainloop()
