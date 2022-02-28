import turtle

def draw_clock(T, radius, speed, angle):
    for a in range(12):
        T.color('green')
        T.shape('turtle')
        T.shapesize(0.5)
        T.penup()
        T.speed(speed)
        T.forward(radius)
        T.stamp()
        T.forward(-radius)
        T.left(angle)
    for x in range(12):
        T.forward(radius - 15)
        T.pendown()
        T.color('green')
        T.pensize(1)
        T.forward(5)
        T.penup()
        T.forward(10 - radius)
        T.left(angle)

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Tessa draws a clock')

tessa = turtle.Turtle()
draw_clock(tessa, 150, 5, 30)

wn.mainloop
