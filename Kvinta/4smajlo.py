import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="pink")
canvas.pack()
import random

def smajlo(x,y,a):
    ##obrys
    canvas.create_rectangle(x,y,x+a,y+a)
    ##oci
    ox1=random.randint(x+5,x+a/2-5)
    oy1=random.randint(y+5,y+a/2-5)
    ox2=random.randint(x+a/2+5,x+a-5)
    oy2=random.randint(y+a/2+5,y+a-5)
    canvas.create_rectangle(ox1,oy1,ox1,oy1)
    canvas.create_rectangle()
    ##nos
    canvas.create_rectangle()
    ##usta
    canvas.create_rectangle()


smajlo(random.randint(1,600),random.randint(1,600),150)
     
