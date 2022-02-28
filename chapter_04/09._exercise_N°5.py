import turtle
import time

def create_windows_turtle(Wclr, Wtitle):
    wn = turtle.Screen()
    wn.bgcolor(Wclr)
    wn.title(Wtitle)
    return wn

def create_turtle(clr, Tsize, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(clr)
    T.shape('turtle')
    T.shapesize(Tsize)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def create_a_square(Tx, Ssize):
    for i in range(20):
        for i in range(4):
            Tx.forward(Ssize)
            Tx.left(90)
            Ssize = Ssize + 5
    time.sleep(2)
    Tx.clear()
    Tx.hideturtle()

def create_square_ratared(T, size, angle):
    for i in range(20):
        for i in range(4):
            T.forward(size)
            T.left(90)
            size = size + 5
            T.left(-angle)
    time.sleep(1)

create_windows_turtle('lightgreen', 'Test')
Tessa = create_turtle('hotpink', 0.5, 3, 0)
create_a_square(Tessa, 5)
Alex = create_turtle('hotpink', 0.5, 3, 0)
create_square_ratared(Alex, 15, 1)
