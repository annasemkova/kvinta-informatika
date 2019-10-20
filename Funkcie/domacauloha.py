import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

def strom():
    x=random.randint(1,800)
    y=random.randint(1,800)
    canvas.create_rectangle(x-10,y,x+10,y+150,fill="brown")
    w=random.randint(30,100)
    canvas.create_oval(x-w,y-w,x+w,y+w,fill="limegreen")

def trava():
    x=random.randint(1,800)
    y=random.randint(1,800)
    for i in range(1,random.randint(4,11)):
        canvas.create_line(x,y,x+random.randint(-10,10),y-random.randint(1,20),fill="green",width=random.randint(1,3))

for i in range(1,11):
    strom()

for i in range(1,21):    
    trava()
