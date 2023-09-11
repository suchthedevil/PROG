import tkinter, random

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

for i in range(6000):
    x, y = random.randrange(5,495), random.randrange(5,495)
    if x<y:
        if 500 - x < y:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="green", outline="" )
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="red", outline="" )
    else:
        if 500 - x < y:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="yellow", outline="" )
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5, fill="blue", outline="" )
    

tkinter.mainloop()
