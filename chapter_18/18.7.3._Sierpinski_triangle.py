from createturtle import createTurtle

def sierpinski(turt, order, size):
    if order == 0:
        for angle in [120, 120, 120]:
            turt.fd(size/3)
            turt.left(angle)
    else:
        for angle in [120, 120, 120]:
            sierpinski(turt, order-1, size)


tess, wn = createTurtle(x_coord=-50, y_coord=50, speed=1)
sierpinski(tess, 1, 300)

close = False
if close:
    wn.mainloop()
else:
    from time import sleep
    sleep(.5)
