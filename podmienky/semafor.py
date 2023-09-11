import tkinter
c = tkinter.Canvas(height="600", width="600")
c.pack()
x,y = 300,300
c.create_rectangle(x-60,y-170,x+60,y+170, width="3", fill="black")
c.create_oval(x-50,y-160,x+50,y-60, width="2", fill="#173e06", tag="green")
c.create_oval(x-50,y-50,x+50,y+50, width="2", fill="#67500a", tag="yellow")
c.create_oval(x-50,y+60,x+50,y+160, width="2", fill="#510505", tag="red")

for j in range(10):
    for i in reversed(range(1,6)):
        if i == 2:
            c.itemconfig("yellow", fill="#ffc103")
        c.itemconfig("red", fill="#ff0909")
        c.create_text(x,y+110, text=str(i), font='Arial 20', fill="white", tag=f"r{i}")
        c.delete(f"r{i+1}")
        c.update()
        c.after(1000)
    c.delete(f"r{i}")
    c.itemconfig("red", fill="#510505")
    c.itemconfig("yellow", fill="#67500a")

    for i in reversed(range(1,6)):
        c.itemconfig("green", fill="#53ff07")
        c.create_text(x,y-110, text=str(i), font='Arial 20', fill="white", tag=f"g{i}")
        c.delete(f"g{i+1}")
        c.update()
        c.after(1000)
    c.delete(f"g{i}")
    c.itemconfig("green", fill="#173e06")

tkinter.mainloop()
