import tkinter
from random import randrange, randint
x_max, y_max = 500, 350
canvas=tkinter.Canvas(width=x_max,height=y_max)
canvas.pack()


for i in range(10000):
    x, y = randrange(x_max), randrange(y_max)
    farba="cyan"
    if  x <= 100 and y <= 150:
        farba="red"
    elif 150 <= x and y <= 150:
            farba="red"
    elif x <= 100 and 200 <= y:
        farba="red"
    elif 150 <= x and 200 <= y:
        farba="red"
    else:
        farba="blue"

    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)

