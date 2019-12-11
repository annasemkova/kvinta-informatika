import tkinter
from random import randrange, randint
x_max, y_max = 200, 300
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

for i in range(10000):
    x, y = randrange(x_max), randrange(y_max)
    farba="black"
    if  x >= x_max/2:
        if y >= y_max/2:
            farba="green"
        else:
            farba="red"
    else:
        if y >= y_max/2:
            farba="blue"
        else:
            farba="yellow"

    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)
