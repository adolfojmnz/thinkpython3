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

def draw_bar(t, height, width, sep):
    if height >= 200:
        t.fillcolor('red')
    elif  height > 100 and height < 200:
        t.fillcolor('yellow')
    elif height < 100:
        t.fillcolor('green')

    if height >= 0:
       t.begin_fill()
       t.lt(90)
       t.fd(height)
       t.write('    ' + str(height))
       t.lt(-90)
       t.fd(width)
       t.lt(-90)
       t.fd(height)
       t.lt(90)
       t.end_fill()
       t.pu()
       t.fd(sep)
       t.pd()
    elif height < 0:
         t.write('    ' + str(height))
         t.fd(width)
         t.pu()
         t.fd(sep)
         t.pd()

def place_turtle(t):
    t.pu()
    t.setpos(-280, -200)
    t.pd()

create_windows_turtle()
Tessa = create_turtles('darkblue', 3, 3)
place_turtle(Tessa)

xs = [48, 117, 200, 240, 160, 260, 220, 120, 70, 24, -8]
for v in xs:
    draw_bar(Tessa, v, 40, 10)
