import turtle
import time

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Automatic traffic light!")
wn.bgcolor("lightgreen")

akame = turtle.Turtle()

akame.penup()
akame.setpos(-40, -100)
akame.pendown()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    akame.pensize(3)
    akame.color("black", "darkgrey")
    akame.begin_fill()
    akame.forward(80)
    akame.left(90)
    akame.forward(200)
    akame.circle(40, 180)
    akame.forward(200)
    akame.left(90)
    akame.end_fill()
    akame.penup()
    # Position tess onto the place where the green light should be
    akame.forward(40)
    akame.left(90)
    akame.forward(50)
    akame.hideturtle()

def automatic_traffic_lights():
    tatsumi = turtle.Turtle()
    tatsumi.hideturtle()
    tatsumi.penup()

    itachi = turtle.Turtle()
    itachi.hideturtle()
    itachi.penup()

    minato = turtle.Turtle()
    minato.hideturtle()
    minato.penup()

    tatsumi.shape('circle')
    tatsumi.shapesize(3)
    tatsumi.setpos(0, -50)

    itachi.setpos(0, 20)
    itachi.shape('circle')
    itachi.shapesize(3)

    minato.setpos(0, 90)
    minato.shape('circle')
    minato.shapesize(3)

    count = 0
    while count < 4:
        count += 1
        tatsumi.showturtle()
        tatsumi.fillcolor("green")
        time.sleep(3)
        tatsumi.hideturtle()

        itachi.showturtle()
        itachi.fillcolor("orange")
        time.sleep(2)
        itachi.hideturtle()

        minato.showturtle()
        minato.fillcolor("red")
        time.sleep(5)
        minato.hideturtle()

def leave():
    wn.bye()

draw_housing()
wn.onkey(automatic_traffic_lights, "2")
wn.onkey(leave, 'q')
wn.listen()
wn.mainloop()