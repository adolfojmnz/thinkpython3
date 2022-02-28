#-------------------------------------------------------------------------------
# Name:        Exercises N° 13/14: Slope and Y-Interception
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     24/06/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
       print("Test at line {0} OK.".format(linenum))
    else:
         print ("Test at line {0} FAILED.".format(linenum))


def test_suite_v13():
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)


def test_suite_v14():
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


def intercept(x1, y1, x2, y2):
    return (y2 - (x2 * (slope(x1, y1, x2, y2))))

test_suite_v13()
test_suite_v14()
