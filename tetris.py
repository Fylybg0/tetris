from tkinter import *
from random import *
import _tkinter

width=15
height=20

if height>=28:
    height=27

hw_p=30

counter=0
obsadene=[]
speed=150
okno=1
okejno=1
down="can"

shapes_colours=["blue","red","green","yellow"]
abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z","Q","Á","Ó"]
obsadene_policka=[]
class Start:
    def __init__(self):
        self.running=0
        self.shapes=None
        self.key=None

    def start(self):
        if self.running==0:
            global obsadene_policka
            obsadene_policka=[]
            for i in range(width):
                obsadene_policka.append(f"{abeceda[height]}{i+1}")
            for i in range(height):
                obsadene_policka.append(f"{abeceda[i]}0")
                obsadene_policka.append(f"{abeceda[i]}{width+1}")
            a.set("0")
            global okno
            okno=1
            platno.delete("all")
            print("Game started!")
            self.movement=Movement()
            self.shapes=Shapes()
            self.running=1
            self.shapes.generuj()

    def stop(self):
        if self.running==1:
            platno.delete("all")
            print("Game stopped!")
            self.running=0
            self.shapes.move_to_stop()

    def movemm(self,event):
        if self.running==1:
            if event.keysym in ["Right","Left","Down"]:
                self.shapes.movem(event)


class Shapes:
    def __init__(self):
        self.shape= None
        self.move= Movement()
        self.colour= choice(shapes_colours)

    def generuj(self):
        global shapes_colours
        if self.colour=="blue":
            shapes_colours=["blue","red","red","green","green","yellow","yellow","red","green","yellow"]
            self.move.generuj("blue")
        elif self.colour=="red":
            shapes_colours=["blue","blue","red","green","green","yellow","yellow","blue","green","yellow"]
            self.move.generuj("red")
        elif self.colour=="green":
            shapes_colours=["blue","blue","red","red","green","yellow","yellow","blue","red","yellow"]
            self.move.generuj("green")
        elif self.colour=="yellow":
            shapes_colours=["blue","blue","red","red","green","green","yellow","blue","red","green"]
            self.move.generuj("yellow")


    def movem(self,event):
        self.move.left_right(event)

    def move_to_stop(self):
        self.move.stopp()


