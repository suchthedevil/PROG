import tkinter, random

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

for i in range(6000):
    x, y = random.randrange(5,495), random.randrange(5,495)
    if x>125 and x<375:
        if y>125 and y<375:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="red", outline="")
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue", outline="")
    else: 
        canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue", outline="")

tkinter.mainloop()
