import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

def vlak(y,p,farba):
    x=100
    for i in range(1,p+1):
        canvas.create_line(x-60,y,x+60,y)
        canvas.create_rectangle(x-50,y-30,x+50,y+30,fill=farba)
        canvas.create_oval(x-30,y+25,x-10,y+45,fill="black")
        canvas.create_oval(x+30,y+25,x+10,y+45,fill="black")
        x+=120

vlak(50,4,"red")
vlak(250,2,"green")
vlak(450,3,"blue")
