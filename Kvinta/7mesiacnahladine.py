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

def dvamesiace(v,x1,y1,x2,y2,a2,b2,v2):
    x1=random.randint(230,480)
    y2=random.randint(10,290)
    b=400-y2-v
    mesiac(x1,y2,"yellow","white",v)
    mesiac(x1,400+b,"yellow","darkblue",v)

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

def logo(x,y,v):
    v2=v/8*3
    h=v/8
    #x,y=stred danej veci
    mesiac(x+h,y,"lightblue","red",v)
    obratenymesiac(x-v-h,y,"lightblue","red",v)
    
def cervenavlajka():
    vlajka(620,"red")
    logo(695,180,40)

def lod(x,y,q):
    canvas.create_rectangle(fill="brown",outline="brown")
    #vlajka
    canvas.create_polygon(fill="beige",outline="black")
    #trup
    canvas.create_polygon(x-q,y-q/2,x+q,y-q/2,x-q/2,y+q/2,x+q/2,y+q/2,fill="lightbrown",outline="black")
    
cervenavlajka()
zelenavlajka()
more()

for i in range(1,50):
    canvas.delete("all")
    dvamesiace(100)
    canvas.update()
    canvas.after(500)
    
