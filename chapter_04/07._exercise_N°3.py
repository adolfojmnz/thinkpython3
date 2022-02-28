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

def create_turtles(Tclr, Psize, Tspeed):
    T = turtle.Turtle()
    T.color(Tclr)
    T.pensize(Psize)
    T.speed(Tspeed)
    return T

def draw_poly(T, Psize, Psides):
    angle = 360/Psides
    for i in range(Psides):
        T.forward(Psize)
        T.left(angle)


def draw_some_polies(Tx, size, sides, sep, quant):
    for i in range(quant):
        draw_poly(Tx, size, sides)
        Tx.penup()
        Tx.left(-90)
        Tx.forward(sep/2)
        Tx.left(90)
        Tx.forward(-sep/2)
        Tx.pendown()
        size = size + sep

create_windows_turtle('lightgreen', 'test')
Tessa = create_turtles('hotpink', 3, 1)
draw_some_polies(Tessa, 20, 15, 20, 5)

#
#
#
#
#
