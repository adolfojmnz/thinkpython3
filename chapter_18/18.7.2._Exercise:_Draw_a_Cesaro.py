from createturtle import turtle, createTurtle

def cesaro(t, order, size):

    if order == 0:
        t.forward(size/2)
    else:
        for angle in [-85, 170, -85, 0]:
            cesaro(t, order-1, (size/2))
            t.left(angle)

def draw_figure(turt, order, size, sides, angle):
    for i in range(sides):
        cesaro(turt, order, size)
        turt.left(angle)
    turt.hideturtle()

# Create turtle's instances.
tess = createTurtle(x_coord=-600, y_coord= 300, speed=0)
alex = createTurtle(x_coord=-600, y_coord= 150, speed=0)
mike = createTurtle(x_coord=-600, y_coord=   0, speed=0)
eren = createTurtle(x_coord=-600, y_coord=-150, speed=0)

# Functions call.
for (order,turt) in enumerate([tess, alex, mike, eren]):
    draw_figure(turt, order, 100, 4, -90)


# Wait until the window's close.
turtle.Screen().mainloop()

