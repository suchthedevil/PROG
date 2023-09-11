import tkinter

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

x, y = 50,50
a = 100

canvas.create_rectangle(x,y, x+a,y+a, fill="red")
canvas.create_text(x+a/2,y+a/2, font="arial 20", text="cerveny", fill="yellow")
canvas.create_rectangle(x+a+10,y, x+a+110,y+100, fill="blue")
canvas.create_text(x+a+10+a/2,y+a/2, font="arial 20", text="modry", fill="yellow")
canvas.mainloop()

#velkost pisma sa da menit len naraz s fontom
