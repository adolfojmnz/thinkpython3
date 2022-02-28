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


def returning_day(week_day, total_days):
    if total_days >= 0:
       a = total_days % 7
    else:
         a = - (abs(total_days) % 7)
         if a < 0 :
            a = 7 + a
    b = day_number(week_day)
    print(day_name(a + b))
    return day_name(a + b)


def returning_day_2(week_day, total_days):
    if total_days >= 0:
       a = total_days % 7
    else:
         a = - (abs(total_days) % 7)
    b = day_number(week_day)
    print(day_name(a + b))


returning_day_2("Wednesday", -1)