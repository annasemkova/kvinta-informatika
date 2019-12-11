import tkinter
from random import randrange, randint
x_max, y_max = 500, 500
canvas=tkinter.Canvas(width=x_max,height=y_max,background="black")
canvas.pack()

#stred obrazovky = x_max/2, y_max/2
s1, s2 = x_max/2, y_max/2

for i in range(100):
    x, y = randrange(x_max), randrange(y_max)
    farba="cyan"
    if  x <= x_max/2 and y <= y_max/2:
        farba="red"
    elif x <= x_max/2 and y >= y_max/2:
            farba="yellow"
    elif x >= x_max/2 and y <= y_max/2:
        farba="blue"
    elif x >= x_max/2 and y >= y_max/2:
        farba="green"
    else: print("chyba v matrixe") 

    canvas.create_line(s1,s2,x,y,fill=farba,width="3")

