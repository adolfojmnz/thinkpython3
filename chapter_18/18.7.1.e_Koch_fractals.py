import turtle

def koch(t, order, size):
    """ Make turtle "t" draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction. """

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


alex = turtle.Turtle()
alex.penup()
alex.setpos(-150, 150)
alex.pendown()

for angle in [120, 120, 120]:
    koch(alex, 3, 300)
    alex.right(angle) 

turtle.Screen().mainloop()

