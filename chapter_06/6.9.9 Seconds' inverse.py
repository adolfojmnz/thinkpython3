#-------------------------------------------------------------------------------
# Name:        module1
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
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0}: OK.".format(linenum)
    else:
        msg = ("Test at line {0}: FAILED.".format(linenum))
    print(msg)


def test_suite_v9():
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

def hours_in(seconds):
    total_hours = seconds // 3600
    return total_hours


def minutes_in(seconds):
    total_minutes = (seconds % 3600) // 60
    return total_minutes

def seconds_in(seconds):
    total_seconds = seconds % 60
    return total_seconds

test_suite_v9()
