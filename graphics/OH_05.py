import math, tkinter 

canvas = tkinter.Canvas(width = 400, height = 400)
canvas.pack()

x0, y0 = 200, 200
r1 = 50
r2 = 110
r3 = 140
n = 30
uhol = 0
v, v1 = r2, r3
a, b, c = 0, 0, 0
for l in range(20000):
    canvas.update()
    canvas.after(100)
    canvas.delete('stred')
    canvas.delete('luce')
    for i in range (0, n):
        uhol += i * (360/n)
        
        x1 = x0 + r1 * math.cos(math.radians(uhol))
        y1 = y0 + r1 * math.sin(math.radians(uhol))
        x2 = x0 + v * math.cos(math.radians(uhol + ((360)/n)/2))
        y2 = y0 + v * math.sin(math.radians(uhol + ((360)/n)/2))
        x3 = x0 + r1 * math.cos(math.radians(uhol + (360/n)))
        y3 = y0 + r1 * math.sin(math.radians(uhol + (360/n)))
        a = x1, y1
        b = x2, y2
        c = x3, y3

        canvas.create_polygon(a, b, c, fill = 'gold', outline = 'orange', tag = 'luce')
        
        uhol = 0
        v, v1 = v1, v
    v, v1 = v1, v
    canvas.create_oval(x0 - r1, y0 - r1, x0 + r1, y0 + r1, fill = 'gold', outline = 'gold', tag = 'stred')   

'''
for i in range (1, n+1):
    uhol += i * (360/n)
    x1 = x0 + r1 * math.cos(math.radians(uhol))
    y1 = y0 + r1 * math.sin(math.radians(uhol))
    x2 = x0 + r2 * math.cos(math.radians(uhol + ((360)/n)/2))
    y2 = y0 + r2 * math.sin(math.radians(uhol + ((360)/n)/2))
    x3 = x0 + r1 * math.cos(math.radians(uhol + (360/n)))
    y3 = y0 + r1 * math.sin(math.radians(uhol + (360/n)))

    canvas.create_polygon()
    canvas.create_text(x1, y1, text='+')
    canvas.create_text(x2, y2, text='+')
    canvas.create_text(x3, y3, text=i, fill = 'red')
    uhol = 0   
'''

tkinter.mainloop()