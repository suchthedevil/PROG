import tkinter, random
from math import *
canvas = tkinter.Canvas(width=800,height=800)
canvas.pack()

x, y = 400, 400
r = 150
h1, h2 = 40, 150
n = 40
uhol = 0
for k in range(20000):
    for i in range(n):
        xc = x + r*cos(radians(uhol))
        yc = y + r*sin(radians(uhol))
        canvas.create_polygon(xc,yc, x+r*cos(radians(uhol+360/n)),y+r*sin(radians(uhol+360/n)),x+(r+h1)*cos(radians(uhol+180/n)), y+(r+h1)*sin(radians(uhol+180/n)), fill="yellow", outline="maroon",tags=f"r")
        canvas.create_oval(x-r,y-r,x+r,y+r, fill="yellow",outline="yellow")
        uhol += 360/n
        h1, h2 = h2, h1
    canvas.after(50)
    canvas.update()
    canvas.delete("r")
    uhol += 360/n

tkinter.mainloop()