import turtle
def create_windows_turtle():
    wn = turtle.Screen()
    wn.bgcolor('Lightgreen')
    wn.title("Draw a bar's graphic")
    return wn
def create_turtles(Tclr0, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(Tclr0)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T
def draw_a_square(t):
    for i in range(4):
        t.fd(40)
        t.left(90)
def place_turtle(t):
    t.pu()
    t.setpos(-280, -200)
    t.pd()
create_windows_turtle()
Tessa = create_turtles('darkblue', 3, 5)
draw_a_square(Tessa)
