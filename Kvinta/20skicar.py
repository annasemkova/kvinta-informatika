import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

r=10
xx, yy = 0, 0

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x-r,y-r,x+r,y+r,outline="red", fill="red")
    global xx, yy
    xx, yy = x, y

def pusti(event):
    x, y = event.x, event.y
    canvas.create_oval(x-r,y-r,x+r,y+r,outline="blue", fill="blue")
    canvas.create_line(xx,yy,x,y)

canvas.bind("<ButtonPress>", klik)
canvas.bind("<ButtonRelease>", pusti)
