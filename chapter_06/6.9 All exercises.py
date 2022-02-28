import sys

def test(x):
    """ Print the result of a test """
    z = sys._getframe(1).f_lineno
    if x:
        msg = "Test at line {0}: OK.".format(z)
    else:
        msg = ("Test at line {0}: FAILED.".format(z))
    print(msg)
    return 0.0


def test_suite_v01(): # 1. Test compasses.
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("S") == "E")
    test(turn_clockwise("42") is None)


def test_suite_v02(): # 2. Return the day name of a week given an integer.
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) is None)


def test_suite_v03(): # 3. Return an integer given a week day name.
    test(day_number("Friday") == 5)
    test(day_number("Sunday") == 0)
    test(day_number(day_name(3)) == 3)
    test(day_name(day_number("Thursday")) == "Thursday")
    pass


def test_suite_v04(): # 4-5. Calculate the returning day of a trip.
    test(returning_day("Monday", 4) == "Friday")
    test(returning_day("Tuesday", 0) == "Tuesday")
    test(returning_day("Tuesday", 14) == "Tuesday")
    test(returning_day("Sunday", 100) == "Tuesday")
    pass


def test_suite_v05():
    test(returning_day("Sunday", -1) == "Saturday")
    test(returning_day("Sunday", -7) == "Sunday")
    test(returning_day("Tuesday", -100) == "Sunday")


def test_suite_v06(): # 6. Return the number of days in a specific month.
    test(how_many_days("February") == 28)
    test(how_many_days("December") == 31)


def test_suite_v07():# 7-8. Calculate the total of secs.
    test(total_secs(2, 30, 10) == 9010)
    test(total_secs(2, 0, 0) == 7200)
    test(total_secs(0, 2, 0) == 120)
    test(total_secs(0, 0, 42) == 42)
    test(total_secs(0, -10, 10) == -590)


def test_suite_v08():
    test(total_secs(2.5, 0, 10.71) == 9010)
    test(total_secs(2.433, 0, 0) == 8758)


# 9. Calculate the total of: hours, minutes and seconds given an amount of secs.
def test_suite_v09():
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

#The N°10 exercise was just analyze...

def test_suite_v11(): # 11. Campare is "a" is greater, less or iqual than "b".
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)


def test_suite_v12(): # 12. Calculate the hypotenuse of a triangle.
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)


def test_suite_v13(): # 13. Calculate the slope of a line.
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)


def test_suite_v14(n): # 14. Return "True" is a number is "even".
    print('Beggining "is even" test!')
    for i in range(2):
        if i == 0:
           print("Testing with", n)
        elif i == 1:
             print("Testing with", n)
        if n % 2 == 0:
           is_even(n)
        else:
           is_even(n)
        n = n+1


def test_suite_v15(n): # 15. Return "True" is a number is "odd".
    print('Beggining "is odd" test!')
    for i in range(2):
        if i == 0:
           print("Testing with", n)
        if i == 1:
           print("Testing with", n)
        if n % 2 != 0:
            is_odd(n)
        else:
             is_odd(n)
        n = n+1


def test_suite_v16(): # 16. Test if "f" is factor of "n".
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))


def test_suite_v17(): # 17. Test if "m" is multiple of "x".
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))


def test_suite_v18(): # 18. Temperture convertion (F° to C°).
    test(farenheint_to_celcius(212) == 100)
    test(farenheint_to_celcius(32) == 0)
    test(farenheint_to_celcius(-40) == -40)
    test(farenheint_to_celcius(36) == 2)
    test(farenheint_to_celcius(37) == 3)
    test(farenheint_to_celcius(38) == 3)
    test(farenheint_to_celcius(39) == 4)


def test_suite_v19(): # 19. Temperture convertion (C° to F°).
    test(celcius_to_farenheint(0) == 32)
    test(celcius_to_farenheint(100) == 212)
    test(celcius_to_farenheint(-40) == -40)
    test(celcius_to_farenheint(12) == 54)
    test(celcius_to_farenheint(18) == 64)
    test(celcius_to_farenheint(-48) == -54)


def turn_clockwise(compass): # 1. Test compasses.
    if compass == "N":
        return "E"
    elif compass == "S":
        return "W"
    elif compass == "E":
        return "S"
    elif compass == "W":
        return "N"
    else:
        return None


def day_name(n): # 2. Return the day name of a week given an integer.
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


def day_number(n): # 3. Return an integer given a week day name.
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


def returning_day(w_day, t_days): # 4-5. Calculate the returning day of a trip.
    return (day_name((t_days + (day_number(w_day)) ) % 7))
    #a = t_days % 7
    #b = day_number(w_day)
    #c = ((a + b) % 7)
    #return (day_name(c))


def how_many_days(month): # 6. Return the number of days in a specific month.
    if month == "January":
       return 31
    if month == "February":
       return 28
    if month == "March":
       return 31
    if month == "April":
       return 30
    if month == "May":
       return 31
    if month == "June":
       return 30
    if month == "July":
       return 31
    if month == "August":
       return 31
    if month == "September":
       return 30
    if month == "Octuber":
       return 31
    if month == "November":
       return 30
    if month == "December":
       return 31
    else:
         return None


def total_secs(hours, minutes, seconds): # 7-8. Calculate the total of secs.
    return int((hours*3600) + (minutes * 60) + seconds)

# 9. Calculate the total of: hours, minutes and seconds given an amount of secs.
def hours_in(seconds):
    total_hours = seconds // 3600
    return total_hours

def minutes_in(seconds):
    total_minutes = (seconds % 3600) // 60
    return total_minutes

def seconds_in(seconds):
    total_seconds = seconds % 60
    return total_seconds

# 10. Just analyze...

def compare(a, b): # 11. Campare is "a" is greater, less or iqual than "b".
    if a > b:
       return 1
    if a == b:
       return 0
    if a < b:
       return -1


def hypotenuse(a, b): # 12. Calculate the hypotenuse of a triangle.
    return (((a**2) + (b**2)) ** 0.5)


def slope(x1, y1, x2, y2): # 13. Calculate the slope of a line.
    return (y2-y1)/(x2-x1)


def intercept(x1, y1, x2, y2): # 13.2. Calculate the Y-interception of a line.
    return (y2 - (x2 * (slope(x1, y1, x2, y2))))


def is_even(n): # 14. Return "True" is a number is "even".
    if n % 2 == 0:
       print("The number is even")
       return True
    else:
         print("The number is odd")
         return False


def is_odd(n): # 15. Return "True" is a number is "odd".
    if n % 2 != 0:
        print("The number is odd")
        return True
    else:
        print("The number is even")
        return False


def is_factor(f, n): # 16. Test if "f" is factor of "n".
    if n % f == 0:
        return True
    else:
         return False


def is_multiple(m, x): # 17. Test if "m" is multiple of "x".
    return (is_factor(x, m))


def farenheint_to_celcius(t): # 18. Temperture convertion (F° to C°).
    return(round( 5/9 *(t-32)))


def celcius_to_farenheint(t): # 19. Temperture convertion (C° to F°).
    return(round(9/5 * t) + 32)


test_suite_v01()
test_suite_v02()
test_suite_v03()
test_suite_v04()
test_suite_v05()
test_suite_v06()
test_suite_v07()
test_suite_v08()
test_suite_v09()
test_suite_v11()
test_suite_v12()
test_suite_v13()
test_suite_v14(0)
test_suite_v15(0)
test_suite_v16()
test_suite_v17()
test_suite_v18()
test_suite_v19()