class Movement:
    def __init__(self):
        global counter, obsadene_policka
        self.c_obsadene=[]
        self.zc_obsadene=[]
        self.key=None
        self.z_obsadene=[]
        self.shape=None
        self.location=1
        self.colour=None
        self.flag=None
        self.shapes=None
        self.runningg=1
        self.jou="ano"
        self.start=None


    def stopp(self):
        global speed, obsadene, obsadene_policka, down
        down="can"
        Game.running=0
        self.runningg=0
        self.start=Start()
        obsadene=[]
        self.z_obsadene=[]
        self.jou="ano"
        self.shape=None

    def generuj(self,colour):
        global speed, counter, obsadene
        if self.runningg==1:
            self.colour=colour
            self.shape=None
            if self.colour=="blue":
                self.shape= platno.create_rectangle(hw_p*int(width/2-1),0,hw_p+hw_p*int(width/2-1),hw_p*4,fill="blue",width=0)
                obsadene=[f"A{int(width/2)}",f"B{int(width/2)}",f"C{int(width/2)}",f"D{int(width/2)}"]
            elif self.colour=="red":
                self.shape= platno.create_polygon(hw_p*int(width/2-1),0,hw_p*int(width/2-1),hw_p*2,hw_p+hw_p*int(width/2-1),hw_p*2,hw_p+hw_p*int(width/2-1),hw_p*3,hw_p*2+hw_p*int(width/2-1),hw_p*3,
                                                  hw_p*2+hw_p*int(width/2-1),hw_p,hw_p+hw_p*int(width/2-1),hw_p,hw_p+hw_p*int(width/2-1),0,fill="red",width=0)
                obsadene=[f"A{int(width/2)}",f"B{int(width/2)}",f"B{int(width/2+1)}",f"C{int(width/2)+1}"]
            elif self.colour=="green":
                self.shape= platno.create_polygon(hw_p*int(width/2-1),0,hw_p*int(width/2-1),hw_p,hw_p*int(width/2-1)+hw_p,hw_p,hw_p*int(width/2-1)+hw_p,hw_p*3,hw_p*2+hw_p*int(width/2-1),hw_p*3,
                                                  hw_p*2+hw_p*int(width/2-1),0,fill="green",width=0)
                obsadene=[f"A{int(width/2)}",f"A{int(width/2)+1}",f"B{int(width/2+1)}",f"C{int(width/2)+1}"]
            elif self.colour=="yellow":
                self.shape= platno.create_rectangle(int(width/2-1)*hw_p,0,hw_p*int(width/2-1)+hw_p*2,hw_p*2,fill="yellow",width=0)
                obsadene=[f"A{int(width/2)}",f"A{int(width/2)+1}",f"B{int(width/2)}",f"B{int(width/2)+1}"]
            platno.update()
            platno.after(150)
            if self.runningg == 1:
                counter+=1
                self.go_down()

    def left_right(self,event):
        global speed, counter, obsadene, okejno, down
        if self.runningg==1 and okejno==1:
            self.key=event.keysym
            if self.key=="Right":
                self.c_obsadene=obsadene
                for i in self.c_obsadene:
                    self.zc_obsadene.append(f"{i[0]}{int(i[1:])+1}")
                for i in self.zc_obsadene:
                    if i in obsadene_policka:
                        self.jou="nie"
                        break
                if self.jou=="nie":
                    self.jou="ano"
                else:
                    obsadene=self.zc_obsadene
                    self.zc_obsadene=[]
                    platno.move(counter,hw_p,0)
                    platno.update()
                self.zc_obsadene=[]
            elif self.key=="Left":
                self.c_obsadene=obsadene
                for i in self.c_obsadene:
                    self.zc_obsadene.append(f"{i[0]}{int(i[1:])-1}")
                for i in self.zc_obsadene:
                    if i in obsadene_policka:
                        self.jou="nie"
                        break
                if self.jou=="nie":
                    self.jou="ano"
                else:
                    obsadene=self.zc_obsadene
                    self.zc_obsadene=[]
                    platno.move(counter,-hw_p,0)
                    platno.update()
                    self.zc_obsadene=[]
            elif self.key=="Down" and down=="can":
                speed=5
                down="cannot"

    def go_down(self):
        global speed, obsadene, okno, okejno, down, counter, obsadene_policka
        if self.runningg==1:
            self.shapes=Shapes()
            for i in range(len(obsadene)):
                for x in range(len(abeceda)):
                    if obsadene[i][0] == abeceda[x]:
                        self.z_obsadene.append(f"{abeceda[x+1]}{obsadene[i][1:]}")
            for i in self.z_obsadene:
                if i in obsadene_policka:
                    obsadene_policka+=obsadene
                    for i in range(width):
                        if f"A{i+1}" in obsadene_policka:
                            okno=0
                            c.set("GAME OVER")
                            if int(a.get())>int(b.get()):
                                b.set(a.get())
                            self.stopp()
                            break
                    if okno != 0 :
                        okejno=0
                        obsadene=[]
                        speed=150
                        down="can"
                        a.set(int(a.get())+1)
                        self.shapes.generuj()
                else:
                    okejno=1
                    self.flag="Jop"
            if self.flag=="Jop":
                obsadene=self.z_obsadene
                self.z_obsadene=[]
                if self.runningg==1 and okno != 0:
                    platno.move(self.shape,0,hw_p)
                    platno.update()
                    platno.after(speed)
                    self.go_down()

def stop_game():
    Game.stop()
    root.destroy()
def on_quit():
    Game.stop()
    root.destroy()


root=Tk()
root.title("Tetris")

platno=Canvas(width=width*hw_p,height=height*hw_p,bg="black")
platno.grid(row=0,column=1,rowspan=height)

Game=Start()

But1=Button(root, text="Start", command=Game.start,width=20)
But1.grid(row=1,column=0)
But2=Button(root, text="Stop", command=Game.stop,width=20)
But2.grid(row=2,column=0)
But3=Button(root, text="Koniec", command=stop_game,width=20)
But3.grid(row=3,column=0)
a,b,c=StringVar(),StringVar(),StringVar()
a.set("0")
b.set("0")
c.set("")
Label(root,textvariable=c).grid(row=5,column=0)
Label(root,text="GAME SCORE").grid(row=7,column=0)
Label(root,textvariable=a).grid(row=8,column=0)
Label(root,text="HIGH SCORE").grid(row=9,column=0)
Label(root,textvariable=b).grid(row=10,column=0)


root.protocol("WM_DELETE_WINDOW", on_quit)
platno.bind_all("<Key>",Game.movemm)

but1=Button()
root.mainloop()
