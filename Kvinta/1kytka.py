import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="pink")
canvas.pack()
import random

def kytka(a,b,r):
    canvas.create_oval(a,b-r,a+2*r,b+r,fill="blue",outline="mediumblue")
    canvas.create_oval(a-2*r,b-r,a,b+r,fill="blue",outline="mediumblue")
    canvas.create_oval(a-r,b,a+r,b+2*r,fill="blue",outline="mediumblue")
    canvas.create_oval(a-r,b-2*r,a+r,b,fill="blue",outline="mediumblue")
    canvas.create_oval(a-r,b-r,a+r,b+r,fill="#FFFFE0",outline="#FFFFE0")
    
for i in range(1,101):
    x=random.randint(1,800)
    y=random.randint(1,800)
    z=random.randint(1,50)
    kytka(x,y,z)
    
