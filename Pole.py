import turtle as t
class Pole(object):
    def __init__(self,name,stack,top_po,x_po,y_po,thinckness,length,color):
        self.name = name
        self.stack =stack
        self.top_po = top_po
        self.x_po = x_po
        self.y_po = y_po
        self.thinckness = thinckness
        self.length = length
        self.color = color

    def showpole(self):
        for i in range(2):
            t.fillcolor(self.color)
            t.begin_fill()
            t.fd(10)
            t.left(90)
            t.fd(100)
            t.left(90)
            t.end_fill()
        t.mainloop()
    def clear_pole(self):
        t.clear()
    


a = Pole(1,1,1,1,1,1,1,"red")
a.showpole()
a.clear_pole()
