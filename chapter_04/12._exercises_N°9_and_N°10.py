#-------------------------------------------------------------------------------
# Name:        Excercises N°9 and N°10
# Purpose:     Educational
#
# Author:      Adolfo Jimenez
#
# Created:     28/05/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def create_windows_turtle(Wtitle):
    wn = turtle.Screen()
    wn.bgcolor('darkgreen')
    wn.title(Wtitle)
    return wn

def create_turtles(Tclr, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(Tclr)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def draw_star(T, Psize, Psides):
    for i in range(5):
        for i in range(Psides):
            T.left(144)
            T.forward(Psize)
        #T.penup()
        T.forward(200)
        #T.pendown()
        T.left(-144)

wn = create_windows_turtle('Draw a star')
Tessa = create_turtles('black', 3, 5)
draw_star(Tessa, 100, 5)

wn.mainloop()
