import tkinter, random
from math import sqrt

canvas = tkinter.Canvas(height=600, width=600)
canvas.pack()

x0, y0 = 300, 300
r = 150

for i in range(2001):
    x, y = random.randrange(10,590), random.randrange(10,590)
    dist = sqrt((y-y0)**2 + (x-x0)**2)
    if dist < r:
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="red", outline="")
    else:
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="yellow", outline="")

tkinter.mainloop()
