import turtle as Turtle
import time

class TurtlGTX:

    def __init__(self):
        self.turtle = Turtle.Turtle()
        self.tscreen = self.turtle.getscreen()
        self.odometer = 0
        self.tyrehealt = 500
    
    def attributes(self, bgcolor='#1d2828', tcolor='#d79921'):
        self.tscreen.bgcolor(bgcolor)
        self.turtle.color(tcolor)

    def left(self, angle):
        self.turtle.left(angle)

    def right(self, angle):
        self.turtle.right(angle)

    def backward(self, units):
        self.forward(-units)
        pass

    def back(self, units):
        self.forward(-units)
        pass

    def bk(self, units):
        self.forward(-units)
        pass

    def fd(self, units):
        self.forward(units)
        pass

    def mechanic(self):
        if self.tyrehealt <= 0:
            self.tyrehealt = 500
    
    def change_tyre(self):
        print(f"We'e got a fla tyre! Let's try to fix it.")
        for event in ['Tools', 'Noises', 'Tyre out', 'Tyre in']:
            print(f"{event}...")
            time.sleep(2)
        self.mechanic()
        print("It's fixed! Let's continue that road.")


    def move(self, direction, steps):
        self.turtle.forward(steps)
        self.tyrehealt -= abs(steps)
        self.odometer += abs(steps)

    def forward(self, units):
        try:
            if (self.tyrehealt - abs(units)) >= 0:
                self.move('fd', units)
            else:
                untravelled = (abs(units) - self.tyrehealt) * (units//abs(units))
                travell = self.tyrehealt * (units//abs(units))
                self.move('fd', travell)
                raise
        except:
            self.change_tyre()
            self.move('fd', untravelled)