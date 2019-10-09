import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

#zadanie=michalpuskel.github.io

def mesiac(x,y,a,b,v,v2):
    #a=farba mesiaca b=farba pozadia v=priemer jedného kruhu v2=vzdialenost oboch kruhov
    canvas.create_oval(x,y,x+v,y+v,fill=a,outline=a)
    canvas.create_oval(x+v2,y,x+v2+v,y+v,fill=b,outline=b)

def more():
    canvas.create_rectangle(0,400,850,850,fill="darkblue",outline="darkblue")

def dvamesiace(v,v2):
    x1=random.randint(230,480)
    y2=random.randint(10,290)
    b=400-y2-v
    mesiac(x1,y2,"yellow","white",v,v2)
    mesiac(x1,400+b,"yellow","darkblue",v,v2)

def vlajka(x,k):
    #k=farba vlajky
    canvas.create_rectangle(x,150,x+150,250,fill=k)
    canvas.create_line(x,180,x,350)
    canvas.create_oval(x-150,350,x+150,650,fill="brown")

def zelenavlajka():
    vlajka(80,"darkgreen")
    mesiac(130,175,"red","darkgreen",50,20)

def obratenymesiac(x,y,a,b,v,v2):
    canvas.create_oval(x,y,x+v,y+v,fill=a,outline=a)
    canvas.create_oval(x+v2-v,y,x+v2,y+v,fill=b,outline=b)
    


def logo(x,y,a,b,v,v2):
    mesiac(x,y,a,b,v,v)
    obratenymesiac(x,y,a,b,v,v2)
    

vlajka(620,"red")
zelenavlajka()
more()
dvamesiace(100,40)
obratenymesiac(50,50,"red","pink",50,30)
#logo(50,50,"yellow","pink",100,80)
