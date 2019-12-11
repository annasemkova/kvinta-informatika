import tkinter
from random import randrange, randint
x_max, y_max = 500, 500
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

for i in range(10000):
    x, y = randrange(x_max), randrange(y_max)
    farba="cyan"
    if  x <= x_max/5:
        farba="red"
    elif x <= x_max/5*2:
        farba="yellow"
    elif x <= x_max/5*3:
        farba="green"
    elif x <= x_max/5*4:
        farba="blue"

    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)

