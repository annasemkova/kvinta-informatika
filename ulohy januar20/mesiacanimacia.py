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

x1=random.randint(230,480)
y2=random.randint(10,290)

def dvamesiace(v):
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

def lod1(m,q):
    lod(m,400,20)
    q*=1
    
def lod2(n,q):
    lod(n,450,40)
    q*=2

def lod3(o,q):
    lod(o,550,80)
    q*=3
    
def flotila():     
    m,n,o=1,1,1
    for i in range(500):
        q=10
        canvas.delete("all")
        cervenavlajka()
        zelenavlajka()
        more()
        dvamesiace(100)
        lod1(m,q)
        m+=q
        lod2(n,q)
        n+=2*q
        lod3(o,q)
        o+=3*q
        canvas.update()
        canvas.after(100)

flotila()
