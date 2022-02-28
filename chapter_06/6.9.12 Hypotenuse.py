#-------------------------------------------------------------------------------
# Name:        Exercise N°12: Calculate the hypotenuse of a right triangle
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     23/06/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
       msg = "Test at line {0} OK.".format(linenum)
    else:
         msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def test_suite_v12():
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)


def hypotenuse(a, b):
    return (((a**2) + (b**2)) ** 0.5)

test_suite_v12()