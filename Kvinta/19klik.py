import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

def klik(event):
    x, y = event.x, event.y
    r = 5
    canvas.create_oval(x-r,y-r,x+r,y+r,outline="red", fill="red")

def pohyb(event):
    x, y = event.x, event.y
    r = 5
    canvas.create_oval(x-r,y-r,x+r,y+r,outline="blue", fill="blue")
    canvas.create_oval(a-r,y-r,a+r,y+r,outline="red", fill="red")

#canvas.bind("<ButtonPress>", klik)
canvas.bind("<Motion>", pohyb)
