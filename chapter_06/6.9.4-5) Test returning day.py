import sys


def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0}: OK.".format(linenum)
    else:
        msg = ("Test at line {0}: FAILED.".format(linenum))
    print(msg)


def day_name(n):
    if n == 0:
        return "Sunday"
    if n == 1:
        return "Monday"
    if n == 2:
        return "Tuesday"
    if n == 3:
        return "Wednesday"
    if n == 4:
        return "Thursday"
    if n == 5:
        return "Friday"
    if n == 6:
        return "Saturday"
    else:
        return None
    pass


def day_number(n):
    if n == "Sunday":
        return 0
    if n == "Monday":
        return 1
    if n == "Tuesday":
        return 2
    if n == "Wednesday":
        return 3
    if n == "Thursday":
        return 4
    if n == "Friday":
        return 5
    if n == "Saturday":
        return 6
    else:
        return None
    pass


def test_suite_v5():
    test(returning_day("Sunday", -1) == "Saturday")
    test(returning_day("Sunday", -7) == "Sunday")
    test(returning_day("Tuesday", -100) == "Sunday")
    pass

def returning_day(week_day, total_days):
    return (day_name(((total_days % 7) + (day_number(week_day)) ) % 7))
    #a = total_days % 7
    #b = day_number(week_day)
    #c = ((a + b) % 7)
    #return (day_name(c))


test_suite_v5()