import tkinter

canvas = tkinter.Canvas(height=500, width=800)
canvas.pack()

vel = 30
farba1, farba2 = 'maroon', 'gold'

x, y = 10, 10
col, row = 8, 5
for i in range(row):
    f1, f2 = farba1, farba2
    for j in range(col):
        canvas.create_rectangle(x,y,x+vel,y+vel, fill=f1)
        f1, f2 = f2, f1
        x += vel+2
    farba1, farba2 = farba2, farba1
    x = 10
    y += vel+2

tkinter.mainloop()