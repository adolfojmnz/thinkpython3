"""
    2) Define a new kind of Turtle, TurtleGTX, that comes with some extra features:

        a)  It can jump forward a given distance

        b)  It has an odometer that keeps track of how far the turtle has travelled
            since it came off the production line.

        c)  The parent class has a number of synonyms like fd, forward, back,
            backward, and bk. For this exercise, just focus on putting this
            functionality into the forward method.

    3) After travelling some random distance, your turtle should break down with a
       flat tyre.

        a)  After this happens, raise an exception whenever forward is called.
            Also provide a change_tyre method that can fix the flat.

       P.S: Think carefully about how to count the distance if the turtle is asked to
            move forward by a negative amount. (We would not want to buy a second-hand
            turtle whose odometer reading was faked because its previous owner drove
            it backwards around the block too often. Try this in a car near you, and
            see if the car’s odometer counts up or down when you reverse.)
"""

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


if __name__ == '__main__':
    mike = TurtlGTX()
    mike.attributes(tcolor='green')
    mike.forward(600)
    mike.tscreen.mainloop()