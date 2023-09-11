import tkinter, random
c = tkinter.Canvas(height="600", width="600")
c.pack()
x,y = 300,300

c.create_oval(x-20,y-20,x+20,y+20, fill="red",tag="ball")

for i in range(100):
    xm, ym = random.randrange(-5,6), random.randrange(-5,6)
    while x >= 20 and x <= 580 and y >= 20 and y <= 580:
        c.move("ball",xm,ym)
        x += xm
        y += ym
        c.after(10)
        c.update()
    x -= xm
    y -= xm




tkinter.mainloop()