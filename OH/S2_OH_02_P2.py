import tkinter
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

def stvorce(vel,retazec):
    x, y = 50, 50
    while retazec:
        if " " not in retazec:
            color = retazec
            canvas.create_rectangle(x,y,x+vel,y+vel, fill=color)
            break
        else:
            color = retazec[:retazec.find(" ")]
            retazec = retazec[retazec.find(" ")+1:]
            canvas.create_rectangle(x,y,x+vel,y+vel, fill=color)
        x += vel+5

stvorce(40,"red blue purple red gold")

tkinter.mainloop()
