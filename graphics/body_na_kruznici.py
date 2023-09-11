#task: vytvorte body (vrcholy) pravidelneho n-uholnika

import tkinter
from math import *

canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()

n = 5
uhol = 0
sx, sy = 500, 500
r = 200
canvas.create_oval(sx-r, sy-r, sx+r, sy+r, width="2")

for i in range(n):
    x = sx + r * cos(radians(uhol))
    y = sy + r * sin(radians(uhol))
    canvas.create_oval(x-4,y-4,x+4,y+4)
    uhol += 360/n

tkinter.mainloop()

