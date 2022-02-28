import turtle

def createTurtle(speed=5, color='green', bgcolor='black', x_coord=-150, y_coord=-150):
    tess = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor(bgcolor)

    tess.speed(speed)
    tess.color(color)

    tess.penup()
    tess.setpos(x_coord, y_coord)
    tess.pendown()
    
    return tess, wn

if __name__ == '__main__': 
    createTurtle()

