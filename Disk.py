import turtle 

class Disk(object):
    def __init__(self,name, x, y, h, w, c):
        self.t = turtle.Turtle()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.c = c

    def showdisk(self):
        self.t.penup()
        self.t.goto(self.x,self.y)
        self.t.pendown()
        self.t.fillcolor(self.c)
        self.t.begin_fill()
        self.t.fd(self.w / 2)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w)
        self.t.left(90)
        self.t.fd(self.h)
        self.t.left(90)
        self.t.fd(self.w / 2)
        self.t.end_fill()

    def newpos(self,x,y):
        self.x = x
        self.y = y

    def cleardisk(self):
        self.t.clear()

            

disk1 = Disk("test",100,100,20,100,"RED")
disk2 = Disk("test",80,10,20,100,"BLUE")

disk1.showdisk()
disk2.showdisk()
disk1.cleardisk()


