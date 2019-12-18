import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

xx, yy = 0, 0
x1, y1 = 0, 0

def press(event):
    x, y = event.x, event.y
    global xx, yy, x1, y1
    xx, yy = x, y
    x1, y1 = xx, yy
    
def pohyb(event):
    x, y = event.x, event.y
    canvas.create_line(x1,y1,x,y,fill="blue")
    x1, y1 = x, y

canvas.bind("<ButtonPress>",press)
canvas.bind("<Motion>",pohyb)
canvas.bind("<ButtonRelease>",)
