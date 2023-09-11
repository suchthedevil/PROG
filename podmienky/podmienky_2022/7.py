import tkinter

canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

n = 3753
x, y = 450, 50

print(f"{n:o}")

for i in range(len(str(n))+1):
    canvas.create_rectangle(x-20,y-20,x,y, fill="cyan")
    cifra = str(n%8)
    n //= 8
    canvas.create_text(x-10, y-10, text=f"{cifra}")
    x -= 22


tkinter.mainloop()