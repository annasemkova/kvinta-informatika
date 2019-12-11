import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()

for i in range(10000):
    x, y = randrange(x_max), randrange(y_max)
    farba="cyan"
    if  x <= y and y <=175:
        farba="blue"
    elif x >= y :
        farba="yellow"
    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)

