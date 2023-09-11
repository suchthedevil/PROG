import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

x, y = 190, 130
r = 120
k = 5
count = 1

while r>15:
    if count%k == 0:
        canvas.create_oval(x-r,y-r,x+r,y+r, outline="grey")
    else:
        canvas.create_oval(x-r,y-r,x+r,y+r, outline="black")
    r -= 5
    count += 1

tkinter.mainloop()