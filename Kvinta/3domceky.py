import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="pink")
canvas.pack()
import random

def dom(x,y,a):
    canvas.create_rectangle(x,y,x+2*a,y+2*a)
    canvas.create_polygon(x,y,x+2*a,y,x+a,y-a)

def osada():
    x=random.randint(1,750)
    y=random.randint(1,750)
    for i in range(1,4):
        a=50
        dom(x,y,a)
        x=x+3*a
    
osada()
     
