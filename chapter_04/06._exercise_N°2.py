import turtle

def create_windows_turtle(Wclr, Wtitle):
    wn = turtle.Screen()
    wn.bgcolor(Wclr)
    wn.title(Wtitle)
    return wn

def create_turtles(Tclr, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(Tclr)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def draw_square(T, sz):
    for i in range(4):
        T.forward(sz)
        T.left(90)

def draw_squares(Tx, size, sep):
    for i in range(5):
        draw_square(Tx, size)
        Tx.penup()
        Tx.left(-90)
        Tx.forward(sep/2)
        Tx.left(90)
        Tx.forward(-sep/2)
        Tx.pendown()
        size = size + sep

create_windows_turtle('lightgreen', 'test')
Tessa = create_turtles('hotpink', 3, 5)
draw_squares(Tessa, 20, 20)
