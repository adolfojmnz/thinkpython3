import turtle


def create_windown():
    wn = turtle.Screen()
    wn.bgcolor("black")

def create_turtle():
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)
    t.color("hotpink")
    return t

def drunk_pirate(tx):
    tx.left(-160)
    tx.fd(100)
    tx.left(43)
    tx.fd(100)
    tx.left(-270)
    tx.fd(100)
    tx.left(97)
    tx.fd(100)
    tx.left(43)
    tx.fd(100)
    tx.left(-200)
    tx.fd(100)
    tx.left(940)
    tx.fd(100)
    tx.left(-17)
    tx.fd(100)
    tx.left(86)
    tx.fd(100)

tessa = create_turtle()
drunk_pirate(tessa)
