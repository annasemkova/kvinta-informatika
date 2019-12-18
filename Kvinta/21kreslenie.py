import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

xx, yy = 0, 0
1="green"
2="blue"
3="red"
4="yellow"
5="pink"

for i in range():
    for i in range():
        farba=
        if 
        def pohyb(event):
            x, y = event.x, event.y
            global xx, yy
            xx, yy = x, y
            

        def kreslenie2(event):
            x, y = event.x, event.y
            canvas.create_line(xx,yy,x,y, fill="farba")


canvas.bind("<ButtonPress>",pohyb)
canvas.bind("<Motion>",kreslenie2)
