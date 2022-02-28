#-------------------------------------------------------------------------------
# Name:        draw_rectangle
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     28/05/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_rectangle(t, w, h):
    """Get the turte to draw a rectangle of widht w and height h"""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz):
    draw_rectangle(tx, sz, sz)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draw a rectangle")

tessa = turtle.Turtle()
#draw_square(tessa, 50)
draw_rectangle(tessa, 50, 40)

wn.mainloop()