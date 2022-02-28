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
#__import__('turtle').__traceable__ = False

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    tess.pensize(3)
    tess.speed(1)

    for i in ['red', 'purple', 'hotpink', 'blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('black')

tess = turtle.Turtle()
size = 20
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10
    tess.forward(10)
    tess.left(-18)

wn.mainloop()
