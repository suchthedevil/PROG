import tkinter

canvas = tkinter.Canvas()
canvas.pack()

n = 13
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 12
        if j == i or j+i == n-1:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

tkinter.mainloop()