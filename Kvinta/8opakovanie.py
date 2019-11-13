import tkinter
canvas=tkinter.Canvas(width=800,height=800,background="white")
canvas.pack()
import random

#zadanie=michalpuskel.github.io

X_MAX, Y_MAX = 800, 800

def stvorec(x,y,s):
    canvas.create_rectangle(x-s/2,y-s/2,x+s/2,y+s/2)

def kamarati(x,y,s,m,p):
#x,y a strana najvacsieho stvorca, m=medzera, p=pocet vsetkych stvorcov
    for i in range(1,p+1):
        stvorec(x,y,s)
        s=s-m*2

for i in range(1,11):
    s=random.randint(150,300)
    x=random.randint(s/2,X_MAX-s/2) 
    y=random.randint(s/2,Y_MAX-s/2)
    m=3
    p=random.randint(5,10)
    kamarati(x,y,s,m,p)


