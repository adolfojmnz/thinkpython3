import turtle
import time

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Automatic traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.penup()
tess.setpos(-40, -100)
tess.pendown()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    tess.penup()
    # Position tess onto the place where the green light should be
    tess.forward(40)
    tess.left(90)
    tess.forward(50)

def automatic_traffic_lights():
    tess.shape("circle")
    tess.shapesize(3)
    count = 0
    while count < 2:
        count += 1
        tess.fillcolor("green")
        time.sleep(3)

        tess.forward(70)
        tess.fillcolor("orange")
        time.sleep(2)

        tess.forward(70)
        tess.fillcolor("red")
        time.sleep(5)
        tess.back(140)
    if count >= 2:
        tess.hideturtle()

def leave():
    wn.bye()

draw_housing()
wn.onkey(automatic_traffic_lights, "2")
wn.onkey(leave, 'q')
wn.listen()
wn.mainloop()