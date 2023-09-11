import tkinter

c = tkinter.Canvas(height=500, width=900)
c.pack()
# den = #89CFF0
# noc = #000026
c.create_rectangle(0,350,900,500, fill="green", outline="")
c.create_rectangle(0,0,900,350, fill="#000026", outline="", tag="obloha")
strom = tkinter.PhotoImage(file="pictures/strom1.png")
c.create_image(700,250, image=strom)

tkinter.mainloop()