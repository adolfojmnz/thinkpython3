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


def returning_day_2(week_day, total_days):
    print(day_name(((total_days % 7) + (day_number(week_day)) ) % 7))
    #a = total_days % 7
    #b = day_number(week_day)
    #c = ((a + b) % 7)
    #print (day_name(c))


returning_day_2("Tuesday", -100)
