import turtle

def create_windows_turtle(Wtitle):
    wn = turtle.Screen()
    wn.bgcolor('Lightgreen')
    wn.title(Wtitle)
    return wn

def create_turtles(Tclr, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(Tclr)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def draw_poly(T, Psize, Psides):
    angle = 360/Psides
    for i in range(Psides):
        T.forward(Psize)
        T.left(angle)

def draw_equitriangle(Tx, sz):
    draw_poly(Tx, sz, 3)

create_windows_turtle('EquiTriangle')
Tessa = create_turtles('hotpink', 3, 1)
draw_equitriangle(Tessa, 50)

