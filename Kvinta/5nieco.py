import tkinter
canvas=tkinter.Canvas(width=800,height=800)
canvas.pack()
import random

def petrzalka(x,y):
    canvas.create_rectangle(x-50,y-75,x+50,y+75)
    canvas.create_polygon(x-50,y-75,x+50,y-75,x,y-130)
    for i in range(1,4):
        canvas.create_rectangle(x-40,y-65,x-5,y-25)
        y=y+45
    y=y-135
    for i in range(1,4):
        canvas.create_rectangle(x+5,y-65,x+40,y-25)
        y=y+45
        
def petrzalskesidlisko():
    for i in range(1,random.randint(2,30)):
        petrzalka(random.randint(100,800),random.randint(100,800))

petrzalskesidlisko()
