import tkinter
canvas=tkinter.Canvas(width=800,height=800)
canvas.pack()
import random

#pocet stlpcov=s, pocet poschodi=p


def panelak(x,y,s,p):
    #obvod
    canvas.create_rectangle(x,y,x+s*50,y+p*50,fill="yellow")
    #pocet stlpcov
    a=0
    for i in range(1,s+1):
            #pocet poschodi
            for i in range(1,p+1):
                canvas.create_rectangle(x+10,y+10,x+40,y+40,fill="lightblue")
                y=y+50
            a=a+1
            y=y-p*50
            x=x+50
        #tu treba vratit x,y na povodne hodnoty, a x posunut na dalsi stlpec a prerobit a

def mesto(k):
    #k=pocet panelakov
    for i in range(1,k+1):
        panelak(random.randint(10,700),random.randint(10,700),random.randint(1,10),random.randint(1,10))


mesto(random.randint(1,15))
