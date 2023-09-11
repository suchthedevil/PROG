import tkinter
from math import *

canvas = tkinter.Canvas(height=500, width=800)
canvas.pack()

sirka, vyska = 300, 200
x, y = 20, 20

canvas.create_rectangle(x,y, x+sirka,y+vyska/2, fill="white")
canvas.create_rectangle(x,y+vyska/2, x+sirka, y+vyska, fill="red")
canvas.create_polygon(x,y, x+sqrt(vyska**2-(vyska/2)**2),y+vyska/2, x,y+vyska, fill="blue")


tkinter.mainloop()