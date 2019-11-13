import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

x,y=60,60
for i in range(1,10):
    canvas.delete("all")
    canvas.create_rectangle(x,y,x+50,y+50)
    x=x+10
    canvas.update()
    canvas.after(500)
