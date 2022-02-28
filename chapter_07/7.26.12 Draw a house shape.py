import turtle

def create_window():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    return wn


def create_turtle():
    tx = turtle.Turtle()
    tx.color('hotpink')
    tx.speed(1)
    tx.pensize(1)
    return tx

def draw_shape(tx):
    tx.lt(45)
    tx.fd(64) # 1

    tx.lt(135)
    tx.fd(40) # 2

    tx.lt(135)
    tx.fd(64) # 3

    tx.lt(-135)
    tx.fd(40) # 4

    tx.lt(-90)
    tx.fd(50) # 5

    tx.lt(-45)
    tx.fd(50) # 6

    tx.lt(-135)
    tx.fd(50) # 7

    tx.lt(-45)
    tx.fd(50) # 8


wn = create_window()
tessa = create_turtle()

draw_shape(tessa)

wn.mainloop()
