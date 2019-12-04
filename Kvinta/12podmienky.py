import tkinter
from random import randrange, randint
x_max, y_max = 200, 300
canvas=tkinter.Canvas(width=x_max,height=y_max,background="white")
canvas.pack()


r = 10
x, y = randint(r, x_max-r), randrange(y_max)

dx=1
dy=1

while True:
    canvas.delete("all")
    canvas.create_oval(x-r,y-r,x+r,y+r,fill="blue")
    y+=dy
    x+=dx
    canvas.update()
    canvas.after(1)
    if y == y_max-r or y == r:
        dy*= -1
    if x == x_max-r or x == r:
        dx*= -1
