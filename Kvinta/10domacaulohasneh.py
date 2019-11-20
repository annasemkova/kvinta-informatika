import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

def vlocka(x,y):
    canvas.create_oval(x,y,x+10,y+10,fill="turquoise")
for i in range(1,101):
    canvas.delete("all")
    for i in range(1,102):
        vlocka(random.randint(1,800),random.randint(1,800))
    canvas.update()
    canvas.after(100)
