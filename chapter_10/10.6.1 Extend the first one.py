import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tx = turtle.Turtle()
pz = 0

"""
def decrease_pensize():
    global pz
    if pz > 1:
        tx.pensize(pz-1)
        pz -= 1
    return pz

def increase_pensize():
    global pz
    if pz < 20:
        tx.pensize(pz+1)
        pz += 1
    return pz
"""
def cr():
    tx.color('red')

def cg():
    tx.color('green')

def cb():
    tx.color('blue')

def h1():
   tx.forward(20)

def h2():
   tx.back(20)

def h3():
   tx.left(45)

def h4():
    tx.right(45)

def b():
    wn.bye()

def pu():
    tx.pu()

def pd():
    tx.pd()

def square():
    tx.shape('square')

def circle():
    tx.shape('circle')

def stamp():
    tx.stamp()

def bgfill():
    tx.begin_fill()

def edfill():
    tx.end_fill()

wn.onkey(h1, "Up")              # Move turtle 20 pixels forward
wn.onkey(h2, "Down")            # Move turtle 20 pixels backward
wn.onkey(h3, "Left")            # Turn turtle 45 degrees counter-clockwise
wn.onkey(h4, "Right")           # Turn turtle 45 degrees clockwise
wn.onkey(b, 'q')                # Close turtle's windows

wn.onkey(cr, 'r')               # Change turtle's color to red
wn.onkey(cg, 'g')               # Change turtle's color to gree
wn.onkey(cb, 'b')               # Change turtle's color to blue

#wn.onkey(increase_pensize, '+') # Increase turtle's pensize by 1 unit
#wn.onkey(decrease_pensize, '-') # Decrease turtle's pensize by 1 unit

wn.onkey(pu, 'u')               # PenUp
wn.onkey(pd, 'd')               # PenDown
wn.onkey(square, 's')           # Draw a square
wn.onkey(circle, 'c')           # Draw a circle
wn.onkey(stamp, 'm')
wn.onkey(bgfill, 'Control_L')   # Bigging fill
wn.onkey(edfill, 'Shift_L')     # End fill

wn.listen()
wn.mainloop()