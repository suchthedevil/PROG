import tkinter, random
from math import *
canvas = tkinter.Canvas(width=800,height=800)
canvas.pack()

x, y = 400, 400
r = 150

n = 18
uhol = 0
while True:
    for i in range(n):
        xc = x + r*cos(radians(uhol))
        yc = y + r*sin(radians(uhol))
        h = random.randrange(20,200)
        canvas.create_polygon(xc,yc, x+r*cos(radians(uhol+360/n)),y+r*sin(radians(uhol+360/n)),x+(r+h)*cos(radians(uhol+180/n)), y+(r+h)*sin(radians(uhol+180/n)), fill="yellow", outline="maroon",tags=f"r")
        canvas.create_oval(x-r,y-r,x+r,y+r, fill="yellow",outline="yellow")
        uhol += 360/n
    canvas.update()
    canvas.after(200)
    canvas.delete("r")

tkinter.mainloop()