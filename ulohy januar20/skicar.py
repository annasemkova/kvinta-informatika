import tkinter
from random import randrange, randint
x_max,y_max=800,600
canvas=tkinter.Canvas(width=x_max,height=y_max,bg="white")
canvas.pack()

x1,y1=0,0
farba, hrubka = "black", 3

def klik(event):
    global x1,y1
    canvas.bind("<B1-Motion>",kreslenie)
    x1,y1=event.x,event.y
    
    x,y=event.x,event.y
    global farba, hrubka
    if  y >= y_max-50 and x >= x_max-50:
        farba="red"
    elif y >= y_max-50 and x_max-50 > x >= x_max-100:
        farba="blue"
    elif y >= y_max-50 and x_max-100 > x >= x_max-150:
        farba="black"
    else:
        pass

    if  y >= y_max-50 and 50 > x >= 2:
        hrubka=1
    elif y >= y_max-50 and 100 > x >= 50:
        hrubka=5
    elif y >= y_max-50 and 150 > x >= 100:
        hrubka=10
    else:
        pass

    if x_max > x >= x_max-150 and 45 >= y > 1:
        canvas.delete("all")
        tlacidla()

    print(hrubka)
    print(farba)

def tlacidla():
    #hrubka
    canvas.create_rectangle(2,y_max-50,50,y_max,outline="black")
    canvas.create_rectangle(50,y_max-50,100,y_max,outline="black")
    canvas.create_rectangle(100,y_max-50,150,y_max,outline="black")
    canvas.create_line(10,y_max-40,40,y_max-10,width=1)
    canvas.create_line(60,y_max-40,90,y_max-10,width=5)
    canvas.create_line(110,y_max-40,140,y_max-10,width=10)

    #farba
    canvas.create_rectangle(x_max-150,y_max-50,x_max-100,y_max,fill="black")
    canvas.create_rectangle(x_max-100,y_max-50,x_max-50,y_max,fill="blue")
    canvas.create_rectangle(x_max-50,y_max-50,x_max,y_max,fill="red")

    #vymaz
    canvas.create_rectangle(x_max-150,1,x_max,45,fill="black")
    canvas.create_text(x_max-70,20,fill="white",font="Times 12 bold",text="VYMAŽ VŠETKO")

def kreslenie(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=hrubka,fill=farba)
    x1,y1=x,y

canvas.bind("<Button-1>", klik)

tlacidla()
   
