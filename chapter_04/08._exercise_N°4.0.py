#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     28/05/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

def create_windows_turtle(Wclr, Wtitle):
    wn = turtle.Screen()
    wn.bgcolor(Wclr)
    wn.title(Wtitle)
    return wn

def create_turtle(clr, Tsize, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(clr)
    T.shape('turtle')
    T.shapesize(Tsize)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def create_a_square(Tx, Ssize):
    for i in range(4):
        Tx.forward(Ssize)
        Tx.left(90)

def create_pretty_pattern(Trtl, squares, size, Rangle):
    for i in range(squares):
        Trtl.forward(size/2)
        Trtl.left(90)
        Trtl.forward(-size/2)
        create_a_square(Trtl, size)
        Trtl.forward(-size/2)
        Trtl.left(90)
        Trtl.forward(size/2)
        Trtl.left(Rangle)

create_windows_turtle('lightgreen', 'Pretty Patter')
Tessa = create_turtle('blue', 0.5, 3, 0)

create_pretty_pattern(Tessa, 24, 100, 360/24)
