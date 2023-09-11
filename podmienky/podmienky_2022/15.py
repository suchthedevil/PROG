import tkinter, random

canvas = tkinter.Canvas(height=300, width=300)
canvas.pack()

red = 0
count = 0

for i in range(10000):
    count += 1
    x, y = random.randrange(2,298), random.randrange(2,298)
    if x**2 + y**2 <= 300**2:
        canvas.create_oval(x-2,y-2,x+2,y+2, outline="", fill="red")
        red += 1
    else: 
        canvas.create_oval(x-2,y-2,x+2,y+2, outline="", fill="blue")

tkinter.mainloop()
print((red/count)*4)