import turtle, time

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Automatic traffic light!")
wn.bgcolor("#808000")

akame = turtle.Turtle()

akame.penup()
akame.setpos(-40, -100)
akame.pendown()

tatsumi = turtle.Turtle()
tatsumi.hideturtle()
tatsumi.penup()

itachi = turtle.Turtle()
itachi.hideturtle()
itachi.penup()

minato = turtle.Turtle()
minato.hideturtle()
minato.penup()


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

    clr = '#202513'
    tatsumi.setpos(0, -50)
    tatsumi.shape('circle')
    tatsumi.shapesize(3)
    tatsumi.fillcolor(clr) # DARKGREEN
    tatsumi.stamp()

    itachi.setpos(0, 20)
    itachi.shape('circle')
    itachi.shapesize(3)
    itachi.fillcolor(clr)  # DARKORANGE
    itachi.stamp()

    minato.setpos(0, 90)
    minato.shape('circle')
    minato.shapesize(3)
    minato.fillcolor(clr) # DARKRED
    minato.stamp()

def automatic_traffic_lights():
    count = 0
    while count < 4:
        count += 1
        tatsumi.showturtle()
        tatsumi.fillcolor("#00FF00")
        time.sleep(3)
        tatsumi.hideturtle()

        itachi.showturtle()
        itachi.fillcolor("#FFD700")
        time.sleep(2)
        itachi.hideturtle()

        minato.showturtle()
        minato.fillcolor("#FF0000")
        time.sleep(5)
        minato.hideturtle()


def leave():
    wn.bye()

draw_housing()
automatic_traffic_lights()

wn.onkey(leave, 'q')
wn.listen()
wn.mainloop()