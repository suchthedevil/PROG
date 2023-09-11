import tkinter, random

canvas = tkinter.Canvas(height=400, width=600)
canvas.pack()

k = 25
x, y = 20, 20
for i in range(10):
    sum = 0
    while sum < k:
        num = random.randrange(1,5)
        sum += num
        canvas.create_oval(x-10,y-10,x+10,y+10, fill="white")
        canvas.create_text(x,y, text=str(num), font="Arial 10")
        x += 25
    if sum == k:
        canvas.create_text(x+75, y, text="HURA", fill="green")
    else: 
        canvas.create_text(x+75, y, text="ŠKODA", fill="red")
    y += 25
    x = 20

tkinter.mainloop()