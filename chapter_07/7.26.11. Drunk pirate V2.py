import turtle


def create_windown():
    wn = turtle.Screen()
    wn.bgcolor("black")
    return wn


def create_turtle():
    tx = turtle.Turtle()
    tx.speed(3)
    tx.pensize(1)
    tx.color("hotpink")
    return tx


def drunk_pirate_v2(xs):
    tx = create_turtle()
    for angle, steps in xs:
        tx.lt(angle)
        tx.fd(steps)


xs = [(160, 200), (-43, 100), (270, 80), (-43, 120)]
wn = create_windown()
drunk_pirate_v2(xs)
wn.mainloop()