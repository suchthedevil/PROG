import tkinter, random

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

x1, y1 = 0, 0
x2, y2 = 500, 500

for i in range(10):
    x, y = random.randrange(5,495), random.randrange(5,495)
    canvas.create_oval(x-2,y-2, x+2,y+2, fill="red")
    if x > x1:
        x1 = x
    if  y > y1:
        y1 = y
    if x < x2:
        x2 = x
    if y < y2:
        y2 = y
    else:
        pass

canvas.create_rectangle(x2,y2,x1,y1)
    




tkinter.mainloop()