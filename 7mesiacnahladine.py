import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

#zadanie=michalpuskel.github.io

def mesiac(x,y,a,b,v):
    #x,y=polohy prvého "hlavného" kruhu
    #a=farba mesiaca b=farba pozadia v=priemer jedného kruhu v2=vzdialenost oboch kruhov
    v2=v/8*3
    canvas.create_oval(x,y,x+v,y+v,fill=a,outline=a)
    canvas.create_oval(x+v2,y,x+v2+v,y+v,fill=b,outline=b)

def more():
    canvas.create_rectangle(0,400,850,850,fill="darkblue",outline="darkblue")

def dvamesiace(x1,y2):
    v=100
    b=400-y2-v
    mesiac(x1,y2,"yellow","white",100)
    mesiac(x1,400+b,"yellow","darkblue",100)

def vlajka(x,k):
    #k=farba vlajky
    canvas.create_rectangle(x,150,x+150,250,fill=k)
    canvas.create_line(x,180,x,350)
    canvas.create_oval(x-150,350,x+150,650,fill="brown")

def zelenavlajka():
    vlajka(80,"darkgreen")
    mesiac(130,175,"red","darkgreen",50)

def obratenymesiac(x,y,a,b,v):
    v2=v-(v/8*3)
    canvas.create_oval(x,y,x+v,y+v,fill=a,outline=a)
    canvas.create_oval(x+v2-v,y,x+v2,y+v,fill=b,outline=b)

def logo(x,y,pozadie,v):
    v2=v/8*3
    h=v/8
    #x,y=stred danej veci
    mesiac(x+h,y,"lightblue",pozadie,v)
    obratenymesiac(x-v-h,y,"lightblue",pozadie,v)
    
def cervenavlajka():
    vlajka(620,"red")
    logo(695,180,"red",40)

def lod(x,y,q):
    canvas.create_rectangle(x-q/5,y-q/2-2*q,x+q/5,y-q/2,fill="#B45F04",outline="#B45F04")
    #vlajka
    canvas.create_polygon(x,y-q/2-2*q,x+q/2,y-q/2-2*q/3,x,y-q/2-q/10,fill="beige",outline="black")
    #trup
    canvas.create_polygon(x-q,y-q/2,x+q,y-q/2,x+q/2,y+q/2,x-q/2,y+q/2,fill="#B45F04",outline="black")
    logo(x,y,"#B45F04",q/3)

def lodkyvkope():
    lod(400,400,20)
    lod(300,450,40)
    lod(200,500,60)

def vsetkookremmesiaca():
    cervenavlajka()
    zelenavlajka()
    more()
    lodkyvkope()

y=350
for i in range(1,70):
    canvas.delete("all")
    vsetkookremmesiaca()
    dvamesiace(400,y)
    y=y-10
    canvas.update()
    canvas.after(50)
    
